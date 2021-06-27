'''
GUIを表示するプログラム

app = QApplication(sys.argv)
win = WinMake(app)
で実行出来る

WinMake()
    __inti__(引数:QApplication型):GUIの初期設定(笑)が入力されている

    showfd():ファイル選択ダイアログボックスを表示する

    win_attendUI():UIを出席判別UIに変更する

    win_menuUI():UIをメインUIに変更する

    win_hide():UIに表示されている要素全てを非表示にする

    win_update():UIを再描写する

FileOpe():
    file_save():ファイルの保存処理を行う(予定)

    file_read():ファイルの読込処理を行う(予定)

'''

import os
import sys
import os.path
from PyQt5.QtCore import  Qt, QTimer
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from concurrent.futures.thread import ThreadPoolExecutor
# from util import (call_slow_request, processing_time)
import datetime
# windowsv3と値をやり取りするための苦渋の策
os.chdir(os.path.dirname(os.path.abspath(__file__)))
p = os.path.abspath('..')
sys.path.insert(1, p)
from functions import define



class WinMake(QMainWindow):
    '''メインウィンドウの生成を行う'''


    def __init__(self, app, parent=None) -> None:
        '''メインウィンドウの初期設定を行う'''
        # super().__init__()
        super(WinMake, self).__init__(parent)

        # 実行ファイルの移動
        move_current_dir()
        # 窓の設定
        self.height_c = int(app.desktop().height() / 2.0)
        self.width_c = int(app.desktop().width() / 2.0)
        self.winw = self.width_c
        self.winh = self.height_c
        self.showFullScreen()

        # ステータスバーの設定
        self.statusBar().showMessage("現在時刻が表示されるはずです テナント募集")
        self.statusBar().setStyleSheet("background-color: rgb(141, 196, 141)")
        self.status = 0

        # メニューバーの設定 File
        self.bar = self.menuBar()
        self.file = self.bar.addMenu("ファイル(&F)")
        self.file.setStatusTip("ファイル操作をまとめたものです")
         ###
        #File 保存
        self.export = QAction(QIcon("icon/save2.png"), "名前を付けて保存", self)
        self.export.setShortcut("Ctrl+s")
        self.export.setStatusTip("保存します")
        self.export.triggered.connect(FileOpe.file_save)
        self.export.triggered.connect(self.fd_save)
        self.file.addAction(self.export)
        #File 読込
        self.inport = QAction(QIcon("icon/write.png"), "時刻の読み込み", self)
        self.inport.setShortcut("Ctrl+o")
        self.inport.setStatusTip("出力します")
        self.inport.triggered.connect(FileOpe.file_read)
        self.inport.triggered.connect(self.fd_read)
        self.file.addAction(self.inport)
        #File 退出
        self.exit = QAction(QIcon("icon/exit3.png"), "Exit", self)
        self.exit.setStatusTip("画面を閉じます")
        self.exit.triggered.connect(self.close)
        self.file.addAction(self.exit)
         ###

        #メニュバーの設定 Operation
        self.ope = self.bar.addMenu("操作(&O)")
         ###
        #Operation 出席をとる
        self.data = QAction("出席をとる", self)
        self.data.setShortcut("Ctrl+a")
        self.data.setStatusTip("出席をとります")
        self.data.triggered.connect(self.win_attendUI)
        self.ope.addAction(self.data)
         ###

        #メニュバーの設定 Help
        # self.help = self.bar.addMenu("ヘルプ(&H)")
        self.help = self.bar.addMenu("インフォメーション(&I)")
        self.help1 = QAction(QIcon("icon/help2.png"), "情報", self)
        self.help1.triggered.connect(self.makeWindow)
        self.help.addAction(self.help1)
         ###

         ###

        self.tool = self.bar.addMenu("is(&BBBB)")
        self.tool2 = self.bar.addMenu("God(&G)")

    # Menu にのせるもの
        # ボタンの設定 ｘボタン
        self.exitbt = QPushButton("X", self)
        self.exitbt.setStyleSheet("background-color: red")
        self.exitbt.setToolTip("このウィンドウを閉じます")
        self.exitbt.setShortcut("c")
        self.exitbt.setGeometry(int(self.width_c * 2) - 50, 27, 50, 50)
        self.exitbt.clicked.connect(self.close)
        # ラベルの設定 取得時間割表示ラベル
        self.timetablelb = QLabel("時間割ファイルを設定してください", self)
        self.timetablelb.setStyleSheet("color: rgb(0,0,0)")
        self.timetablelb.setGeometry(int(self.width_c * 0.5), int(self.height_c * 0.5), 50000, 100)
        # ボタンの設定 ファイル読込ボタン
        self.readbt = QPushButton("ファイルの読込", self)
        self.readbt.setToolTip("Ctrl+o")
        self.readbt.setGeometry(int(self.timetablelb.x() - 110), int(self.timetablelb.y() + 30), 100, 50)
        self.readbt.clicked.connect(self.fd_read)
        # ボタンの設定 出席ボタン
        self.attendbt = QPushButton("出席をとる", self)
        self.attendbt.setToolTip("出席をとる画面を表示します")
        self.attendbt.setShortcut("s")
        self.attendbt.setGeometry(self.width_c - 175, self.height_c - 150, 400, 300)
        self.attendbt.setStyleSheet("font-size: 50pt")
        self.attendbt.clicked.connect(self.win_attendUI)

    #Attendにのせるもの
        # ボタンの設定 Menuに戻るボタン
        self.returnmenubt = QPushButton("戻る", self)
        self.returnmenubt.setToolTip("Menuに戻ります")
        self.returnmenubt.setShortcut("c")
        self.returnmenubt.setStyleSheet("background-color: red")
        self.returnmenubt.setGeometry(int(self.width_c * 2) - 50, 27, 50, 50)
        self.returnmenubt.clicked.connect(self.win_menuUI)
        # ラベルの設定 時刻出力ラベル
        self.timelb = QLabel("時刻を出力するよ", self)
        self.timelb.setGeometry(self.width_c - int(self.width_c * 0.6), self.height_c - 300, self.width_c * 2, 200)
        # ラベルの設定 ID出力ラベル
        self.idlb = QLabel("ID(または名前)を出力するよ", self)
        self.idlb.setGeometry(self.width_c - int(self.width_c * 0.6), int(self.timelb.y() + 300), self.width_c * 2, 200)
        # ラベルの設定 出席判別ラベル
        self.attendlb = QLabel("出席を判別するよ", self)
        self.attendlb.setGeometry(self.width_c - int(self.width_c * 0.6), int(self.idlb.y() +300), self.width_c * 2, 200)

        # QTimerの設定
        timer = QTimer()
        timer.timeout.connect(self.win_update)
        timer.start(int(1000/120))

        # スタイルの呼び出し
        self.win_menuUI()

        # 画面の表示とwin_updateの開始
        self.show()
        app.exec_()


    def fd_read(self):
        '''読み込みファイルを選択するダイアログの表示を行う'''
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
            self.timetablelb.setText(str(os.path.basename(fn[0])))

        return fn


    def fd_save(self):
        '''読み込みファイルを選択するダイアログの表示を行う'''
        fn = QFileDialog.getSaveFileName(self, str("ファイルを保存します"))
        #フィルタ
        if fn[0] == '':
            fn = "保存に失敗したようです"
            self.timetablelb.setText(str(fn))
        else:
            self.timetablelb.setStyleSheet("font-size: 25pt")
            self.timetablelb.setText(str(os.path.basename(fn[0])))

        return fn


    def win_attendUI(self):
        '''UIを出席判別画面へ変更する'''
        self.status = 1
        self.win_hide()
        # AttendUIに用いる要素の表示
        self.returnmenubt.show()
        self.attendlb.show()
        self.timelb.show()
        self.idlb.show()

        # Attendのデザイン読み込み
        with open('attendsyl.css') as f:
            css = f.read()
        self.setStyleSheet(css)


    def win_menuUI(self):
        '''UIをメイン画面へ変更する'''
        self.status = 0
        self.win_hide()
        # MenuUIに用いる要素の表示
        self.attendbt.show()
        self.exitbt.show()
        self.bar.show()
        self.readbt.show()
        self.timetablelb.show()

        # Menuのデザイン読み込み
        with open('menusyl.css') as f:
            css = f.read()
        self.setStyleSheet(css)


    def win_hide(self):
        '''要素を全て非表示にする'''
        self.attendbt.hide()
        self.exitbt.hide()
        self.attendlb.hide()
        self.idlb.hide()
        self.returnmenubt.hide()
        self.bar.hide()
        self.readbt.hide()
        self.timetablelb.hide()
        self.timelb.hide()


    def makeWindow(self):
        '''サブウィンドウ(ポップアップウィンドウ)の呼び出しを行う'''
        # サブウィンドウの作成
        subWindow = SubWindow()
        # サブウィンドウの表示
        subWindow.show()


    def win_update(self):
        '''指定ms毎に行われる処理'''
        try:
            self.timelb.setText(str(datetime.datetime.now()))
            if self.status == 0:
                self.statusBar().showMessage("現在時刻は" + str(datetime.datetime.now()) + "次回授業開始予定時刻は  None    メインウィンドウ※開発中Windowです")
                self.statusBar().setStyleSheet("background-color: rgb(141, 196, 141)")
            elif self.status == 1:
                with open('menusyl.css') as f:
                    css = f.read()
                self.setStyleSheet(css)
                self.statusBar().showMessage("現在時刻は" + str(datetime.datetime.now()) + "次回授業開始予定時刻は  None   出席判別ウィンドウ※開発中Windowです")
                self.idlb.setText("nfcのIDは" + define.nfcdata +"\n利用者名は" + define.studentname)
                self.attendlb.setText("出席判定の結果は " + define.attendcheck[0])

                if define.attendcheck[1] == 0:
                    self.statusBar().setStyleSheet("background-color: rgb(141, 196, 141)")
                elif define.attendcheck[1] == 1:
                    self.statusBar().setStyleSheet("background-color: rgb(196, 195, 114)")
                elif define.attendcheck[1] == 2:
                    self.statusBar().setStyleSheet("background-color: rgb(196, 114, 141)")
                elif define.attendcheck[1] == 3:
                    self.statusBar().setStyleSheet("background-color: rgb(93, 87, 185)")

        except:
            self.close()
            print('Something Happened')



