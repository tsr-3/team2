
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
  static decode(key, iv, plaintext){
    if(typeof(key) !== 'string' || typeof(iv) !== 'string' || typeof(plaintext) !== 'string') return null;
    //
  }
};
