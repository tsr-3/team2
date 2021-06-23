import binascii
# import nfc
from time import time
import sys
# from types import LambdaType#時間のインポート
import datetime#時間のインポート

# -- global --
idm= ""


def on_connect(tag):
    print("touched")
    global idm
    idm = binascii.hexlify(tag.idm)
    return True

def read_id():
    clf = nfc.ContactlessFrontend('usb')
    try:
        clf.connect(rdwr={'on-connect': on_connect})
    finally:
        clf.close()


def printidm():
    read_id()
    now= datetime.datetime.now()
    return idm,now


if __name__ == '__main__':
    print(printidm())


