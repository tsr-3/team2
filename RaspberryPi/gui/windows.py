'''
製作者:B21P036
動作:状況に応じたWindowを生成する(予定)のプログラム

関数
class Start
    def attend: 欠席か出席かを判定する部分

class App
    def intiUI: 特に使い道がない
    def attendUI: 関数attendに用いている基礎UI部分

説明
他のプログラムへこのプログラムをimportしても画面の更新が行われない(windowが閉じるまで操作が帰らないから)
ので下の
import timegetのように このプログラムへimportすればいいのかも
スレッドのやり方を教えろください
'''

import sys
from PyQt5.QtCore import QTimer
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import datetime
import timeget

style = '''
QMainWindow{
    background-color: pink;
    color: #0f0;
}
QLabel{
    color: green;
    font-size: 50pt
}
'''

style2 = '''
QMainWindow{
    background-color: green;
    color: #0f0;
}
QLabel{
    color: red;
    font-size: 50pt
}
'''
i = 0


class App(QMainWindow):
    '''Formの作成'''

    def initUI(self):
        '''要らないやつ'''
        self.setWindowTitle("InitUI")
        self.setGeometry(100, 100, 400, 400)

        self.label = QLabel("Python", self)
        self.label.move(50,50)

        self.label2 = QLabel("PyQt5", self)
        self.label2.move(100,100)

        self.label3 = QLabel("Examples", self)
        self.label3.move(150,150)

        self.label4 = QLabel("pytonspot.com", self)
        self.label4.move(200,200)


    def attendUI(self):
        '''出席/欠席を表示するやつの元'''
        self.setWindowTitle("Attend")
        self.setGeometry(100, 100, 400, 400)

        self.label = QLabel("Python", self)
        self.label.setGeometry(50,50,400,400)

class Start():
    '''他プログラムに出張する所'''
    def attend(self):
        '''出席/遅刻を判別する所'''
        app = QApplication(sys.argv)
        form = App()
        form.attendUI()
        app.setStyleSheet(style2)
        # form.show()
        form.showFullScreen()

        # なんかここが滅茶苦茶汚い
        def pudate():
            global i
            if timeget.test():
                form.label.setText("出席！")
                app.setStyleSheet(style)
            else:
                form.label.setText("遅刻！")
                app.setStyleSheet(style2)
            i += 1
            print(i)

        timer = QTimer()
        timer.timeout.connect(pudate)
        timer.start(1000)

        sys.exit(app.exec_())

if __name__ == '__main__':
    win = Start()
    win.attend()