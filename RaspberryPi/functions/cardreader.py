import binascii
import nfc
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
    return idm#,now

def second_warm():
    import comparsion
    comparsion.comp()
    if studentData[i]['学籍番号']==students_list[i]['学籍番号']:
        enter_warnigtext="すでに入室済みです"
        return enter_warnigtext


    


if __name__ == '__main__':
    print(printidm())


