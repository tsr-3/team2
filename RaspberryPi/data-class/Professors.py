from typing import Counter


class Professors:
    
    _professors:list = None

    # Professors() と呼び出したとき
    #   self._professorsにNoneを設定する
    # Professors(value) と呼び出したとき
    #   self._professorsにvalueを設定する
    #   valueリストの各データにid, name, yomi, sex, lectのキーが存在することをチェックし、一つでもキーが存在しなかったらExceptionを投げる

    def __init__(self, value:list = None):#コンストラクタ
        pass
        self._professors==None
        if type(value) is list:
            if value in value ('id')or('name')or('yomi')or('sex')or('lect[]'):
                self._professors==self._professors(value)
            return self._professors    

    # keyがintのとき
    #   self._professorsのリストのkey番目の教員データを返す
    #   self._professors[key]がリストの範囲外のとき、Noneを返す
    # keyがstrのとき
    #   教員IDがstrの教員データを返す
    #   strの教員IDが存在しないとき、Noneを返す
    # keyがそれ以外の時
    #   Exceptionを投げる
    
    def __getitem__(self, key):
        pass
        for key in self._prfessors():
            if type(key)==int:
                return self._professors(key)
                if self._professors[key]>=self._professors():
                    return None
            if type(key)==str:
                self._professors(id)==self._professors('')
                return self._professors(id)
                if self._professors('id')=='':
                    return None
            else:
                return Exception

    @property
    def count(self):
        pass
        counter=0
        for key in self._professors():
            counter+=1
        return counter
    # 教員データの数を返す
    @count.getter
    def count(self):
        pass
        count=Professors()
        return count.count
        
        

    @property
    def data(self):
        pass
        return self._professors()
    # 教員データのリストを返す
    @data.getter
    def data(self):
        pass
    # self._professorsにvalueを設定する、同時にコンストラクタでも行ったキーのチェックも行う
    @data.setter
    def data(self, value):
        pass

    @property
    def empty(self):
        pass
    # データが設定されていないかどうかを返す
    # => データが設定されていないときにtrue
    @empty.getter
    def empty(self):
        pass


if __name__=='__main__':
    value=['123','岡田','okada','女',[1]]
    if value!=('id')or('name')or('yomi')or('sex')or('lect[]'):
        print('Exception')
    
    key=(12.5)
    if type(key)==int:
        print('123')
    elif type(key)==str:
        print('あいうえお')
    else:
        print('Exception')
    
    count=Professors()
    print(count.count)


    
    


    