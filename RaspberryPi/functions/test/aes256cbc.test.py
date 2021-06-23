
import base64
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad

BLOCK_SIZE = 32

key = get_random_bytes(32) # 32byte/256bit
iv = get_random_bytes(16) # 16byte/128bit
plaintext = 'i think b is very bad, but b does not think b is bad because he think b is god'

print('key: ' + key.hex() + ' (' + str(len(key)) + ')')
print('iv: ' + iv.hex() + ' (' + str(len(iv)) + ')')
print('blocksize: ' + str(BLOCK_SIZE))

cipher = AES.new(key, AES.MODE_CBC, iv)
encoded = cipher.encrypt(pad(plaintext.encode('utf-8'), BLOCK_SIZE))
enc_txt = (base64.b64encode(encoded)).decode('utf-8')

print("encoded: " + enc_txt)

ciphered = base64.b64decode(enc_txt.encode('utf-8'))

decipher = AES.new(key, AES.MODE_CBC, iv)
decoded = decipher.decrypt(ciphered)
dec_txt = unpad(decoded, BLOCK_SIZE).decode('utf-8')

print('decoded: ' + dec_txt)
