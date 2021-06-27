import binascii
from time import time
import sys
# from types import LambdaType#時間のインポート
import datetime#時間のインポート

# -- global --
idm= ""


def on_connect():
    print("touched")
    global idm
    idm = input("Your ID:")
    return True

def read_id():
    on_connect()


def printidm():
    read_id()
    now= datetime.datetime.now()
    return idm,now


if __name__ == '__main__':
    print(printidm())


