
const crypto = require('crypto');

const BLOCK_SIZE = 32;
const key = crypto.scryptSync('', crypto.randomBytes(32), 32);
const iv = crypto.randomBytes(16);
const plaintext = '{"list":[0,2,4,6,8,10],"obj":{"value":11,"str":"bbbaddd"},"str":"b%20is%20bad","value":1011}';

console.log('original: ' + plaintext + ' (' + plaintext.length + ')');
console.log('key: ' + key.toString('base64') + ' (' + (key.toString('base64')).length + ')');
console.log('iv: ' + iv.toString('base64') + ' (' + (iv.toString('base64')).length + ')');

const cipher = crypto.createCipheriv('aes-256-cbc', key, iv);
let encoded = cipher.update(plaintext, 'utf-8', 'base64');
encoded += cipher.final('base64');

console.log('encoded: ' + encoded + ' (' + encoded.length + ')');

const decipher = crypto.createDecipheriv('aes-256-cbc', key, iv);
let decoded = decipher.update(encoded, 'base64', 'utf-8');
decoded += decipher.final('utf-8');

console.log('decode: ' + decoded + ' (' + decoded.length + ')');
