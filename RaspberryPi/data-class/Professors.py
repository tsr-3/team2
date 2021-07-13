# coding :utf-8

class Professors:
    _professors: list = None
    # student
    # - id
    # - name
    # - yomi
    # - sex
    # - idm

    def __init__(self, professors:list = None): # constructor
        if professors is None:
            return None
        self.data = professors

    def __getitem__(self, item):
        if type(item) == int:
            if len(self._professors) <= item:
                return None
            return self._professors[item]
        elif type(item) == str:
            data:bool = False
            for val in self._professors:
                if val['id'] == item:
                    data = val
                    break
            if data is False:
                return None
            return data
        else:
            return None

    def __setitem__(self, item, value):
        if type(item) == int:
            if len(self._professors) <= item:
                return False
            self._professors[item] = value
        elif type(item) == str:
            pass
        else:
            return False

    @property
    def count(self):
        pass
    @count.getter
    def count(self):
        return len(self._professors)

    @property
    def data(self):
        pass
    @data.setter
    def data(self, value: list):
        for val in value:
            if 'id' not in val or 'name' not in val or 'yomi' not in val or 'sex' not in val or 'idm' not in val:
                raise BaseException('invalid value type of "student"', val)
        self._professors = value
    @data.getter
    def data(self):
        return self._professors

    def find(self, cond:dict):
        KEYS = ['id', 'name', 'yomi', 'sex', 'idm']
        subset:list = self._professors
        for key in KEYS:
            if not len(subset):
                return subset
            if key in cond:
                temp:list = []
                for dat in subset:
                    if dat[key] == cond[key]:
                        temp.append(dat)
                subset = temp
        return subset

    @property
    def empty(self):
        pass
    @empty.getter
    def empty(self):
        if self._professors == None:
            return True
        return False

if __name__ == '__main__':
    instance = Professors([{"id":"S001","name":"相道森","yomi":"あいどうしん","sex":"男","idm":"012E44A7A5187429"},{"id":"S002","name":"揚村巴絵","yomi":"あげむらともえ","sex":"女","idm":"012E44A7A518527D"},{"id":"S003","name":"浅井礼子","yomi":"あさいれいこ","sex":"女","idm":"012E44A7A5152B9F"},{"id":"S004","name":"荒松晴一","yomi":"あらまつせいいち","sex":"男","idm":"012E44A7A518807A"}])
    print(instance.empty)
    print(instance[3])
    instance[3] = {"id":"S100","name":"渡利雄祐","yomi":"わたりゆうすけ","sex":"男","idm":"012E44A7A5112853"}
    print(instance[3])
    print(instance['S002'])
    print(instance.find({'id':'S002'}))
    print(instance.find({'name':'渡利雄祐'}))
    print(instance.find({'sex':'男'}))

    # instance.data = [{'id':'', 'name':'', 'yomi':'', 'idm':''}] # error test


#from typing import Counter
#
#
#class Professors:
#
#    _professors:list = None
#
#    # Professors() と呼び出したとき
#    #   self._professorsにNoneを設定する
#    # Professors(value) と呼び出したとき
#    #   self._professorsにvalueを設定する
#    #   valueリストの各データにid, name, yomi, sex, lectのキーが存在することをチェックし、一つでもキーが存在しなかったらExceptionを投げる
#
#    def __init__(self, value:list = None):#コンストラクタ
#        print("do init")
#        pass
#
#        self._professors==None
#
#        if type(value) is list:
#            if value in value ('id')or('name')or('yomi')or('sex')or('lect[]'):
#                self._professors==self._professors(value)
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
#    def dat(self, value):
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
#    value=['123','岡田','okada','女',[1]]
#    if value!=('id')or('name')or('yomi')or('sex')or('lect[]'):
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