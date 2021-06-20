
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
BLOCK_SIZE = 32

key = 'ztqO594gkEGu3Gdqg6i2GSZQIiv3hU0z'
text = 'b is bad'

print('key length: ' + str(len(key)) + ', block size: ' + str(BLOCK_SIZE))

cipher = AES.new(key.encode('utf8'), AES.MODE_ECB) # 32byte = 256bit AES256
encrypted = cipher.encrypt(pad(text.encode('utf8'), BLOCK_SIZE)) # string.encode('utf-8') => buffer(byte array)

enc_text = encrypted.hex() # byte array => string

print('encrypted: ' + enc_text)

decipher = AES.new(key.encode('utf8'), AES.MODE_ECB)
decrypted = decipher.decrypt(bytearray.fromhex(enc_text))

dec_text = unpad(decrypted, BLOCK_SIZE).decode('utf-8')

print('decrypted: ' + dec_text)
