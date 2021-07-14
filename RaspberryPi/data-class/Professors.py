# coding :utf-8

class Professors:

    # クラス変数(不変)
    KEYS = ['id','name','yomi','sex','lect']
    # クラス変数とインスタンス変数について理解しましょう
    # professors (variable name : type)
    # - id : str
    # - name : str
    # - yomi : str
    # - sex : str
    # - lect : object (list or dict or ...)
    # [{"id":"P001","name":"秋場紀明","yomi":"秋葉典明","sex":"男","lect":[応用数学,数学演習]},{},....{}] 的な？

    # コンストラクタの仕様(編集者注：どうやら言語仕様上コンストラクタではreturn Noneしか出来ないらしい)
    # Professors() と呼び出したとき
    #   self._professorsにNoneを設定する
    # Professors(item) と呼び出したとき
    #   valueリストの各データにid, name, yomi, sex, lectのキーが存在することをチェック
    #   問題が無ければself._professorsにvalueを設定する
    def __init__(self, professors:list = None): # constructor
        self._professors = []
        if professors is None:
            self._professors = None
        else:
            for i in range(len(professors)):
                print(f'{professors[i]}について')
                '''
                if 'id' not in professors[i]:
                    print('idがない')
                elif 'name' not in professors[i]:
                    print('nameがない')
                elif 'yomi' not in professors[i]:
                    print('yomiがない')
                elif 'sex' not in professors[i]:
                    print('sexがない')
                elif 'lect' not in professors[i]:
                    print('lectがない')
                else:
                    self._professors.append(professors[i])
            if self._professors == []:
                self._professors = None
                '''
            # 大量のif文の代替案
                key_is_not_found = False
                for j in range(len(self.KEYS)):
                    if self.KEYS[j] not in professors[i]:
                        key_is_not_found = True
                        print(f'{self.KEYS[j]}がない')
                        #raise Exception or return None
                if key_is_not_found == False:
                    self._professors.append(professors[i])
            if self._professors == []:
                self._professors = None

        # 検証済み

    # keyがintのとき
    #   self._professorsのリストのkey番目の教員データを返す
    #   self._professors[key]がリストの範囲外のとき、Noneを返す
    # keyがstrのとき
    #   キー（lect以外）がstrの教員データを返す
    #   strのキーが存在しないとき、Noneを返す
    # keyがそれ以外の時
    #   Exceptionを投げる
    def __getitem__(self, item):
        if self._professors == None: # そもそもデータが無いときは例外
            return Exception
        elif type(item) == int:
            if int(len(self._professors)) <= item:
                return None
            return self._professors[item-1] # item番目のデータが欲しいはずなので item-1
        elif type(item) == str:
            for val in self._professors:
                for key in self.KEYS:
                    if key == 'lect':
                            if val.get(key) == item:
                                print(f'{key}が{item}のデータは{val}')
                    elif val.get(key) == item:
                        print(f'{key}が{item}のデータは{val}')
                        pass
                    else:
                        continue
                if val is None:
                    return None
        else:
            return Exception
        # 検証済み

    def __setitem__(self,key,item):
        if self._professors == None:
            self._professors == []
        elif item is None:
            self._professors = None
        else:
            key_is_not_found = False
            for j in range(len(self.KEYS)):
                if self.KEYS[j] not in item:
                    key_is_not_found = True
                    print(f'{self.KEYS[j]}がない')
                    return Exception
            if key_is_not_found == False:
                self._professors.insert(key,item)

    @property
    def count(self):
        pass
    # 教員データの数を返す
    @count.getter
    def count(self):
        if self._professors == None:
            self._professors = []
        return len(self._professors)
        # 検証済み

    @property
    def data(self):
        pass
    @data.getter
    def data(self):
        return self._professors
        '''
    # self._professorsにvalueを設定する、同時にコンストラクタで行ったようなキーのチェックも行う
    @data.setter
    def data(self,item):
        self._professors = []
        if item is None:
            self._professors = None
        else:
            key_is_not_found = False
            for j in range(len(self.KEYS)):
                if self.KEYS[j] not in item:
                    key_is_not_found = True
                    print(f'{self.KEYS[j]}がない')
            if key_is_not_found == False:
                self._professors.append(item)
        if self._professors == []:
            self._professors = None
            '''
    @property
    def empty(self):
        pass
    @empty.getter
    def empty(self):
        if self._professors == None:
            return True
        return False
        # 検証済み

