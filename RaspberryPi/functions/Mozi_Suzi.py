import datetime
now = datetime.datetime.now()
print(now)

#文字列からdatetime
#datetime.datetime.strptime(文字列,'%Y/%m/%d %H:%M:%S')
dt_str = '2021/06/23 18:00:00'#文字列
dt =datetime.datetime.strptime(dt_str,'%Y/%m/%d %H:%M:%S')
print(dt)

#datetimeから文字列
#print(datetime.datetime.now()した変数.strftime('%Y/%m/%d %H:%M:%S'))
dd=dt.strftime('%Y/%m/%d %H:%M:%S')
print(dd)
