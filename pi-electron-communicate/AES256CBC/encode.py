# load plain text and encrypt

from AES256CBC import AES256CBC

cryptogram_text = ''
with open("plaintext.json", "r", encoding="utf-8") as fp:
    json = fp.read()
    cryptogram = AES256CBC.encode(json)
    cryptogram_text += cryptogram['key'] + '\n' + cryptogram['iv'] + '\n' + cryptogram['body']
    fp.close()
with open("cryptogram.txt", "w", encoding='utf-8') as fp:
    fp.write(cryptogram_text)
    fp.close()
