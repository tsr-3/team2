// cipher

const crypto = require('crypto');

class AES256ECB{
  static encode(text){
    if(typeof(text) !== 'string') return null;
    const response = {body:''};
    response.key = AES256ECB.random_string(32);
    for(let txt of AES256ECB.split(text, 32)){
      console.log(txt);
      let cipher = crypto.createCipher('aes-256-ecb', response.key);
      cipher.update(txt, 'utf8', 'hex');
      let tmp = cipher.final('hex');
      response.body += tmp;
      console.log(tmp);
    }
    // cipher.update(text, 'utf8', 'hex');
    // response.body = cipher.final('hex');
    return response;
  }
  static decode(key, text){
    if(typeof(text) !== 'string' || typeof(key) !== 'string') return null;
    let decipher, response = '';
    for(let txt of AES256ECB.split(text, 32)){
      console.log(txt);
      decipher = crypto.createDecipher('aes-256-ecb', key);
      decipher.update(txt, 'hex', 'utf8');
      response += decipher.final('utf8');
    }
    // decipher.update(text, 'hex', 'utf8');
    // return decipher.final('utf8');
    return response;
  }
  static random_string(length){
    if(typeof(length) !== 'number') return null;
    const CHARACTER_LIST = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789';
    let text = '';
    const buf = crypto.randomBytes(length);
    for(let num of buf)
      text += CHARACTER_LIST[num % CHARACTER_LIST.length];
    return text;
  }
  static split(text, length){
    if(typeof(text) !== 'string' || typeof(length) !== 'number') return null;
    const arr = [];
    while(text.length > length){
      arr.push(text.substr(0, length));
      text = text.substr(length);
    }
    arr.push(text);
    return arr;
  }
};

exports.AES256ECB = AES256ECB;

// debug
if(process.argv[1].match(/Cipher\.cjs/)){
  const encoded = AES256ECB.encode('i think b is very bad, but b does not think b is bad because he think b is god');
  console.log('key : ' + encoded.key);
  console.log('body: ' + encoded.body);
  const decoded = AES256ECB.decode(encoded.key, encoded.body);
  console.log(decoded);
}
