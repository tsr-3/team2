# coding: utf-8

# attendance string
# [year]-[month]-[day] [hour]:[minutes]:[second] [student-id]
# ex) 2021-07-09 03:44:24 B21P037

import dateutil.parser
import datetime

class Attendance:

    _attendance: list = None

    def __init__(this, value = None): # constructor
        if type(value) is str:
            this._attendance = []
            for line in value.split('\n'):
                tmp = line.split(' ')
                this._attendance.append({'time':dateutil.parser.parse(tmp[0] + ' ' + tmp[1]), 'student': tmp[2]})
            return
        if type(value) is list:
            for val in value:
                if 'time' not in val or 'student' not in val:
                    return None
                if isinstance(val['time']) is not datetime:
                    return None
                if type(val['student']) is not str:
                    return None
            this._attendance = value

    def __iadd__(this, value:dict): # +=
        if 'time' not in value or 'student' not in value:
            return None
        if isinstance(value['time']) is not datetime:
            return None
        if type(value['student']) is not str:
            return None
        if type(this._attendance) is not list:
            return None
        this._attendance.append(value)
    
    def stringify(this):
        string:str = ''
        for attendance in this._attendance:
            string += str(attendance['time']) + ' ' + attendance['student'] + '\n'
        return string

if __name__ == '__main__':
    pass
