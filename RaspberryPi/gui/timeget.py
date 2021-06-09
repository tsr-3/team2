# 出席， 遅刻， 非履修者をモニターに表示するやーつ 試作1号(デバックの部)
# 事前設定
#  出席 時刻丁度
#  遅刻 遅刻猶予時刻よりも時刻が後ろの
#  非履修者 存在しない

'''
製作者:B21P036
動作:現在時刻と設定時刻を比較し，出席/遅刻を判別する

関数
class Person(デバック用)
    def Set: 生徒の情報を入力

class Subject(デバック用)
    def __init__: 初期設定
    def SetTime: 講義の時刻を設定できる


def AttendOrTard: 時刻を判別し
    現在時刻 <= 設定時刻ならば True
    現在時刻 >= 設定時刻ならば False
    を出力する

説明
画面出力のためにデバック用に作ったやつです
多分僕のやる範囲外なので消してもらっていいです

pip(もしくはpip3) install python-dateutil が必要です
'''


import datetime
import dateutil.parser



class Person:
    '''人の設定を行う'''
    def __init__(self) -> None:
        self.name = "加藤"
        self.id = "12345abcd"
        self.sub = "英語"


    def Set(self, str1, num, subject):
        self.name = str1
        self.id = num
        self.sub = subject

class Subject:
    '''講義の設定を行う'''
    def __init__(self) -> None:
        self.sub = "英語"
        self.start = datetime.datetime.now()

    def StartTime(self, str):
        self.start = dateutil.parser.parse(str)
        return self.start

def test():
    now = datetime.datetime.now()
    A = Person()
    # print(A.name, A.sub, A.id, type(A))
    print(A.name, A.sub, A.id)


    B = Person()
    B.Set("平間", "0000aaa", "英語")
    # print(B.name, B.sub, B.id, type(B))
    print(B.name, B.sub, B.id)

    C = Subject()
    st = C.StartTime("21:57")
    print("現在時刻 = ", now)
    print(C.sub, "の開始時刻は", C.StartTime)
    if(now <= st): #開始時刻に間に合った場合
        print("now <= C")
        return True
    else: #遅刻した場合
        print("now > C")
        return False

if __name__ == '__main__':
    now = datetime.datetime.now()
    A = Person()
    # print(A.name, A.sub, A.id, type(A))
    print(A.name, A.sub, A.id)


    B = Person()
    B.Set("平間", "0000aaa", "英語")
    # print(B.name, B.sub, B.id, type(B))
    print(B.name, B.sub, B.id)

    C = Subject()
    st = C.StartTime("18:18")
    print("現在時刻 = ", now)
    print(C.sub, "の開始時刻は", C.StartTime)
    if(now <= st): #開始時刻に間に合った場合
        print("now <= C")
    else: #遅刻した場合
        print("now > C")