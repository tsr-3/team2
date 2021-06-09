from types import LambdaType
import datetime
#def comp(idm:str,students,lect_time):
    
time = datetime.datetime.now()
print(time)
#time ="06/02 15:15"
start_time =datetime.datetime(2021,6,2,16,00)
end_time =datetime.datetime(2021,6,2,19,00)
late_time=datetime.datetime(2021,6,2,18,00)


if time < late_time:
    print('出席')
elif time < end_time:
    print('遅刻')
else:
    print('欠席')

