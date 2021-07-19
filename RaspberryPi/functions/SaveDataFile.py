# coding: utf-8
# ----- SaveDataFile ----- #
# version 3.9.0 64-bit

import json

##Main.pyからSaveDataFile.py をimport するためのおまじない
import os
import sys
os.chdir(os.path.dirname(os.path.abspath(__file__)))
p = os.path.abspath('..')
sys.path.insert(1, p)
from functions.AES256CBC import AES256CBC
from dataclass.Professors import Professors
from dataclass.students import Students

# savedata
# filetype + Base64(AES256CBC(data-container-s))
# | str"t2pecf=="(8-byte) | data-containers(variable-byte)
# data-containers
# | type(7-byte) | key(43-byte) | iv(22-byte) | body(variable-byte) |
# 各コンテナは.でつなぐ
# key
# AES256CBC => 44byte data => remove one padding(=) => 43byte data
# iv
# AES256CBC => 24byte data => remove two padding(=) => 22byte data
# type
# - .prof=== : professors data
# - .student : students data
# - .lecture : lecture data
# - .attend= : attendance data

class SaveDataFile:
    # SaveDataFile.read(filepath)
    # return : {'proffesors': list, 'students' : list. 'lecture': dict, 'attendance': list}
    @staticmethod
    def read(path: str):
        # read file
        try:
            fp = open(path, mode = 'r', encoding = 'utf-8')
        except:
            return None
        encoded:str = fp.read()
        # close
        fp.close()
        # check file type
        if encoded[0:8] != 't2pecf==': # Team2 raspberryPi - Electron Communication File
            return None
        DATA = {}
        for container in encoded[8:].split('.'):
            if container[0:7] == 'prof===':
                # professors
                plain = AES256CBC.decode(container[7:50] + '=', container[50:72] + '==', container[72:])
                # DATA['professors'] = json.loads(plain)
                DATA['professors'] = Professors(json.loads(plain))
            if container[0:7] == 'student':
                # students
                plain = AES256CBC.decode(container[7:50] + '=', container[50:72] + '==', container[72:])
                # DATA['students'] = json.loads(plain)
                DATA['students'] = Students(json.loads(plain))
            if container[0:7] == 'lecture':
                # lecture data
                plain = AES256CBC.decode(container[7:50] + '=', container[50:72] + '==', container[72:])
                DATA['lecture'] = json.loads(plain)
            if container[0:7] == 'attend=':
                # attendances
                plain = AES256CBC.decode(container[7:50] + '=', container[50:72] + '==', container[72:])
                DATA['attendances'] = plain.split('\n')
        return DATA
    
    @staticmethod
    def write(dat:object, path:str):
        container: list = []
        if 'professors' in dat:
            cipher = AES256CBC.encode(json.dumps(dat['professors']))
            container.append('prof===' + cipher['key'].replace('=','') + cipher['iv'].replace('=','') + cipher['body'])
        if 'students' in dat:
            cipher = AES256CBC.encode(json.dumps(dat['students']))
            container.append('student' + cipher['key'].replace('=','') + cipher['iv'].replace('=','') + cipher['body'])
        if 'lecture' in dat:
            cipher = AES256CBC.encode(json.dumps(dat['lecture']))
            container.append('lecture' + cipher['key'].replace('=','') + cipher['iv'].replace('=','') + cipher['body'])
        if 'attendances' in dat:
            cipher = AES256CBC.encode('\n'.join(dat['attendances']))
            container.append('attend=' + cipher['key'].replace('=','') + cipher['iv'].replace('=','') + cipher['body'])
        try:
            fp = open(path, mode = 'w', encoding = 'utf-8')
        except:
            return False
        fp.write('t2pecf==' + '.'.join(container))
        fp.close()
        return True

class SaveDataFile_noCipher:
    @staticmethod
    def read(path:str):
        try:
            with open(path, encoding = 'utf-8', mode = 'r') as fp:
                return json.loads(fp.read())
        except BaseException as e:
            print('[SaveDataFile_noCipher]', e)
            return None
    @staticmethod
    def write(dat:dict, path:str):
        try:
            fp = open(path, encoding = 'utf-8', mode = 'w')
            fp.write(json.dumps(dat))
            fp.close()
        except BaseException as e:
            print('[SaveDataFile_noCipher]', e)
            return None

if __name__ == '__main__':
    data = {}
    data['professors'] = [{'name':'b', 'lect':['BrainFuck', 'JavaScript', 'PHP']}, {'name':'hrm', 'lect':['c#', 'vim', 'Python']}, {'name':'hatena', 'lect':[]}]
    data['students'] = [{'name':'aym', 'id':'ayumu'}, {'name':'hst', 'id':'daigakusei'},{'name':'tnhs', 'id':'nihachi16'}]
    data['lecture'] = {'name':'Brainfuck', 'id':'bf', 'start':'18:00', 'late':'30', 'students':['ayumu','daigakusei','nihachi16']}
    data['attendances'] = ['ayumu 2021-07-17 16:28:18', 'daigakusei 2021-07-17 16:29:55', 'nihachi16 2021-07-17 16:30:07']
    # SaveDataFile.write(data, './test/t2pecf/sdf-test.dat')
    dat = SaveDataFile.read('./test/t2pecf/sdf-test.dat')
    if 'professors' in dat:
        print(dat['professors'])
    if 'students' in dat:
        print(dat['students'])
    if 'lecture' in dat:
        print(dat['lecture'])
    if 'attendance' in dat:
        print(dat['attendances'])
