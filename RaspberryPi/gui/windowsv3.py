import sys
from PyQt5.QtCore import QThread, QTimer
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from concurrent.futures.thread import ThreadPoolExecutor
# from util import (call_slow_request, processing_time)
import datetime
import threading
import timeget

class WinMake(QMainWindow):
    def __init__(self) -> None:
        super().__init__()

        # 窓の設定
        self.height_c = int(app.desktop().height() / 2.0)
        self.width_c = int(app.desktop().width() / 2.0)
        self.setGeometry(0, 0, self.width_c * 2, self.height_c * 2 - 100) # 位置
        # メニューバーの設定
        self.bar = self.menuBar()
        self.file = self.bar.addMenu("ファイル")
        self.export = self.file.addMenu("えくすぽーと")
        self.inport = self.file.addMenu("いんぽーと")
        self.edit = self.bar.addMenu("保存")
        self.view = self.bar.addMenu("A")
        self.search = self.bar.addMenu("B")
        self.tool = self.bar.addMenu("C")
        self.tool2 = self.bar.addMenu("D")
        self.hello = self.bar.addMenu("Hello")

        # ボタンの設定 ｘボタン
        self.exitbt = QPushButton("X", self)
        self.exitbt.setToolTip("このウィンドウを閉じます")
        self.exitbt.setShortcut("c")
        self.exitbt.setGeometry(int(self.width_c * 0.2), int(self.height_c * 0.2), 50, 50)
        # ボタンの設定 出席ボタン
        self.attendbt = QPushButton("出席をとる", self)
        self.attendbt.setToolTip("出席をとる画面を表示します")
        self.attendbt.setShortcut("s")
        self.attendbt.setGeometry(self.width_c, self.height_c, 100, 100)
        # ボタンの設定 Menuに戻るボタン
        self.returnmenubt = QPushButton("戻る", self)
        self.returnmenubt.setToolTip("Menuに戻ります")
        self.returnmenubt.setGeometry(int(self.width_c * 0.2), int(self.height_c * 0.2), 50, 50)
        # ラベルの設定 出席判別ラベル
        self.attendlb = QLabel("出席を判別するよ", self)
        self.attendlb.setGeometry(self.width_c - int(self.width_c * 0.2), self.height_c - 300, self.width_c * 2, 200)
        # ラベルの設定 ID出力ラベル
        self.attendidlb = QLabel("IDを出力するよ", self)
        self.attendidlb.setGeometry(self.width_c - int(self.width_c * 0.2), self.height_c, self.width_c * 2, 200)

        # QTimerの設定
        # timer = QTimer()
        # timer.timeout.connect(self.WinUpdate)
        # timer.start(1000)

        # 上記のものを全て隠す
        self.WinHide()
        # スタイルの呼び出し
        self.WinMenuUI()
        # イベント設定
        self.exitbt.clicked.connect(self.close)
        self.attendbt.clicked.connect(self.WinAttendUI)
        self.returnmenubt.clicked.connect(self.WinMenuUI)

        self.show()
        app.exec_()

    def WinAttendUI(self):
        '''AttendUIの表示'''
        self.WinHide()
        # AttendUIに用いる要素の表示
        self.returnmenubt.show()
        self.attendlb.show()
        self.attendidlb.show()

        # Attendのデザイン読み込み
        with open('attendsyl.qss') as f:
            css = f.read()
        app.setStyleSheet(css)

    def WinMenuUI(self):
        '''MenuUIの表示'''
        self.WinHide()
        # MenuUIに用いる要素の表示
        self.attendbt.show()
        self.exitbt.show()

        # Menuのデザイン読み込み
        with open('menusyl.qss') as f:
            css = f.read()
        app.setStyleSheet(css)

    def WinHide(self):
        '''要素を全て非表示にする'''
        self.attendbt.hide()
        self.exitbt.hide()
        self.attendlb.hide()
        self.attendidlb.hide()
        self.returnmenubt.hide()


    def WinUpdate(self, www):
        self.attendlb.setText("出席！")
        print("HELLO ", www)

# def run_concurrent():
#     with ThreadPoolExecutor() as executor:
#         # features = [executor.submit(call_slow_request) for _ in range(3)]
#         # for feature in features:
#             # print(feature.result())
# #
#         app = QApplication(sys.argv)
#         win = None
#         features = executor.submit(win = WinMake())
#         features.WinUpdate()
#         # features.WinMake()
#         # features.WinUpdate("hello")
#         # App = QApplication(sys.argv).WinMake()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = WinMake()
    # win.WinUpdate("hello")
    # run_concurrent()
    print ('hello world')