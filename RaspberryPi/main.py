# -*- coding: utf-8 -*-
# --- RaspberryPi main script --- #

from RaspberryPi.functions.comparsion import comp
from RaspberryPi.functions.SaveDataFile import DummySaveDataFile as SaveDataFile # debug
# from RaspberryPi.functions.SaveDataFile import SaveDataFile
import datetime
import dateutil.parser
import threading
import concurrent.futures
import time

#GUI表示に必要なもの
import sys
from PyQt5.QtWidgets import *
from gui import windowsv3 #./gui/windowsv3 をimportしている
from functions import define # windowsv3と値をやり取りするための苦渋の策
# from functions import cardreader
from functions import dummy_cardreader as cardreader # 上記cardreader の手動入力版(35行目も記載)
from functions import time_attend # 出席を判定するもの
from functions import comparsion # IDｍと生徒情報を紐づける

from types import LambdaType

t1 = datetime.datetime(2021, 6, 2, 16, 00)
t2 = datetime.datetime(2021, 6, 2, 17, 00)
t3 = datetime.datetime(2023, 6, 2, 18, 00)

# -- NFCread function -- #
def NFCread():

    data = [{"学籍番号":"S001","名前":"相道森","IDm":"012E44A7A5187429"}] # テスト用データ

    i = 0
    while(True):
        i += 1
        time.sleep(1)

        # idm, now = cardreader.printidm() #カードリーダによる読み取り
        idm, now = cardreader.printidm() #手動ID入力
        define.nfcdata = str(idm) # nfcのIDをwindowsv3.pyへ渡す
        tmp = comparsion.comp(idm, data) # IDmから生徒名を検索
        define.studentname = tmp[0] # IDに対応する生徒の名前をwindowsv3.pyへ渡す
        # タッチした時刻と登録された時刻の比較を行いwindowsv3.pyへ渡す(出席/遅刻/欠席/非履修者)

        check = time_attend.time(t1, t2, t3)

        if tmp[2]:
            if check == "出席":
                define.attendcheck[1] = 0
            elif check == "遅刻":
                define.attendcheck[1] = 1
            elif check == "欠席":
                define.attendcheck[1] = 2
            define.attendcheck[0] = check
        else:
            define.attendcheck[0] = "非履修者"
            define.attendcheck[1] = 3


# -- main loop -- #

STATE_BEFORE_START:int = 1
STATE_ACCEPTING:int = 2
STATE_END_ACCEPT:int = 3

def mainProcess():
    state:int = STATE_BEFORE_START
    students:list
    professors:list
    lecture:dict
    while(True):
        if state == STATE_BEFORE_START:
            if students == None or professors == None or lecture == None:
                dat = SaveDataFile.read()
            if students == None:
                students = dat['students']
            if professors == None:
                professors = dat['professors']
            if lecture == None:
                lecture = dat['lecture']
        elif state == STATE_ACCEPTING:
            idm, now = cardreader.printidm()
            # check if this student is enrolled in lecture
            if comparsion.comp(idm, lecture.students):
                pass
            else:
                pass
        elif state == STATE_END_ACCEPT:
            pass

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
