# 学生リスト.csvから
#
'''
    入力：
    出力：
'''

from types import LambdaType
import datetime
import csv

time = datetime.datetime.now()
print(time)
#time ="06/02 15:15"
#start_time =datetime.datetime(2021,6,2,16,00)
#end_time =datetime.datetime(2021,6,2,19,00)
#late_time=datetime.datetime(2021,6,2,18,00)

#テスト実行用？？
idm=str('a012')
#students=('b012')

# 元の実装
def comp(idm:str,students,lect_time):
    with open('学生リスト.csv',newline='') as f:
        reader=csv.DictReader(f)
        for row in reader:
            if idm!=row['IDm']:
                print('履修者ではありません')
            number=(row['学籍番号'])
    return number

# 元を改変したtsr的実装
def comparsion(idm,students):
    for i in range(len(students)):
        if idm != students['IDm']:
            print('履修者ではありません')
            pass
        number = students['学籍番号']
    return number