from types import LambdaType
import datetime

#入力(start_time,late_time,end_time):
#入力（出席の時間、遅刻の時間、欠席の時間）

#出力　文字列（出席、遅刻、欠席）
def time(start_time,late_time,end_time):
    time = datetime.datetime.now()

    if time < late_time:
        return "出席"
    elif time < end_time:
        return "遅刻"
    else:
        return "欠席"

