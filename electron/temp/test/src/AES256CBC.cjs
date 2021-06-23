
const crypto = require('crypto');

exports.AES256CBC = class{
  static encode(plaintext){
    if(typeof(plaintext) !== 'string') return null;
    const key = crypto.scryptSync('', crypto.randomBytes(32), 32);
    const iv = crypto.randomBytes(16);
    const cipher = crypto.createCipheriv('aes-256-cbc', key, iv);
    let decoded = cipher.update(plaintext, 'utf-8', 'base64');
    return {body: decoded + cipher.final('base64'), key: key.toString('base64'), iv: iv.toString('base64')};
  }
  static decode(key, iv, text){
    if(typeof(key) !== 'string' || typeof(iv) !== 'string' || typeof(text) !== 'string') return null;
    key = Buffer.from(key, 'base64');
    iv = Buffer.from(iv, 'base64');
    const decipher = crypto.createDecipheriv(text, key, iv);
    let decode = decipher.update(text, 'base64', 'utf-8');
    decode += decipher.final('utf-8');
    return decode;
  }
};


if(process.argv[1].match(/AES256CBC.cjs/)){
  // debug
  const plaintext = '{"list":[0,2,4,6,8,10],"obj":{"value":11,"str":"bbbaddd"},"str":"b%20is%20bad","value":1011}';
  console.log('origin: ' + plaintext);
  const encoded = this.AES256CBC.encode(plaintext);
  console.log(encoded);
  const decoded = this.AES256CBC.decode(encoded.key, encoded.iv, encoded.body);
  console.log(decoded);
}
