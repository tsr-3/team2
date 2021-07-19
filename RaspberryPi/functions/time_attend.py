from abc import ABC
from types import LambdaType
import datetime
import dateutil.parser

#入力(start_time,late_time,end_time):
#入力（出席の時間、遅刻の時間、欠席の時間）

#出力　文字列（出席、遅刻、欠席）
def timeC(start_time,late_time,end_time):
    time = datetime.datetime.now()

    if time < late_time:
        return "出席"
    elif time < end_time:
        return "遅刻"
    else:
        return "欠席"

def timecheck(now:datetime, times:dict):
    now = datetime.datetime.now()

    START = times["start"]
    LATE = START + datetime.timedelta(minutes = times['late'])
    ABCENT = LATE + datetime.timedelta(minutes = times['limit'])

    if now < LATE:
        return "出席", 0
    elif now < ABCENT:
        return "遅刻", 1
    else:
        return "欠席", 2

if __name__ == "__main__":

    t1 = datetime.datetime(2021, 6, 2, 16, 00)
    t2 = datetime.datetime(2021, 6, 2, 17, 00)
    t3 = datetime.datetime(2021, 6, 2, 18, 00)


    time(t1, t2, t3)
