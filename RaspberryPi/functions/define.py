'''
Main.py と windowsv3.py の橋渡しを行うための苦渋の策プログラム

nfcdataをglobalに置くことによって，nfcで取得したデータをGUIに出力することができるようになる
'''

# nfcのID
global nfcdata
nfcdata = "NFCのID"

# 対応する生徒の名前
global studentname
studentname = "生徒の名前"

