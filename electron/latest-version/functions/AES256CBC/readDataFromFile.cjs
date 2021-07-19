const fs = require('fs');
const AES256CBC = require('./AES256CBC');

// (暗号化済み)ファイルから文字列を少しずつ取得して最後にまとめて返すやつ
const readFileEx = async(filepath) => {
  let cryptoedtext = '';
  const stream = fs.createReadStream(filepath, {
    encoding: "utf8",         // 文字コード
    highWaterMark: 1024       // 一度に取得するbyte数
  });
  await new Promise((resolve, reject) => {
    stream.on("data", (chunk) => cryptoedtext += chunk);
    stream.on("end", () => resolve(cryptoedtext));
    stream.on("error", (err) => reject());
  });
  return cryptoedtext;
}

const decrypto = async (text) => {
  // 僕の欲しい配列をつくるzoy
  let decryptotext = [];
  let splited = text.split('.');
  let t2pecf = splited[0].substr(0, 8);
  let prof = splited[0].slice(8);
  splited.shift(); // 先頭削除
  splited.unshift(prof);
  splited.unshift(t2pecf);
  // 僕の欲しい配列完成(壊したら二度とやらないよ)
  for (let i = 1; i < splited.length; i++) {
    // 配列内の各文字列を役割ごとに分割
    let type = splited[i].substr(0, 7).replace(/=/g, '');
    let key = splited[i].substr(7, 43);
    let iv = splited[i].substr(50, 22);
    let body = splited[i].slice(72);
    let plaintext = ((await AES256CBC.AES256CBC.decode(key, iv, body)).replace(/\x13|\x16|\r|\n+$/g, ''));
    fs.appendFileSync('predec-by-node.dat', plaintext + '\n')
    let adddata = { [type]: await toObjorList(plaintext) };
    decryptotext.push(adddata);
  }
  return decryptotext;
}

// 文字列になってしまったやつを戻す
const toObjorList = (text) => {
  let obj = [];
  let tmparray = Array.from(text);
  if (tmparray[0] == '[') {
    text = text.substr(1, text.length - 2);
    let tmp = text.split(/,(?![^{]*})/);
    for (let i = 0; i < tmp.length; i++){
      obj.push(JSON.parse(tmp[i]))
    }
  }
  else if (tmparray[0] == '{') {
    obj = JSON.parse(text)
  }
  else {
    obj = text.split(/\n/);
  }
  return obj;
}

if (process.argv[1].match(/readDataFromFile/)) {
  (async () => {
    let filePath = './sdf-test.dat';
    let result1 = await readFileEx(filePath);
    console.log('暗号化済みtext');
    console.log(result1);

    let dectxt = await decrypto(result1);
    // アクセステスト
    console.log('復号text');
    for (let i = 0; i < dectxt.length; i++){
      console.log(dectxt[i])
    }
    console.log('profの[Array]にアクセスするテスト')
    console.log(dectxt[0]['prof'])
    fs.writeFileSync('dec-by-node.dat', JSON.stringify(dectxt))

    //エンコードテスト
    console.log('暗号化テスト(これでいいのか知らん)\nt2pecf==')
    let enctxr = 't2pecf==';
    let keytxt = ['prof','student','lecture','attend']
    let keyword = ['prof===', '.student', '.lecture', '.attend='];
    for (let j = 0; j < dectxt.length; j++) {
      console.log(JSON.stringify(dectxt[j][keytxt[j]]))
      let enc = (await AES256CBC.AES256CBC.encode(JSON.stringify(dectxt[j][keytxt[j]])))
      console.log(keyword[j] + '\n' + enc['key'] + '\n' + enc['iv'] + '\n' + enc['body'])
      enctxr += keyword[j] + enc['key'].replace('=','') + enc['iv'].replace('==','') + enc['body']
    }
    fs.writeFileSync('enc-by-node.dat', enctxr);
  })();
}

/**
 * read filedata
 * @param {strihng} filepath 
 */
exports.read = (filepath)=>{
  return JSON.parse(fs.readFileSync(filepath, 'utf-8'));
}
/**
 * write filedata
 * @param {string} filepath 
 * @param {object} data 
 */
exports.write = (filepath, data)=>{
  fs.writeFileSync(filepath, JSON.stringify(data));
};
