'''
製作者:B21P036
NFCが無い環境でもデバック作業が行えるように,IDmを標準入力によって入力するプログラム

on_connect():IDmを標準入力として取得する
GOon_connect

read_id():互換性の為に経由するする
GOread_id

printidm():IDmを返す (PrintなんだからPrintしろ)
GOprintidm

'''
import binascii
from time import time
import sys
# from types import LambdaType#時間のインポート
import datetime#時間のインポート

# -- global --
idm= ""

#GOon_connect
def on_connect():
    print("touched")
    global idm
    idm = input("Your ID:")
    return True

#GOread_id
def read_id():
    on_connect()


#GOprintidm
def printidm():
    read_id()
    now= datetime.datetime.now()
    return idm,now


if __name__ == '__main__':
    print(printidm())


