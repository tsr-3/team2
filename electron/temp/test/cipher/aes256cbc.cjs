
const crypto = require('crypto');

async function main(){
  let encoded = await enc('{"color_list":["red","green","blue"],"num_list":[123,456,789],"mix_list":["red",456,null,true],"array_list":[[12,23],[34,45],[56,67]],"object_list":[{"name":"tanaka","age":26},{"name":"suzuki","age":32}]}');
  console.log(encoded);
  let decoded = await dec(encoded.key, encoded.iv, encoded.body);
  console.log(decoded);
}

/**
 * @param {string} plaintext 
 */
async function enc(plaintext){
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

/**
 * @param {string} key 
 * @param {string} iv 
 * @param {string} cryptogram 
 */
async function dec(key, iv, cryptogram){
  let plaintext = '';
  key = Buffer.from(key, 'base64');
  iv = Buffer.from(iv, 'base64');
  const decipher = crypto.createDecipheriv('aes-256-cbc', key, iv);
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
  return plaintext;
}

main();
