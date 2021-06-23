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



# -- NFCread function -- #
def NFCread():
    while(True): 
        #idm = cardreader()
        #result = comp(idm students, lect_time)
         #comp(idm:str, students:[str], lect_time:{start:datetime,end:datetime,late:datetime})
        # monitor
         #datawrite()
        time.sleep(1)

        define.nfcdata = str(cardreader.printidm()) # nfcのIDです str(i)を読み取ったIDｍに変更してください
        define.studentname = str(-1 * i) # 上記IDに対応する生徒の名前です str(-1 * 1)を生徒名に変更してください
        


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