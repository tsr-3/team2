
const crypto = require('crypto');

exports.AES256CBC = class{
  static async encode(plaintext){
    const key = crypto.randomBytes(32), iv = crypto.randomBytes(16);
    const cipher = crypto.createCipheriv('aes-256-cbc', key, iv);
    let cryptogram = '';
    await new Promise((resolve, reject)=>{
      cipher.setEncoding('base64');
      cipher.on('data', chunk => cryptogram += chunk);
      cipher.on('end', ()=>resolve());
      cipher.write(plaintext);
      cipher.end();
    });
    return {body: cryptogram, key: key.toString('base64'), iv: iv.toString('base64')};
  }
  static async decode(key, iv, cryptogram){
    let plaintext = '';
    key = Buffer.from(key, 'base64');
    iv = Buffer.from(iv, 'base64');
    const decipher = crypto.createDecipheriv('aes-256-cbc', key, iv);
    decipher.setAutoPadding(false);
    await new Promise((resolve, reject)=>{
      decipher.on('readable', ()=>{
        let chunk;
        while(null !== (chunk = decipher.read()))
          plaintext += chunk.toString('utf-8');
      });
      decipher.on('end', ()=>resolve());
      decipher.write(cryptogram, 'base64');
      decipher.end();
    });
    return plaintext.replace(/\x14/g,'');
  }
};


if(process.argv[1] && process.argv[1].match(/AES256CBC.cjs/)){
  // debug
  (async ()=>{
    const plaintext = '{"list":[0,2,4,6,8,10],"obj":{"value":11,"str":"bbbaddd"},"str":"b%20is%20bad","value":1011}';
    console.log(plaintext);
    const encoded = await this.AES256CBC.encode(plaintext);
    console.log(encoded);
    const decoded = await this.AES256CBC.decode(encoded.key, encoded.iv, encoded.body);
    console.log(decoded);
  })();
}
