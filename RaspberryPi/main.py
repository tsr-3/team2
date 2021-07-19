# -*- coding: utf-8 -*-
# --- RaspberryPi main script --- #

from functions.comparsion import comp
from functions.SaveDataFile import SaveDataFile_noCipher as SaveDataFile
from functions.second_warn import second_warn
# from RaspberryPi.functions.SaveDataFile import SaveDataFile
import datetime
import dateutil.parser
import threading
import concurrent.futures
import time

#GUI表示に必要なもの
import sys
from PyQt5.QtWidgets import *

from functions import windowsv3 #./functions/windowsv3 をimportしている
from functions import ValueStorage # windowsv3と値をやり取りするための苦渋の策
# from functions import cardreader
from functions import dummy_cardreader as cardreader # 上記cardreader の手動入力版 # debug
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
        ValueStorage.nfcdata = str(idm) # nfcのIDをwindowsv3.pyへ渡す
        tmp = comparsion.comp(idm, data) # IDmから生徒名を検索
        ValueStorage.studentname = tmp[0] # IDに対応する生徒の名前をwindowsv3.pyへ渡す
        # タッチした時刻と登録された時刻の比較を行いwindowsv3.pyへ渡す(出席/遅刻/欠席/非履修者)

        check = time_attend.time(t1, t2, t3)

        if tmp[2]:
            if check == "出席":
                ValueStorage.attendcheck[1] = 0
            elif check == "遅刻":
                ValueStorage.attendcheck[1] = 1
            elif check == "欠席":
                ValueStorage.attendcheck[1] = 2
            ValueStorage.attendcheck[0] = check
        else:
            ValueStorage.attendcheck[0] = "非履修者"
            ValueStorage.attendcheck[1] = 3


# -- main loop -- #

STATE_BEFORE_START:int = 1
STATE_ACCEPTING:int = 2
STATE_END_ACCEPT:int = 3

flag_doMainLoop:bool = True

def mainProcess():
    ValueStorage.process_state = STATE_BEFORE_START
    students:list = None
    professors:list = None
    lecture:dict = None
    attendance_dat:list = []
    accept_start:datetime = None
    while(True):
        # sleep
        time.sleep(0.1)

        if not flag_doMainLoop:
            break
        if ValueStorage.process_state == STATE_BEFORE_START:
            if ValueStorage.filepath is None:
                continue
            try:
                dat = SaveDataFile.read(ValueStorage.filepath)
            except BaseException as err:
                print(err)
                raise err
            if students == None:
                students = dat['students']
                ValueStorage.isFiledataExist['students'] = True
            if professors == None:
                professors = dat['professors']
                ValueStorage.isFiledataExist['professors'] = True
            if lecture == None:
                lecture = dat['lecture']
                ValueStorage.isFiledataExist['lecture'] = True
            ValueStorage.filepath = None
        elif ValueStorage.process_state == STATE_ACCEPTING:
            idm, now = cardreader.printidm()
            if second_warn(idm, attendance_dat):
                continue # already accepting
            # check if this student is enrolled in lecture
            if not comparsion.comp(idm, lecture.students)[2]:
                continue # isnot in student who enrolled in lecture
            # set to global for idm and time to accept
            # add accept(attendance) data
            attendance_dat.append({'time': now, 'id': students.find({'idm': idm})})
        elif ValueStorage.process_state == STATE_END_ACCEPT:
            pass

# -- onexec -- #
if __name__ == '__main__':

    #スレッド作成
    executor = concurrent.futures.ThreadPoolExecutor(max_workers=2)
    # 繰り返し行う処理
    executor.submit(mainProcess)

    # GUI処理(mainに無いと警告が出る)
    app=QApplication(sys.argv)
    win = windowsv3.WinMake(app)

    print(ValueStorage.nfcdata)
