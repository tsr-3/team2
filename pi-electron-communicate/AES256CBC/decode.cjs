
const {AES256CBC} = require('./AES256CBC.cjs');
const fs = require('fs');

let cryptogram = fs.readFileSync('cryptogram.txt', 'utf-8');
const [key, iv, body] = cryptogram.split('\n');

fs.writeFileSync("decryptogram.json", AES256CBC.decode(key, iv, body));
