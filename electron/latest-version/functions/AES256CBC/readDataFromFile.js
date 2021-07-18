const fs = require('fs');
const { addListener } = require('process');
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
    let plaintext = (await AES256CBC.AES256CBC.decode(key, iv, body)).replace(/\x13|\x16|\r/g, '').trim();
    console.log(plaintext)
    let adddata = { [type]: plaintext };
    decryptotext.push(adddata);
  }
  return decryptotext;
}

if (process.argv[1].match(/readDataFromFile/)) {
  (async () => {
    let filePath = './sdf-test.dat';
    let result1 = await readFileEx(filePath);
    console.log('暗号化済みtext')
    console.log(result1);

    console.log('復号text');
    let dectxt = await decrypto(result1);
    console.log(dectxt);
  })();
}