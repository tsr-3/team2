from os import name
import sys
import os.path
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
        self.winw = self.width_c
        self.winh = self.height_c
        # self.setGeometry(0, 0, self.width_c * 2, self.height_c * 2) # 位置
        self.showFullScreen()
        # self.setGeometry(0, 0, self.winw, self.winh) # 位置
        # ステータスバーの設定
        self.statusBar().showMessage("現在時刻が表示されるはずです テナント募集")
        self.statusBar().setStyleSheet("background-color: rgb(141, 196, 141)")
        self.status = 0
        # メニューバーの設定
        self.bar = self.menuBar()
        self.file = self.bar.addMenu("ファイル(&F)")
         #メニューバーボタンの設定 保存
        self.export = QAction("名前を付けて保存", self)
        self.export.setShortcut("Ctrl+s")
        self.export.setStatusTip("保存します")
        self.export.triggered.connect(FileOpe.SaveFile)
        self.file.addAction(self.export)
         #メニューバーボタンの設定 読込
        self.inport = QAction("時刻の読み込み", self)
        self.inport.setShortcut("Ctrl+o")
        self.inport.setStatusTip("出力します")
        self.inport.triggered.connect(FileOpe.ReadFile)
        self.inport.triggered.connect(self.showfd)
        self.file.addAction(self.inport)
         #メニューバーボタンの設定 退出
        self.exit = QAction("Exit", self)
        self.exit.setStatusTip("画面を閉じます")
        self.exit.triggered.connect(self.close)
        self.file.addAction(self.exit)
        self.help = self.bar.addMenu("ヘルプ(&H)")
        self.search = self.bar.addMenu("B(&B)")
        self.tool = self.bar.addMenu("is(&I)")
        self.tool2 = self.bar.addMenu("God(&G)")


        # ボタンの設定 ｘボタン
        self.exitbt = QPushButton("X", self)
        self.exitbt.setStyleSheet("background-color: red")
        self.exitbt.setToolTip("このウィンドウを閉じます")
        self.exitbt.setShortcut("c")
        self.exitbt.setGeometry(int(self.width_c * 2) - 50, 27, 50, 50)
        # self.exitbt.setGeometry(int(self.winw * 0.8), int(self.winh * 0.2), 50, 50)
        # ラベルの設定 取得時間割表示ラベル
        self.timetablelb = QLabel("時間割ファイルを設定してください", self)
        self.timetablelb.setStyleSheet("color: rgb(0,0,0)")
        self.timetablelb.setGeometry(int(self.width_c * 0.5), int(self.height_c * 0.5), 50000, 100)
        # self.timetablelb.setGeometry(int(self.winw * 0.2), int(self.winh * 0.5), 50000, 100)
        # ボタンの設定 ファイル読込ボタン
        self.readbt = QPushButton("ファイルの読込", self)
        self.readbt.setToolTip("Ctrl+o")
        # self.readbt.setStyleSheet("background-color: blue")
        self.readbt.setGeometry(int(self.timetablelb.x() - 110), int(self.timetablelb.y() + 30), 100, 50)
        # self.readbt.setGeometry(int(self.timetablelb.x() - 100), int(self.timetablelb.y()), 100, 100)
        # ボタンの設定 出席ボタン
        self.attendbt = QPushButton("出席をとる", self)
        self.attendbt.setToolTip("出席をとる画面を表示します")
        self.attendbt.setShortcut("s")
        self.attendbt.setGeometry(self.width_c - 175, self.height_c - 150, 350, 300)
        # self.attendbt.setGeometry(int(self.winw * 0.5), int(self.winh * 0.7), 100, 100)
        self.attendbt.setStyleSheet("font-size: 50pt")
        # ボタンの設定 Menuに戻るボタン
        self.returnmenubt = QPushButton("戻る", self)
        self.returnmenubt.setToolTip("Menuに戻ります")
        self.returnmenubt.setShortcut("c")
        self.returnmenubt.setStyleSheet("background-color: red")
        self.returnmenubt.setGeometry(int(self.width_c * 2) - 50, 27, 50, 50)
        # self.returnmenubt.setGeometry(int(self.winw * 0.8), int(self.winh * 0.2), 50, 50)
        # ラベルの設定 出席判別ラベル
        self.attendlb = QLabel("出席を判別するよ", self)
        self.attendlb.setGeometry(self.width_c - int(self.width_c * 0.6), self.height_c - 300, self.width_c * 2, 200)
        # self.attendlb.setGeometry(int(self.winh * 0.2), int(self.winh * 0.5), self.width_c * 2, 200)
        # ラベルの設定 ID出力ラベル
        self.idlb = QLabel("ID(または名前)を出力するよ", self)
        self.idlb.setGeometry(self.width_c - int(self.width_c * 0.6), int(self.attendlb.y() + 300), self.width_c * 2, 200)
        # self.idlb.setGeometry(int(self.winw * 0.2), int(self.winh * 0.8), self.width_c * 2, 200)

        # QTimerの設定
        timer = QTimer()
        timer.timeout.connect(self.WinUpdate)
        timer.start(1000)

        # 上記のものを全て隠す
        self.WinHide()
        # スタイルの呼び出し
        self.WinMenuUI()
        # イベント設定
        self.exitbt.clicked.connect(self.close)
        self.attendbt.clicked.connect(self.WinAttendUI)
        self.returnmenubt.clicked.connect(self.WinMenuUI)
        self.readbt.clicked.connect(self.showfd)

        self.show()
        app.exec_()

    def showfd(self):
        # fn = QFileDialog.getOpenFileName(self,str("用いたいファイルを選んでください"), "/home/deskTop", str("Image Files (*.png *.jpg *.bmp)"))
        fn = QFileDialog.getOpenFileName(self,str("用いたいファイルを選んでください"))
        # print(fn)
        # print(type(fn[0])) #ファイル名
        # print(type(fn[1])) #拡張子分類

        #フィルタ
        if fn[0] == '':
            fn = "選択に失敗したようです"
            self.timetablelb.setText(str(fn))
        else:
            self.timetablelb.setStyleSheet("font-size: 25pt")
            self.timetablelb.setText(str(fn[0]))

        return fn


    def WinAttendUI(self):
        self.status = 1
        '''AttendUIの表示'''
        self.WinHide()
        # AttendUIに用いる要素の表示
        self.returnmenubt.show()
        self.attendlb.show()
        self.idlb.show()

        # Attendのデザイン読み込み
        with open('attendsyl.css') as f:
            css = f.read()
        app.setStyleSheet(css)

    def WinMenuUI(self):
        self.status = 0
        '''MenuUIの表示'''
        self.WinHide()
        # MenuUIに用いる要素の表示
        self.attendbt.show()
        self.exitbt.show()
        self.bar.show()
        self.readbt.show()
        self.timetablelb.show()

        # Menuのデザイン読み込み
        with open('menusyl.css') as f:
            css = f.read()
        app.setStyleSheet(css)

    def WinHide(self):
        '''要素を全て非表示にする'''
        self.attendbt.hide()
        self.exitbt.hide()
        self.attendlb.hide()
        self.idlb.hide()
        self.returnmenubt.hide()
        self.bar.hide()
        self.readbt.hide()
        self.timetablelb.hide()


    def WinUpdate(self):
        try:
            if self.status == 0:
                self.attendlb.setText(str(datetime.datetime.now()))
                self.statusBar().showMessage("現在時刻は" + str(datetime.datetime.now()) + "次回授業開始予定時刻は  None                                                                                                                                                                                                                                                                                                                     メインウィンドウ※開発中Windowです")
                # self.statusBar().showMessage("現在時刻は" + str(datetime.datetime.now()) + "次回授業開始予定時刻は" + str(self.))
            elif self.status == 1:
                self.attendlb.setText(str(datetime.datetime.now()))
                self.statusBar().showMessage("現在時刻は" + str(datetime.datetime.now()) + "次回授業開始予定時刻は  None                                                                                                                                                                                                                                                                                                              出席判別ウィンドウ※開発中Windowです")
        except:
            self.close()
            print('Something Happened')


class FileOpe():
    def SaveFile(self):
        print("Saved!!")
    def ReadFile(self):
        print("Read!!")

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