class SubWindow(QWidget):
    '''ポップアップウィンドウの作成を行う'''


    def __init__(self, parent=None):
        '''ポップアップウィンドウの初期設定を行う'''
        self.w = QDialog(parent)
        self.w.setWindowTitle("このプロジェクトの情報")
        self.w.setGeometry(500, 500, 200, 300)

        label = QLabel('出席管理プロジェクト Team2', self.w)
        label2 = QLabel("他ファイルから授業の開始時刻,遅刻みなし時刻，欠席時刻等を入力し\nそれに対応する出力を行うことによっていい感じにします", self.w)
        label3 = QLabel(self.w)
        label3.setOpenExternalLinks(True)
        label3.setText("<a href='http://github.com/tsr-on-github/team2'>GitHubレポジトリ</a>")

        layout = QVBoxLayout()
        layout.addWidget(label)
        layout.addWidget(label2)
        layout.addWidget(label3)

        self.w.setLayout(layout)

    def show(self):
        '''ポップアップウィンドウの表示を行う'''
        self.w.exec_()



class FileOpe():
    '''ファイル操作を行う？'''
    def file_save(self):
        print("Saved!!")
        return "Saved!!"
    def file_read(self):
        print("Read!!")
        return "Read!!"


def move_current_dir():
    '''カレントディレクトリをこのプログラム(windowsv3)が存在するディレクトリに変更する'''
    os.chdir(os.path.dirname(os.path.abspath(__file__)))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = WinMake(app)