if __name__ == '__main__':

    # インスタンスに何も設定されていないときのテスト
    empty_instance = Professors()
    print(empty_instance.data) # 理想値 => None

    # インスタンスのデータを配布されていた教員・担当科目リスト.csvから引用
    test_instance1 = Professors(professors=
    [{"id":"P001","name":"秋場紀明","yomi":"あきばのりあき","sex":"男","lect":["応用数学","数学演習"]},
    {"id":"P002","name":"有本太志","yomi":"ありもとたいし","sex":"男","lect":["保健体育"]},
    {"id":"P003","name":"大島恵理子","yomi":"おおしまえりこ","sex":"女","lect":["心理学"]},
    {"id":"P004","name":"鬼野極","yomi":"おにのきわむ","sex":"男","lect":["プログラミング"]},
    {"id":"P005","name":"高坂信之","yomi":"こうさかのぶゆき","sex":"男","lect":["電磁気学"]},
    {"id":"P006","name":"澤井信彦","yomi":"さわいのぶひこ","sex":"男","lect":["情報ネットワーク"]},
    {"id":"P007","name":"進藤健児","yomi":"しんどうけんじ","sex":"男","lect":["システム開発演習","情報工学実習"]},
    {"id":"P008","name":"武山寛子","yomi":"たけやまひろこ","sex":"女","lect":["情報理論","アルゴリズムとデータ構造"]},
    {"id":"P009","name":"土橋健二","yomi":"つちはしけんじ","sex":"男","lect":["経済学"]},
    {"id":"P010","name":"豊崎史朗","yomi":"とよさきしろう","sex":"男","lect":["英会話"]},
    {"id":"P011","name":"西田順","yomi":"にしだじゅん","sex":"男","lect":["教養英語","科学英語"]},
    {"id":"P012","name":"古澤範人","yomi":"ふるさわのりひと","sex":"男","lect":["物理学"]},
    {"id":"P013","name":"細川靖司","yomi":"ほそかわやすし","sex":"男","lect":["コミュニケーション入門"]},
    {"id":"P014","name":"水沼勝敏","yomi":"みずぬまかつとし","sex":"男","lect":["電子回路学"]},
    {"id":"P015","name":"三谷和巳","yomi":"みつやかずみ","sex":"男","lect":["信号処理"]},
    {"id":"P016","name":"鷲見和紀","yomi":"わしみかずのり","sex":"男","lect":["文学・文化学"]}
    ])
    print(test_instance1.data) # 理想値 => 上のリストが \ﾜｰｰｰｰ/ って出てくる

    # どこかしら(すべて)に欠損があるテストデータ
    test_instance2 = Professors(professors=
    [{"name":"秋場紀明","yomi":"あきばのりあき","sex":"男","lect":["応用数学","数学演習"]},
    {"id":"P002","yomi":"ありもとたいし","sex":"男","lect":["保健体育"]},
    {"id":"P003","name":"大島恵理子","sex":"女","lect":["心理学"]},
    {"id":"P004","name":"鬼野極","yomi":"おにのきわむ","lect":["プログラミング"]},
    {"id":"P005","name":"高坂信之","yomi":"こうさかのぶゆき","sex":"男"},
    {"id":"P006","yomi":"さわいのぶひこ","sex":"男","lect":["情報ネットワーク"]},
    {"id":"P007","name":"進藤健児","sex":"男","lect":["システム開発演習","情報工学実習"]},
    {"id":"P008","name":"武山寛子","yomi":"たけやまひろこ","lect":["情報理論","アルゴリズムとデータ構造"]},
    {"id":"P009","name":"土橋健二","yomi":"つちはしけんじ","sex":"男"},
    {"id":"P010","name":"豊崎史朗","sex":"男","lect":["英会話"]},
    {"id":"P011","name":"西田順","yomi":"にしだじゅん","lect":["教養英語","科学英語"]},
    {"id":"P012","name":"古澤範人","yomi":"ふるさわのりひと","sex":"男"},
    {"id":"P013","name":"細川靖司","yomi":"ほそかわやすし","lect":["コミュニケーション入門"]},
    {"id":"P014","name":"水沼勝敏","yomi":"みずぬまかつとし","sex":"男"},
    {"id":"P015","sex":"男","lect":["信号処理"]},
    {"id":"P016","name":"鷲見和紀"}
    ])
    print(test_instance2.data) # 理想値 全てのキーに欠損がある => None 一部のキーに欠損がある => 必要充分なデータが出力
    # ここまでコンストラクタの検証(済)

    # ここからメソッドの検証
    print(empty_instance[1]) # => Exception(例外)が返ってくる

    print(test_instance1[10]) # => test_instance1の10番目が返ってくる(豊崎史郎)
    print(test_instance1[20]) # => 存在しないためNoneが返ってくる

    print(test_instance1['P001']) # => データの中身 lectの比較だけ上手く動かない
    print(test_instance1['B']) # => None

    # 検証結果 => まあまあ良いのでは？

    # ここから getter setter の検証
    print(f'教員データの数：{test_instance1.count}個') # getter => 16

    print(f'教員データのリスト\n{test_instance1.data}') # getter => データ全部
    print(f'教員データのリスト\n{test_instance2.data}') # getter => None

    print(empty_instance.empty) # getter => True
    print(test_instance1.empty) # getter => False
    print(test_instance2.empty) # getter => True

    # ここまで大きな問題なし

    # data.setterを検証のために，空のやつを使うやで
    print(f'教員データのリスト\n{empty_instance.data}') # getter => None
    I_want_to_add = {'id':'P000','name':'被験者','yomi':'おにんぎょう','sex':'不明','lect':['相対性理論応用']}
    empty_instance[empty_instance.count] = I_want_to_add
    print(empty_instance.data)



