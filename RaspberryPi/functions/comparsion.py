'''
入力：studentID
出力：studentName
説明：学籍番号が入力されたらそれに対応する学生の氏名を返す関数
'''

from types import LambdaType

import json

def comp(studentID,studentName)
    json_open=open('学生リスト.json','r')
    json_load=json.load(json_open)
    studentID=[S001,S002,...,S100]
    for v in json.load.values():
        if studentID==v['学籍番号']:
            studentName=v['名前']
            return studentName