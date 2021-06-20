// hash

const crypto = require('crypto');

exports.hash = class{
  static sha256(text){
    if(typeof(text) !== 'string') return null;
    return crypto.createHash('sha256').update(text).digest('hex');
    // 64 chars
  }
  static sha384(text){
    if(typeof(text) !== 'string') return null;
    return crypto.createHash('sha384').update(text).digest('hex');
    // 96 chars
  }
  static sha512(text){
    if(typeof(text) !== 'string') return null;
    return crypto.createHash('sha512').update(text).digest('hex');
    // 128 chars
  }
};

