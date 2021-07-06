import binascii
import nfc
from time import time
import sys
# from types import LambdaType#時間のインポート
import datetime#時間のインポート

# -- global --
idm= ""

# idmを取得して格納する関数
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

# idmを返す関数？？？
def printidm():
    read_id()
    now= datetime.datetime.now()
    return idm#,now

# 2回目の入室者に警告を出す
'''
    入力：
        studentData：出席した学生のデータ(学籍番号だけでも動くかな？)
    戻り値：
        2回目の人が居たとき -> False
        それ以外 -> True
'''
def second_warn(studentData:list):
    import comparsion
    comparsion.comp()
    dataLength = len(studentData)
    new_attender=studentData[dataLength]['学籍番号']
    for i in range(dataLength-1):
        if new_attender==studentData[i]['学籍番号']:
            studentData.pop(i)
            return False
    return True




if __name__ == '__main__':
    print(printidm())
