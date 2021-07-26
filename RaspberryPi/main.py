# -*- coding: utf-8 -*-
# --- RaspberryPi main script --- #

from typing import ValuesView
from functions.comparsion import comp
from functions.SaveDataFile import SaveDataFile_noCipher as SaveDataFile
from functions.second_warn import second_warn
from dataclass.Professors import Professors
from dataclass.students import Students
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
    accept_start:datetime = None
    while(True):
        # sleep
        time.sleep(0.1)

        if ValueStorage.process_state == STATE_BEFORE_START:
            if ValueStorage.filepath is None:
                continue
            try:
                dat = SaveDataFile.read(ValueStorage.filepath)
            except BaseException as err:
                print(err)
                raise err
            if dat == None:
                ValueStorage.filepath = None
                continue
            try:
                if 'students' in dat:
                    students = Students(dat['students']) # throw error here (invalid data type)
                    ValueStorage.isFiledataExist['students'] = True
                else:
                    ValueStorage.isFiledataExist['students'] = False
                if 'professors' in dat:
                    professors = Professors(dat['professors'])
                    ValueStorage.isFiledataExist['professors'] = True
                else:
                    ValueStorage.isFiledataExist['students'] = False
                if 'lecture' in dat:
                    lecture = dat['lecture']
                    ValueStorage.lectID = lecture['id']
                    ValueStorage.isFiledataExist['lecture'] = True
                else:
                    ValueStorage.isFiledataExist['students'] = False
                ValueStorage.filepath = None
                ValueStorage.late_time =  lecture['late']
                ValueStorage.abcent_time =  lecture['limit']
            except BaseException as e:
                #print(e)
                ValueStorage.filepath = None
                #raise e

        elif ValueStorage.process_state == STATE_ACCEPTING:
            idm, now = cardreader.printidm()
            if second_warn(idm, ValueStorage.attendance):
                continue # already accepting
            try:
                dat = students.find({'idm': idm})
                if(len(dat) == 0):
                    # is not defined
                    ValueStorage.nfcdata = idm
                    ValueStorage.studentname = '--undefined--'
                    ValueStorage.attendcheck[0] = '本校の生徒ではありません'
                    continue
                STUDENT = dat[0]
                print(STUDENT)
            except BaseException as e:
                print(e)
                raise e
            # check if this student is enrolled in lecture
            if not comparsion.comp(STUDENT['id'], lecture['students']):
                ValueStorage.nfcdata = idm
                ValueStorage.studentname = STUDENT['name']
                ValueStorage.attendcheck[0] = '非履修者です'
                continue # isnot in student who enrolled in lecture
            # show data
            ValueStorage.nfcdata = idm
            ValueStorage.studentname = STUDENT['name']
            ValueStorage.attendcheck[0], ValueStorage.attendcheck[1] = time_attend.timecheck(now, {'start': ValueStorage.now_time, 'limit': lecture['limit'], 'late':lecture['late']})

            # add accept(attendance) data
            ValueStorage.attendance.append({'time': now, 'id': STUDENT['id']})
        elif ValueStorage.process_state == STATE_END_ACCEPT:
            return None

# -- onexec -- #
if __name__ == '__main__':

    #スレッド作成
    ValueStorage.thread = executor = concurrent.futures.ThreadPoolExecutor(max_workers=2)
    # 繰り返し行う処理
    executor.submit(mainProcess)

    # GUI処理(mainに無いと警告が出る)
    app=QApplication(sys.argv)
    win = windowsv3.WinMake(app)

    print(ValueStorage.nfcdata)
