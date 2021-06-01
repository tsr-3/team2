# ref: https://udemyfun.com/python-crypt-decrypt-file/

import string
import random

from Crypto.Cipher import AES


key = ''.join(
    random.choice(string.ascii_letters) for _ in range(AES.block_size)
)

iv = ''.join(
    random.choice(string.ascii_letters) for _ in range(AES.block_size)
)

with open('plaintext', 'r') as f, open('encode.dat', 'wb'), as e:
    plaintext = f.read() 
    cipher = AES.new(key, AES.MODE_CBC, iv)
    padding_length = AES.block_size - len(plaintext) % AES.block_size
    plaintext += chr(padding_length) * padding_length
    cipher_text = cipher.encrypt(plaintext)
    e.write(cipher_text)]

##### 動くとは言っていない