#データのいんぽとえくぽがほしい



import sys
from PyQt5.QtCore import QThread, QTimer
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import datetime
import threading
import timeget



def tehon():
    app = QApplication([])
    window = QWidget()
    layout = QVBoxLayout()
    layout.addWidget(QPushButton('Top'))
    layout.addWidget(QPushButton('Bottom'))
    window.setLayout(layout)
    window.showFullScreen()
    app.exec_()

# class WinMake():
class MenuUI(QMainWindow):
    # def menuUI(self):
    def __init__(self, parent=None):
        super(MenuUI, self).__init__(parent)
        # self.setStyleSheet(style)
        css = ""
        with open('style.qss') as f:
            css = f.read()
        print(css)
        app.setStyleSheet(css)

        # フルスクリーンの大きさ
        height_c = int(app.desktop().height() / 2.0)
        width_c = int(app.desktop().width() / 2.0)

        # 窓の設定
        self.setGeometry(0, 0, width_c * 2, height_c * 2 - 100) # 位置

        # メニューバーの設定
        bar = self.menuBar()
        file = bar.addMenu("ファイル")
        export = file.addMenu("えくすぽーと")
        inport = file.addMenu("いんぽーと")
        edit = bar.addMenu("保存")
        view = bar.addMenu("A")
        search = bar.addMenu("B")
        tool = bar.addMenu("C")
        tool2 = bar.addMenu("D")
        hello = bar.addMenu("Hello")

        # ボタンの設定
        exitbt = QPushButton("X", self)
        exitbt.setToolTip("このウィンドウを閉じます")
        # exitbt.setShortcut("Ctrl+c") #ショートカットキー
        exitbt.setShortcut("c")
        exitbt.setGeometry(int(width_c * 0.2), int(height_c * 0.2), 50, 50)
        exitbt.clicked.connect(self.close)

        attendbt = QPushButton("出席をとる", self)
        attendbt.setToolTip("出席をとる画面を表示します")
        attendbt.setShortcut("s")
        attendbt.setGeometry(width_c, height_c, 100, 100)
        attendbt.clicked.connect(self.sub)

        self.show()
        app.exec_()

    def sub(self):
        self.subwin = AttendUI()
        # self.subwin.show()

# class AttendUI(QWidget):
class AttendUI(QMainWindow):

    # def attendUI(self):
    def __init__(self, parent=None):
    # def AttendUI(self, parent=None):
        super(AttendUI, self).__init__(parent)

        '''出席と遅刻を司るUI'''
        t = threading.Thread(target=self)
        # self.setStyleSheet(style2)
        css = ""
        with open('style.qss') as f:
            css = f.read()
        print(css)
        app.setStyleSheet(css)

        # フルスクリーンの大きさ
        height_c = int(app.desktop().height() / 2.0)
        width_c = int(app.desktop().width() / 2.0)

        # LaBeLの設定
        labelA = QLabel("出席を判別するよ", self)
        labelB = QLabel("IDを出力するよ", self)
        labelA.setGeometry(width_c - int(width_c * 0.2), height_c - 300, width_c * 2, 200)
        labelB.setGeometry(width_c - int(width_c * 0.2), height_c, width_c * 2, 200)

        # ボタンの設定
        exitbt = QPushButton("X", self)
        exitbt.setToolTip("このウィンドウを閉じます")
        # exitbt.setShortcut("Ctrl+c") #ショートカットキー
        exitbt.setShortcut("c")
        exitbt.setGeometry(int(width_c * 0.2), int(height_c * 0.2), 50, 50)
        exitbt.clicked.connect(self.close)

        def update():
            time = timeget
            if time.test():
                labelA.setText("出席")
                labelB.setText("ID出るはず")
            else:
                labelA.setText("遅刻")
                labelB.setText("ID出るはず")

        timer = QTimer()
        timer.timeout.connect(update)
        timer.start(1000)
        self.showFullScreen()
        self.show()
        app.exec_() #これを付けてると このclass単体では動作する

if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = MenuUI()
    # subwin = AttendUI()
    # t = threading.Thread(target= win)
    # sys.exit(app.exec_())

