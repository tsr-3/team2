'''
GUIを表示するプログラム

app = QApplication(sys.argv)
win = WinMake(app)
で実行出来る

WinMake()
    __init__(引数:QApplication型):GUIの初期設定(笑)が入力されている
    GOinit   //push<shift-*>

    fd_read:読み込み用ファイル選択ダイアログボックスを表示する
    GOfd_read

    fd_save:書き出しファイル選択ダイアログボックスを表示する
    GOfd_save

    win_attendUI():UIを出席判別UIに変更する
    GOwin_attendUI

    win_menuUI():UIをメインUIに変更する
    GOwin_menuUI

    win_hide():UIに表示されている要素全てを非表示にする
    GOwin_hide

    message_info:サブウィンドウの呼び出す
    GOmessage_info

    win_update():UIを再描写する
    GOwin_update

    resize():ボタンやラベルのリサイズする
    GOresize

    messege_warn():ファイルが選択されていない場合の警告を呼び出す
    GOmessage_warn


InfoWindow()
    __init__():初期設定
    GOsubinit

    show():サブウィンドウの表示する
    GOshow

WarnWindow()
    __init__():初期設定
    GOwarninit

move_current_dir():作業ディレクトリをwindowsv3が存在する場所へ移動する(cssを読み込むため)
GOmove_current_dir

'''

import os
import sys
from typing import ValuesView
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
from functions import ValueStorage
from functions.SaveDataFile import SaveDataFile_noCipher as SaveDataFile
from functions import subwindows



