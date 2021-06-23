# --- RaspberryPi main script --- #

import datetime
import dateutil.parser

#GUI表示に必要なもの
from gui import windowsv3 #./gui/windowsv3 をimportしている
import sys
from PyQt5.QtWidgets import *


import threading
import concurrent.futures
import time

# windowsv3と値をやり取りするための苦渋の策
from functions import define
from functions import cardreader
from functions import time_attend


t1 = datetime.datetime(2021, 6, 2, 16, 00)
t2 = datetime.datetime(2021, 6, 2, 17, 00)
t3 = datetime.datetime(2021, 6, 2, 18, 00)

# -- NFCread function -- #
def NFCread():
    i = 0
    while(True):
        i += 1
        #time.sleep(1)

        idm, now = cardreader.printidm()
        define.nfcdata = str(idm) # nfcのIDです
        define.studentname = str(-1 * i) # 上記IDに対応する生徒の名前です str(-1 * 1)を生徒名に変更してください

        # タッチした時刻と登録された時刻の比較を行い(出席/遅刻/欠席)
        define.attendcheck = time_attend.time(t1, t2, t3)



# -- onexec -- #
if __name__ == '__main__':


    #スレッド作成
    executor = concurrent.futures.ThreadPoolExecutor(max_workers=2)
    # 繰り返し行う処理
    executor.submit(NFCread)

    # GUI処理(mainに無いと警告が出る)
    app=QApplication(sys.argv)
    win = windowsv3.WinMake(app)

    print(define.nfcdata)
