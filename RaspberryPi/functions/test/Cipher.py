
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad

class AES256ECB:
    def encode(text:str):
        BLOCK_SIZE = 32
        response = {}
        response['key'] = AES256ECB.random_string(32) # 32byte = 256bit AES256
        cipher = AES.new(response['key'].encode('utf-8'), AES.MODE_ECB)
        response['body'] = cipher.encrypt(pad(text.encode('utf-8'), BLOCK_SIZE)).hex()
        return response
    def decode(key:str, text:str):
        BLOCK_SIZE = 32
        decipher = AES.new(key.encode('utf-8'), AES.MODE_ECB)
        return unpad(decipher.decrypt(bytearray.fromhex(text)), BLOCK_SIZE).decode('utf-8')
    def random_string(length:int):
        CHARACTER_LIST = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
        key = ''
        byte_array = get_random_bytes(length)
        for byte in byte_array:
            byte = int(byte)
            key += CHARACTER_LIST[byte % len(CHARACTER_LIST)]
        return key

if __name__ == '__main__':
    encoded = AES256ECB.encode('i think b is very bad, but b does not think b is bad because he think b is god')
    print('key : ' + encoded['key'])
    print('body: ' + encoded['body'])
    decoded = AES256ECB.decode(encoded['key'], encoded['body'])
    print(decoded)
