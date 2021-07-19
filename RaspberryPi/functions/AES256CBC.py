
import base64
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad

class AES256CBC:
    def encode(text:str):
        BLOCK_SIZE = 32
        key = get_random_bytes(32)
        iv = get_random_bytes(16)
        body = (base64.b64encode((AES.new(key, AES.MODE_CBC, iv)).encrypt(pad(text.encode('utf-8'), BLOCK_SIZE)))).decode('utf-8')
        key = (base64.b64encode(key)).decode('utf-8')
        iv = (base64.b64encode(iv)).decode('utf-8')
        return {'key': key, 'iv': iv, 'body': body}
    def decode(key:str, iv:str, text:str):
        try:
            BLOCK_SIZE = 32
            key = base64.b64decode(key.encode('utf-8'))
            iv = base64.b64decode(iv.encode('utf-8'))
            return unpad((AES.new(key, AES.MODE_CBC, iv)).decrypt(base64.b64decode(text.encode('utf-8'))), BLOCK_SIZE).decode('utf-8')
        except BaseException as err:
            print('aes256cbc.decode', err)
            raise err


if __name__ == '__main__':
    plaintext = '{"list":[0,2,4,6,8,10],"obj":{"value":11,"str":"bbbaddd"},"str":"b is bad","value":1011}'
    print('origin: ' + plaintext)
    encoded = AES256CBC.encode(plaintext)
    print('key: ' + encoded['key'] + ' (' + str(len(encoded['key'])) + ')')
    print('iv: ' + encoded['iv'] + ' (' + str(len(encoded['iv'])) + ')')
    print('encoded: ' + encoded['body'])
    decoded = AES256CBC.decode(encoded['key'], encoded['iv'], encoded['body'])
    print('decoded: ' + decoded)
