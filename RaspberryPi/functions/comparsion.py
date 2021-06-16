#学生リスト.csvから
#


from types import LambdaType
import datetime
import csv
#def comp(idm:str,students,lect_time):
    
time = datetime.datetime.now()
print(time)
#time ="06/02 15:15"
start_time =datetime.datetime(2021,6,2,16,00)
end_time =datetime.datetime(2021,6,2,19,00)
late_time=datetime.datetime(2021,6,2,18,00)

idm=str('a012')
#students=('b012')

with open('学生リスト.csv',newline='') as f:
    reader=csv.DictReader(f)
    for row in reader:
        if idm!=row['IDm']:
            print('履修者ではありません')
        number=(row['学籍番号'])
return number
        

