# AES Cipher
# written by AdmHatena (https://github.com/AdmHatena/)
# version Python 3.9.0 64-bit

# need `npm install pycryptodome`

import base64
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

class AESCipher:
    # enc(target:str)
    # - target:str - エンコードするデータ
    # return - encoded, key, tag, nonce
    # - encoded:str - base64変換されたエンコード済みのデータ
    # - key:str - base64変換されたエンコードに利用したキー
    # - tag:str - base64変換されたエンコードに利用したタグ
    # - nonce:str - base64変換されたエンコードで生成されたnonce
    def enc(target:str):
        result = {}
        key = get_random_bytes(16)
        cipher = AES.new(key, AES.MODE_EAX)
        encoded, tag = cipher.encrypt_and_digest(target.encode('utf-8'))
        result.encoded = base64.b64encode(encoded)
        result.key = base64.b64encode(key)
        result.tag = base64.b64encode(tag)
        result.nonce = base64.b64encode(nonce)
        
        return result
    
    # dec(target:str, key:str, tag:str, nonce:str)
    # - target:str - デコードするデータ(base64)
    # - key:str - デコードに利用するキー(base64)
    # - tag:str - デコードに利用するタグ(base64)
    # - nonce:str - デコードに利用するnonce(base64)
    # return - decoded
    # - decoded:str - デコードされたデータ
    def dec(target:str, key:str, tag:str, nonce:str):
        cipher = AES.new(base64.b64decode(key), AES.MODE_EAX, base64.b64decode(nonce))
        data = cipher.decrypt_and_verify(base64.b64decode(target), base64.b64decode(tag))
        return data

if __name__ == '__main__':
    encoded, key, tag, nonce = AESCipher.enc('B IS VERY BAD')
    decoded = AESCipher.dec(encoded, key, tag, nonce)
    print(encoded)
    print(decoded)

# ref: https://pycryptodome.readthedocs.io/en/latest/src/examples.html#encrypt-data-with-aes