#from typing import Counter
#
#
#class Professors:
#
#    _professors:list = None
#
#    # Professors() と呼び出したとき
#    #   self._professorsにNoneを設定する
#    # Professors(item) と呼び出したとき
#    #   self._professorsにvalueを設定する
#    #   valueリストの各データにid, name, yomi, sex, lectのキーが存在することをチェックし、一つでもキーが存在しなかったらExceptionを投げる
#
#    def __init__(self, item:list = None):#コンストラクタ
#        print("do init")
#        pass
#
#        self._professors==None
#
#        if type(item) is list:
#            if item in item ('id')or('name')or('yomi')or('sex')or('lect[]'):
#                self._professors==self._professors(item)
#            print("end init")
#            return self._professors
#
#    # keyがintのとき
#    #   self._professorsのリストのkey番目の教員データを返す
#    #   self._professors[key]がリストの範囲外のとき、Noneを返す
#    # keyがstrのとき
#    #   教員IDがstrの教員データを返す
#    #   strの教員IDが存在しないとき、Noneを返す
#    # keyがそれ以外の時
#    #   Exceptionを投げる
#
#    def __getitem__(self, key):
#        print("do getitem")
#        pass
#        for key in self._professors():
#            if type(key)==int:
#                if self._professors[key]>=self._professors():
#                   return self._professors(key)
#                else:
#                    return None
#            if type(key)==str:
#                self._professors(id)==self._professors('')
#                return self._professors(id)
#            if self._professors('id')=='':
#                return None
#            else:
#                return Exception
#
#    @property
#    def count(self):
#        print("do count")
#        pass
#        counter=0
#        for key in self._professors():
#            counter+=1
#        return counter
#    # 教員データの数を返す
#    @count.getter
#    def count(self):
#        print("do count.getter")
#        pass
#        # count=Professors()
#        return count.count
#
#
#
#    @property
#    def data(self):
#        print("do data")
#        pass
#        pass
#        return self._professors()
#    # 教員データのリストを返す
#    @data.getter
#    def data(self):
#        print("do data.getter")
#        pass
#    # self._professorsにvalueを設定する、同時にコンストラクタでも行ったキーのチェックも行う
#    @data.setter
#    def dat(self, item):
#        print("do data.setter")
#        pass
#
#    @property
#    def empty(self):
#        print("do empty")
#        pass
#    # データが設定されていないかどうかを返す
#    # => データが設定されていないときにtrue
#    @empty.getter
#    def empty(self):
#        print("do empty.getter")
#        pass
#
#
#if __name__=='__main__':
#    item=['123','岡田','okada','女',[1]]
#    if item!=('id')or('name')or('yomi')or('sex')or('lect[]'):
#        print('Exception')
#
#    key=(12.5)
#    if type(key)==int:
#        print('123')
#    elif type(key)==str:
#        print('あいうえお')
#    else:
#        print('Exception')
#
#    count=Professors()
#    print(count.count)
#