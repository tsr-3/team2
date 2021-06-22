
const crypto = require('crypto');

const BLOCK_SIZE = 32;
const key = 'ztqO594gkEGu3Gdqg6i2GSZQIiv3hU0z'; // 32byte = 256bit AES256
const text = 'b is bad';

console.log('key length: ' + key.length + ', block size: ' + BLOCK_SIZE);

const cipher = crypto.createCipher('aes-256-ecb', key);
let ciphered = cipher.update(text, 'utf8', 'hex');
ciphered += cipher.final('hex');

console.log('encrypted: ' + ciphered);

const decipher = crypto.createDecipher('aes-256-ecb', key);
let deciphered = decipher.update(ciphered, 'hex', 'utf8');
deciphered += decipher.final('utf8');

console.log('decrypted: ' + deciphered);
