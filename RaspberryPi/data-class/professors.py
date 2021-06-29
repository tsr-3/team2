
class Professors:

    _professors:list = None

    # Professors() と呼び出したとき
    #   self._professorsにNoneを設定する
    # Professors(value) と呼び出したとき
    #   self._professorsにvalueを設定する
    #   valueリストの各データにid, name, yomi, sex, lectのキーが存在することをチェックし、一つでもキーが存在しなかったらExceptionを投げる
    def __init__(self, value:list = None):
        pass

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

    @property
    def count(self):
        pass
    # 教員データの数を返す
    @count.getter
    def count(self):
        pass

    @property
    def data(self):
        pass
    # 教員データのリストを返す
    @data.getter
    def data(self):
        pass
    # self._professorsにvalueを設定する、同時にコンストラクタで行ったキーのチェックも行う
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
