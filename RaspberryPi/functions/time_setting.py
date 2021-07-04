'''
製作者:B21P036
datetime型の計算を行うプログラム

ANY_add(足されるもの(datetime型), 足すもの((+,-の)整数型を推奨, 少数型でも可))

weeks_add:週を加算する
GOweeks

days_add:日
GOdays

hours_add:時
GOhours

minutes_add:分
GOminutes

seconds_add:秒
GOseconds

milliseconds_add:ミリ秒
GOmilliseconds

microseconds_add:マイクロ秒
GOmicroseconds


years とmonths は無いらしい(dateutil で可能らしいが実装保留)
'''

import datetime


#GOweeks
def weeks_add(original, additon):
    '''週を加算する'''
    return original + datetime.timedelta(weeks = additon)

#GOdays
def days_add(original, additon):
    '''日を加算する'''
    return original + datetime.timedelta(days = additon)

#GOhours
def hours_add(original, additon):
    '''時を加算する'''
    return original + datetime.timedelta(hours = additon)

#GOminutes
def minutes_add(original, additon):
    '''分を加算する'''
    return original + datetime.timedelta(minutes = additon)

#GOseconds
def seconds_add(original, additon):
    '''秒を加算する'''
    return original + datetime.timedelta(seconds = additon)

#GOmilliseconds
def milliseconds_add(original, additon):
    '''ミリ秒を加算する'''
    return original + datetime.timedelta(milliseconds = additon)

#GOmicroseconds
def microseconds_add(original, additon):
    '''マイクロ秒を加算する'''
    return original + datetime.timedelta(microseconds = additon)



if __name__ == "__main__":
    t1 = datetime.datetime(2021, 1, 1, 0, 0, 0, 0)
    print(t1)
    ans = weeks_add(t1, 9)
    print(ans)
    ans = days_add(t1, 1)
    print(ans)
    ans = hours_add(t1, 1)
    print(ans)
    ans = seconds_add(t1, 1)
    print(ans)
    ans = milliseconds_add(t1, 1)
    print(ans)
    ans = microseconds_add(t1, 1)
    print(ans)
