import random
import string
import base64

from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

# key = ''.join([random.choice(string.ascii_letters + string.digits) for i in range(50)])
key = get_random_bytes(16)

cipher = AES.new(key, AES.MODE_EAX)
target = 'B IS VERY BAD'

encrypted, tag = cipher.encrypt_and_digest(target.encode('utf-8'))

print(encrypted)
print(tag)
print(base64.b64encode(encrypted))


# ref: https://dev.classmethod.jp/articles/python-crypto-libraries/