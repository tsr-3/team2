
const {AES256CBC} = require('./AES256CBC.cjs');
const fs = require('fs');


async function main(){
  let cryptogram = fs.readFileSync('cryptogram.txt', 'utf-8');
  const [key, iv, body] = cryptogram.split('\n');
  
  fs.writeFileSync("decryptogram.json", await AES256CBC.decode(key, iv, body));
}

main();
