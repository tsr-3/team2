'''
入力：ICカードからIDm，外部入力(ファイル入力側)から学生の情報を集めたオブジェクト(学籍番号と名前が対応していれば可)
出力：入力されたIDmに対応した学生の名前と学籍番号を返す
説明：読み取ったIDmから履修者を識別し，履修者リストに存在する場合はそれに対応する学生の名前と学籍番号を返す
    もし履修者リストに該当者が居ない場合は警告文を返す
'''

from types import LambdaType

def comp(IDm:str, students_list:list):
    studentData = []
    warning_text = "あなたは履修者ではありません。退室してください。"
    for i in range(len(students_list)):#リストをfor文で回す
        if IDm==students_list[i]['IDm']:#if文でIDmとリストのIDmを比較
            studentData.append(students_list[i]['名前'])
            studentData.append(students_list[i]['学籍番号'])
            return studentData
    if i == len(students_list) and studentData == []:
        return warning_text