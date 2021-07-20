import os
import sys
from PyQt5.QtCore import  Qt, QTimer
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

class WarnWindow(QWidget):
    '''ファイルが選択できていない場合の警告画面の作成を行う'''


    #GOwarninit
    def __init__(self, parent=None):
        '''ウィンドウ初期設定を行う'''
        self.w = QDialog(parent)
        self.w.setWindowTitle("ファイルの読み込みが出来ていません")
        self.w.setGeometry(500, 500, 200, 300)

        label = QLabel(self.w)
        label.setText('授業関係ファイルを選択してください :)')
        label.setFont(QFont("Arial", 14, QFont.Black))

        # ファイルを読み込み
        image = QImage('style/ex.gif')
        imagelabel = QLabel()
        # ラベルに読み込んだ画像を反映
        imagelabel.setPixmap(QPixmap.fromImage(image))
        # スケールは1.0
        imagelabel.scaleFactor = 0.3


        exit = QPushButton(self.w)
        exit.setGeometry(0, 0, 1, 1)
        exit.setShortcut("Ctrl+c")
        exit.setShortcut("c")
        exit.clicked.connect(self.w.close)

        layout = QVBoxLayout()
        layout.addWidget(label)
        layout.addWidget(imagelabel)

        self.w.setLayout(layout)

    def show(self):
        '''表示を行う'''
        self.w.exec_()


class InfoWindow(QWidget):
    '''ポップアップウィンドウの作成を行う'''

    VERSION = '1.0.0'

    #GOsubinit
    def __init__(self, parent=None):
        '''ポップアップウィンドウの初期設定を行う'''
        self.w = QDialog(parent)
        self.w.setWindowTitle("このプロジェクトの情報")
        self.w.setGeometry(500, 500, 200, 300)

        label = QLabel('出席管理プロジェクト Team2 version:' + InfoWindow.VERSION, self.w)
        label2 = QLabel("出席確認システムで設定された情報を元に生徒の出席を判別,集計します", self.w)
        label3 = QLabel(self.w)
        label3.setOpenExternalLinks(True)
        label3.setText("<a href='http://github.com/tsr-on-github/team2'>GitHubレポジトリ</a>")

        layout = QVBoxLayout()
        layout.addWidget(label)
        layout.addWidget(label2)
        layout.addWidget(label3)

        self.w.setLayout(layout)

    #GOshow
    def show(self):
        '''ポップアップウィンドウの表示を行う'''
        self.w.exec_()



class HelpWindow(QWidget):
    '''ファイルが選択できていない場合の警告画面の作成を行う'''

    def __init__(self, parent=None):
        '''ウィンドウ初期設定を行う'''
        self.w = QDialog(parent)
        self.w.setWindowTitle("ヘルプ")
        self.w.setGeometry(200, 200, 200, 150)

        label = QLabel(self.w)
        label.setText('使い方')
        label.setFont(QFont("Arial", 14, QFont.Black))

        self.h1 = QPushButton("手順1(出席判定ファイルの読込方法について)", self.w)
        self.h1.clicked.connect(HelpWindow.pro1)
        self.h2 = QPushButton("手順2(出席判定の開始方法について)", self.w)
        self.h2.clicked.connect(HelpWindow.pro2)
        self.h3 = QPushButton("手順3(出席判定中画面の要素について)", self.w)
        self.h3.clicked.connect(HelpWindow.pro3)
        self.h4 = QPushButton("手順4(出席判定後に出力されるファイルについて)", self.w)
        self.h4.clicked.connect(HelpWindow.pro4)

        exit = QPushButton(self.w)
        exit.setGeometry(0, 0, 1, 1)
        exit.setShortcut("Ctrl+c")
        exit.setShortcut("c")
        exit.clicked.connect(self.w.close)

        layout = QVBoxLayout()
        layout.addWidget(label)
        layout.addWidget(self.h1)
        layout.addWidget(self.h2)
        layout.addWidget(self.h3)
        layout.addWidget(self.h4)

        self.w.setLayout(layout)

    def show(self):
        '''表示を行う'''
        self.w.exec_()

    def pro1(self):
        help1 = WinHelp1()
        help1.show()

    def pro2(self):
        help2 = WinHelp2()
        help2.show()

    def pro3(self):
        help3 = WinHelp3()
        help3.show()

    def pro4(self):
        help4 = WinHelp4()
        help4.show()


