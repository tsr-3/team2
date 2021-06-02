# ----- SaveDataFile ----- #
# written by AdmHatena(https://github.com/AdmHatena/)
# version 3.9.0 64-bit

import AESCipher

class SaveDataFile:
    def read(path:str):
        with open(path, 'r', 1, 'utf-8') as fp:
            encoded = fp.read()
        pass
    def write(dat:object, path:str):
        pass