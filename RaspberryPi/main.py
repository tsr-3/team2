# --- RaspberryPi main script --- #

import datetime
import dateutil.parser

#GUI表示に必要なもの
from gui import windowsv3   #./gui/windowsv3 をimportしている
import sys
from PyQt5.QtWidgets import *


import threading
import concurrent.futures
import time

# -- main function -- #
def main():
    # read save file
    for i in range(10):

        #idm = cardreader()
        #result = comp(idm students, lect_time)
         #comp(idm:str, students:[str], lect_time:{start:datetime,end:datetime,late:datetime})
        # monitor
         #datawrite()
        time.sleep(1)
        print("Done mainfunc")

# -- onexec -- #
if __name__ == '__main__':


    # スレッド(max_worker の数だけ同時処理が出来ます)
    executor = concurrent.futures.ThreadPoolExecutor(max_workers=2)
    # 繰り返し行う処理
    executor.submit(main)

    print("hello world")

    # GUIの起動
    app=QApplication(sys.argv)
    win = windowsv3.WinMake(app)