class WinHelp1(QWidget):
    def __init__(self, parent=None):
        '''ウィンドウ初期設定を行う'''
        self.w = QDialog(parent)
        self.w.setWindowTitle("手順1")
        self.w.setGeometry(400, 400, 200, 300)

        label = QLabel(self.w)
        label.setText('「ファイルの読込」ボタンを押して,出席を取るファイル(t2pecf拡張子)を選択しましょう')
        label.setFont(QFont("Arial", 14, QFont.Black))
        label2 = QLabel(self.w)
        label2.setText('t2pecfは，T２ｐｅｃｆ ｉｓ ｔｅａｍ2 RａｓｐｂｅｒｒｙＰｉ Eｌｅｃｔｏｎ Cｏｍｍｕｎｉｃａｔｉｏｎ Fｉｌｅ の略です')
        label2.setFont(QFont("Arial", 14, QFont.Black))

        # ファイルを読み込み
        image = QImage('style/protocol1.gif')
        imagelabel = QLabel()
        # ラベルに読み込んだ画像を反映
        imagelabel.setPixmap(QPixmap.fromImage(image))
        # スケールは1.0
        imagelabel.scaleFactor = 0.3


        exit = QPushButton(self.w)
        exit.setGeometry(0, 0, 1, 1)
        exit.setShortcut("Ctrl+c")
        exit.setShortcut("c")
        exit.clicked.connect(self.w.close)

        layout = QVBoxLayout()
        layout.addWidget(label)
        layout.addWidget(label2)
        layout.addWidget(imagelabel)

        self.w.setLayout(layout)

    def show(self):
        '''表示を行う'''
        self.w.exec_()

class WinHelp2(QWidget):
    def __init__(self, parent=None):
        '''ウィンドウ初期設定を行う'''
        self.w = QDialog(parent)
        self.w.setWindowTitle("手順2")
        self.w.setGeometry(400, 400, 200, 300)

        label = QLabel(self.w)
        label.setText('「出席を取る」ボタンを押しましょう\n コレを押した瞬間に出席受付と出席計測区間が開始されます')
        label.setFont(QFont("Arial", 14, QFont.Black))

        # ファイルを読み込み
        image = QImage('style/protocol2.gif')
        imagelabel = QLabel()
        # ラベルに読み込んだ画像を反映
        imagelabel.setPixmap(QPixmap.fromImage(image))
        # スケールは1.0
        imagelabel.scaleFactor = 0.3


        exit = QPushButton(self.w)
        exit.setGeometry(0, 0, 1, 1)
        exit.setShortcut("Ctrl+c")
        exit.setShortcut("c")
        exit.clicked.connect(self.w.close)

        layout = QVBoxLayout()
        layout.addWidget(label)
        layout.addWidget(imagelabel)

        self.w.setLayout(layout)

    def show(self):
        '''表示を行う'''
        self.w.exec_()

class WinHelp3(QWidget):
    def __init__(self, parent=None):
        '''ウィンドウ初期設定を行う'''
        self.w = QDialog(parent)
        self.w.setWindowTitle("手順3")
        self.w.setGeometry(400, 400, 200, 300)

        label = QLabel(self.w)
        label.setText('この画面になった状態でカードリーダーにカードをタッチすると生徒の情報が画面に表示され出席データに保存されます\nこの画面から「戻る」ことで出席受付が終了します')
        label.setFont(QFont("Arial", 14, QFont.Black))

        # ファイルを読み込み
        image = QImage('style/protocol3.gif')
        imagelabel = QLabel()
        # ラベルに読み込んだ画像を反映
        imagelabel.setPixmap(QPixmap.fromImage(image))
        # スケールは1.0
        imagelabel.scaleFactor = 0.3


        exit = QPushButton(self.w)
        exit.setGeometry(0, 0, 1, 1)
        exit.setShortcut("Ctrl+c")
        exit.setShortcut("c")
        exit.clicked.connect(self.w.close)

        layout = QVBoxLayout()
        layout.addWidget(label)
        layout.addWidget(imagelabel)

        self.w.setLayout(layout)

    def show(self):
        '''表示を行う'''
        self.w.exec_()

class WinHelp4(QWidget):
    def __init__(self, parent=None):
        '''ウィンドウ初期設定を行う'''
        self.w = QDialog(parent)
        self.w.setWindowTitle("手順4")
        self.w.setGeometry(400, 400, 200, 300)

        label = QLabel(self.w)
        label.setText('「戻る」ボタンを押し,「X」ボタンを押すことで起動終了することができます')
        label.setFont(QFont("Arial", 14, QFont.Black))

        label2 = QLabel(self.w)
        label2.setText('「X」ボタンを押して正常終了すると, "YY-mm-dd_起動終了時刻(1200等).t2pecf"ファイルが作成されます\nこれを保管して出席確認システムに読み込ませましょう')
        label2.setFont(QFont("Arial", 14, QFont.Black))
        # ファイルを読み込み
        image = QImage('style/protocol4.gif')
        imagelabel = QLabel()
        # ラベルに読み込んだ画像を反映
        imagelabel.setPixmap(QPixmap.fromImage(image))
        # スケールは1.0
        imagelabel.scaleFactor = 0.3


        exit = QPushButton(self.w)
        exit.setGeometry(0, 0, 1, 1)
        exit.setShortcut("Ctrl+c")
        exit.setShortcut("c")
        exit.clicked.connect(self.w.close)

        layout = QVBoxLayout()
        layout.addWidget(label)
        layout.addWidget(label2)
        layout.addWidget(imagelabel)

        self.w.setLayout(layout)

    def show(self):
        '''表示を行う'''
        self.w.exec_()