class WinMake(QMainWindow):
    '''メインウィンドウの生成を行う'''



    #GOinit
    def __init__(self, app, parent=None) -> None:
        '''メインウィンドウの初期設定を行う'''
        # super().__init__()
        super(WinMake, self).__init__(parent)

        # 実行ファイルの移動
        move_current_dir()
        # 窓の設定
        #self.height_c = int(app.desktop().height() / 2.0)
        #self.width_c = int(app.desktop().width() / 2.0)

        #self.showFullScreen()
        self.setGeometry(100, 100, 1000, 500)
        self.show()

        self.now_width = 0 #現在起動されているGUIウィンドウの幅
        self.now_height = 0 #現在起動されているGUIウィンドウの高



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
        self.export.triggered.connect(self.fd_save)
        #self.file.addAction(self.export)
        #File 読込
        self.inport = QAction(QIcon("icon/write.png"), "時刻の読み込み", self)
        self.inport.setShortcut("Ctrl+o")
        self.inport.setShortcut("a")
        self.inport.setStatusTip("出力します")
        self.inport.triggered.connect(self.fd_read)
        self.file.addAction(self.inport)
        #File 退出
        self.exit = QAction(QIcon("icon/exit3.png"), "Exit", self)
        self.exit.setShortcut("Ctrl+c")
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
        self.help = self.bar.addMenu("ヘルプ(&H)")
        self.helper = QAction(QIcon("icon/help.png"), "ヘルプ", self)
        self.helper.setShortcut("ctrl+h")
        self.helper.triggered.connect(self.message_help)
        self.help.addAction(self.helper)

        #メニュバーの設定 info
        self.info = self.bar.addMenu("インフォメーション(&I)")
        self.info1 = QAction(QIcon("icon/info.png"), "情報", self)
        self.info1.triggered.connect(self.message_info)
        self.info.addAction(self.info1)
         ###

         ###

        #self.tool2 = self.bar.addMenu("God(&G)")

    # MainGUI にのせるもの
        # ボタンの設定 ｘボタン
        self.exitbt = QPushButton("X", self)
        self.exitbt.setStyleSheet("background-color: red")
        self.exitbt.setToolTip("このウィンドウを閉じます")
        self.exitbt.setShortcut("c")
        #self.exitbt.setGeometry(int(self.width_c * 2) - 50, 27, 50, 50)
        self.exitbt.setGeometry(int(self.width() - self.width() * 1/20) , int(1/20), int(self.width() * 1/20), int(self.width() * 1/20))
        #self.exitbt.clicked.connect(self.close)
        self.exitbt.clicked.connect(self.quit_window)
        # ボタンの設定 ファイル読込ボタン
        self.readbt = QPushButton("ファイルの読込", self)
        self.readbt.setToolTip("Ctrl+o")
        #self.readbt.setGeometry(int(self.timetablelb.x() - 110), int(self.timetablelb.y() + 30), 100, 50)
        self.readbt.setGeometry(int(self.width() * 1/10), int(self.height() * 1/4), int(self.width() *  1/10), int(self.height() * 1/10))
        self.readbt.clicked.connect(self.fd_read)
        # ラベルの設定 取得時間割表示ラベル
        self.timetablelb = QLabel("時間割ファイルを設定してください", self)
        self.timetablelb.setStyleSheet("color: rgb(0,0,0)")
        #self.timetablelb.setGeometry(int(self.width_c * 0.5), int(self.height_c * 0.5), 50000, 100)
        self.timetablelb.setGeometry(int(self.width() * 1/10 + self.readbt.x()), int(self.height() * 1/4), int(self.width()), int(self.height() * 1/10))
        # ボタンの設定 出席ボタン
        self.attendbt = QPushButton("出席をとる", self)
        self.attendbt.setToolTip("出席をとる画面を表示します")
        self.attendbt.setShortcut("s")
        #self.attendbt.setGeometry(self.width() - 175, self.height() - 150, 400, 300)
        self.attendbt.setGeometry(int(self.width() * 3/10), int(self.height() * 1/2), int(self.width() * 4/10), int(self.height() * 3/10))
        self.attendbt.setStyleSheet("font-size: 50pt")
        self.attendbt.clicked.connect(self.win_attendUI)

    #AttendGUIにのせるもの
        # ボタンの設定 Menuに戻るボタン
        self.returnmenubt = QPushButton("終了", self)
        self.returnmenubt.setToolTip("Menuに戻ります")
        self.returnmenubt.setShortcut("c")
        self.returnmenubt.setStyleSheet("background-color: red")
        #self.returnmenubt.setGeometry(int(self.width_c * 2) - 50, 27, 50, 50)
        self.returnmenubt.setGeometry(int(self.width() - self.width() * 1/20) , int(1/20), int(self.width() * 1/20), int(self.width() * 1/20))
        self.returnmenubt.clicked.connect(self.win_menuUI)
        # ラベルの設定 時刻出力ラベル
        self.timelb = QLabel("時刻を出力するよ", self)
        #self.timelb.setGeometry(self.width_c - int(self.width_c * 0.6), self.height_c - 300, self.width_c * 2, 200)
        self.timelb.setGeometry(int(self.width() * 1/10), int(self.height() * 1/10), int(self.width() ), int(self.height() * 3/10))
        # ラベルの設定 ID出力ラベル
        self.idlb = QLabel("ID(または名前)を出力するよ", self)
        #self.idlb.setGeometry(self.width_c - int(self.width_c * 0.6), int(self.timelb.y() + 300), self.width_c * 2, 200)
        self.idlb.setGeometry(int(self.width() * 1/10), int(self.timelb.height() + self.timelb.y() + self.height() * 1/10), self.width(), int(self.height() * 2/10))
        # ラベルの設定 出席判別ラベル
        self.attendlb = QLabel("出席を判別するよ", self)
        #self.attendlb.setGeometry(self.width_c - int(self.width_c * 0.6), int(self.idlb.y() +300), self.width_c * 2, 200)
        self.attendlb.setGeometry(int(self.width() * 1/10), int(self.idlb.height() + self.idlb.y() + self.height() * 1/10), self.width(), int(self.height() * 1/10))


        self.latetime = datetime.datetime.now()
        self.abcenttime = self.latetime

        # QTimerの設定
        timer = QTimer()
        timer.timeout.connect(self.win_update)
        timer.start(int(1000/120))


        # スタイルの呼び出し
        self.win_menuUI()

        # 画面の表示とwin_updateの開始
        self.show()
        app.exec_()



    def quit_window(self):
        '''MainUIのXボタンを押したときの処理'''

        #ここにValueStorageに使う値を書いてね
        ValueStorage.process_state = 3
        attend = []
        for dat in ValueStorage.attendance:
            attend.append(str(dat['time']) + ' ' + dat['id'])
        print('[debug] save', ValueStorage.lectID)
        SaveDataFile.write({'attendance': '\n'.join(attend), 'lecture': {'id': ValueStorage.lectID}}, datetime.datetime.now().strftime('%Y-%m-%d_%H%M') + '.t2pecf')
        ValueStorage.thread.shutdown(cancel_futures = True, wait = False)
        self.close()
        os._exit(0)



    #GOfd_read
    def fd_read(self):
        '''読み込みファイルを選択するダイアログの表示を行う'''
        # fn = QFileDialog.getOpenFileName(self,str("用いたいファイルを選んでください"), "/home/deskTop", str("Image Files (*.png *.jpg *.bmp)"))
        fn = QFileDialog.getOpenFileName(self,str("用いたいファイルを選んでください"), filter="Team Files(*.json *.t2pecf)")
        # print(fn)
        # print(type(fn[0])) #ファイル名
        # print(type(fn[1])) #拡張子分類

        #フィルタ
        if fn[0] == '':
            fn = "選択に失敗したようです"
            self.timetablelb.setText(str(fn))
            # ValueStorage.attendcheck[1] == 2: # 欠席
            self.statusBar().setStyleSheet("background-color: rgb(196, 114, 141)")
        else:
            self.timetablelb.setStyleSheet("font-size: 25pt")
            self.timetablelb.setText(str(os.path.basename(fn[0])))
            # print(fn[0])
            self.statusBar().setStyleSheet("background-color: rgb(141, 196, 141)")

            ValueStorage.filepath = fn[0]


        return fn


    #GOfd_save
    def fd_save(self):
        '''書き出しファイルを選択するダイアログの表示を行う'''
        fn = QFileDialog.getSaveFileName(self, str("ファイルを保存します"))
        #フィルタ
        if fn[0] == '':
            fn = "保存に失敗したようです"
            self.timetablelb.setText(str(fn))
            self.statusBar().setStyleSheet("background-color: rgb(196, 114, 141)")
        else:
            self.timetablelb.setStyleSheet("font-size: 25pt")
            self.timetablelb.setText(str(os.path.basename(fn[0])))
            self.statusBar().setStyleSheet("background-color: rgb(141, 196, 141)")

        return fn


    #GOwin_attendUI
    def win_attendUI(self):
        '''UIを出席判別画面へ変更する'''
        #print("hello")
        if self.messege_warn():

            return

        print(ValueStorage.isFiledataExist)

        if (ValueStorage.isFiledataExist["professors"] is None) or (ValueStorage.isFiledataExist["students"] is None) or (ValueStorage.isFiledataExist["lecture"] is None):
            self.timetablelb.setText("出席が取れないファイルです")
            return

        self.status = 1
        self.win_hide()
        # AttendUIに用いる要素の表示
        self.returnmenubt.show()
        self.attendlb.show()
        self.timelb.show()
        self.idlb.show()
        self.statusBar().setStyleSheet("background-color: rgb(141, 196, 141)")

        # Attendのデザイン読み込み
        with open('style/attendsyl.css') as f:
            css = f.read()
        self.setStyleSheet(css)
        ValueStorage.process_state = 2 # STATE_ACCEPTING
        ValueStorage.now_time = datetime.datetime.now()
        self.latetime = ValueStorage.now_time + datetime.timedelta(minutes=ValueStorage.late_time)
        self.abcenttime = self.latetime + datetime.timedelta(minutes=ValueStorage.abcent_time)
        ValueStorage.attendance.append({'time': ValueStorage.now_time, 'id': 'start'})





    #GOwin_menuUI
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
        with open('style/menusyl.css') as f:
            css = f.read()
        self.setStyleSheet(css)


    #GOwin_hide
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


    #GOwin_update
    def win_update(self):
        '''指定ms毎に行われる処理'''
        try:
            self.timelb.setText("現在時刻は" + str(datetime.datetime.now()) + "\n" + str(self.latetime.time()) + "まで出席" + str(self.abcenttime.time()) + "まで遅刻")
            if self.status == 0:
                self.statusBar().showMessage("現在時刻は" + str(datetime.datetime.now()) + "メインウィンドウ")
            elif self.status == 1:
                with open('style/menusyl.css') as f:
                    css = f.read()
                self.setStyleSheet(css)
                self.statusBar().showMessage("現在時刻は" + str(datetime.datetime.now()) + "出席判別ウィンドウ")
                self.idlb.setText("nfcのIDは" + ValueStorage.nfcdata +"\n利用者名は" + ValueStorage.studentname)
                self.attendlb.setText("出席判定の結果は " + ValueStorage.attendcheck[0])

                if ValueStorage.attendcheck[1] == 0: # 通常/出席
                    self.statusBar().setStyleSheet("background-color: rgb(141, 196, 141)")
                elif ValueStorage.attendcheck[1] == 1: # 遅刻
                    self.statusBar().setStyleSheet("background-color: rgb(196, 195, 114)")
                elif ValueStorage.attendcheck[1] == 2: # 欠席
                    self.statusBar().setStyleSheet("background-color: rgb(196, 114, 141)")
                elif ValueStorage.attendcheck[1] == 3: # 非履修
                    self.statusBar().setStyleSheet("background-color: rgb(93, 87, 185)")

            self.resize()
        except:
            self.close()
            print('Something Happened')
            self.timetablelb.setText('Something Happend(ERROR)')


    #GOresize
    def resize(self):
        '''ボタンやラベルのリサイズを行う'''
        if not self.isFullScreen(): #フルスクリーンウィンドウでなければ
            if (self.height() != self.now_height or self.width() != self.now_width): # GUIウィンドウの大きさが変化したときにボタンやラベルの大きさを変更する
                self.exitbt.setGeometry(int(self.width() - self.width() * 1/20) , int(1/20), int(self.width() * 1/20), int(self.width() * 1/20))
                self.readbt.setGeometry(int(self.width() * 1/10), int(self.height() * 1/4), int(self.width() *  1/10), int(self.height() * 1/10))
                self.timetablelb.setGeometry(int(self.width() * 1/10 + self.readbt.x()), int(self.height() * 1/4), int(self.width()), int(self.height() * 1/10))
                self.attendbt.setGeometry(int(self.width() * 3/10), int(self.height() * 1/2), int(self.width() * 4/10), int(self.height() * 3/10))
                self.returnmenubt.setGeometry(int(self.width() - self.width() * 1/20) , int(1/20), int(self.width() * 1/20), int(self.width() * 1/20))
                self.timelb.setGeometry(int(self.width() * 1/10), int(self.height() * 1/10), int(self.width() ), int(self.height() * 2/10))
                self.idlb.setGeometry(int(self.width() * 1/10), int(self.timelb.height() + self.timelb.y() + self.height() * 1/10), self.width(), int(self.height() * 2/10))
                self.attendlb.setGeometry(int(self.width() * 1/10), int(self.idlb.height() + self.idlb.y() + self.height() * 1/10), self.width(), int(self.height() * 1/10))

        self.now_width = self.width()
        self.now_height = self.height()


    #GOmessage_warn
    def messege_warn(self):
        '''ファイルが選択されていない場合に警告画面を表示する'''
        if (self.timetablelb.text() == "時間割ファイルを設定してください") or (self.timetablelb.text() == "選択に失敗したようです"):
            # サブウィンドウの作成
            warn = subwindows.WarnWindow()
            # サブウィンドウの表示
            warn.show()

            self.fd_read()

            return True


    #GOmessage_info
    def message_info(self):
        '''サブウィンドウ(ポップアップウィンドウ)の呼び出しを行う'''
        # サブウィンドウの作成
        infowindow = subwindows.InfoWindow()
        # サブウィンドウの表示
        infowindow.show()

    def message_help(self):
        helpwindow = subwindows.HelpWindow()
        helpwindow.show()

#GOmove_current_dir
def move_current_dir():
    '''カレントディレクトリをこのプログラム(windowsv3)が存在するディレクトリに変更する'''
    os.chdir(os.path.dirname(os.path.abspath(__file__)))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = WinMake(app)

