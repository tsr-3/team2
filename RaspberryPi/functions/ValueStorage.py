'''
Main.py と windowsv3.py の橋渡しを行うための苦渋の策プログラム

nfcdataをglobalに置くことによって，nfcで取得したデータをGUIに出力することができるようになる
'''

# nfcのID
from datetime import datetime


global nfcdata
nfcdata = "NFCのID"

# 対応する生徒の名前
global studentname
studentname = "生徒の名前"

# 出席/遅刻/欠席
'''
0: 出席(通常状態)
1: 遅刻
2: 欠席
3: 非履修者

'''
global attendcheck
attendcheck = ["出席かどうかを判別", 0]

global filepath
filepath:str = None

global isFiledataExist
isFiledataExist:dict = {
    "professors": None,
    "students": None,
    "lecture": None
}

global process_state
process_state: int

global attendance
attendance:list = []

global thread
thread = None


global now_time
global late_time
late_time = 0
global abcent_time
abcent_time = 0