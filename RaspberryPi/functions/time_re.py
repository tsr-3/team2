# from types import LambdaType
import datetime
#def comp(idm:str,students,lect_time):


def my_time(now: datetime, lect_time):
    if now < lect_time['late']:
        return '出席'
    if now < lect_time['end']:
        return '遅刻'
    return '欠席'


if __name__ == '__main__':
    time = datetime.datetime.now()
    lect_time = {}
    print(time)
    #time ="06/02 15:15"
    lect_time['start'] =datetime.datetime(2021,6,2,16,00)
    lect_time['end'] =datetime.datetime(2021,6,2,19,00)
    lect_time['late']=datetime.datetime(2021,6,2,18,00)
    print(my_time(time, lect_time))
