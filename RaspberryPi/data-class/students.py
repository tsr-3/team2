# coding :utf-8

class Students:
    _students: list = None
    # student
    # - id
    # - name
    # - yomi
    # - sex
    # - idm

    def __init__(self, students:list = None): # constructor
        if students is None:
            return None
        self.data = students

    def __getitem__(self, item):
        if type(item) == int:
            if len(self._students) <= item:
                return None
            return self._students[item]
        elif type(item) == str:
            data:bool = False
            for val in self._students:
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
            if len(self._students) <= item:
                return False
            self._students[item] = value
        else:
            return False

    @property
    def count(self):
        pass
    @count.getter
    def count(self):
        return len(self._students)

    @property
    def data(self):
        pass
    @data.setter
    def data(self, value: list):
        for val in value:
            if 'id' not in val or 'name' not in val or 'yomi' not in val or 'sex' not in val or 'idm' not in val:
                raise BaseException('invalid value type of "student"', val)
        self._students = value
    @data.getter
    def data(self):
        return self._students

    def find(self, cond:dict):
        KEYS = ['id', 'name', 'yomi', 'sex', 'idm']
        subset:list = self._students
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
        if self._students == None:
            return True
        return False

if __name__ == '__main__':
    instance = Students([{"id":"S001","name":"相道森","yomi":"あいどうしん","sex":"男","idm":"012E44A7A5187429"},{"id":"S002","name":"揚村巴絵","yomi":"あげむらともえ","sex":"女","idm":"012E44A7A518527D"},{"id":"S003","name":"浅井礼子","yomi":"あさいれいこ","sex":"女","idm":"012E44A7A5152B9F"},{"id":"S004","name":"荒松晴一","yomi":"あらまつせいいち","sex":"男","idm":"012E44A7A518807A"}])
    print(instance.empty)
    print(instance[3])
    instance[3] = {"id":"S100","name":"渡利雄祐","yomi":"わたりゆうすけ","sex":"男","idm":"012E44A7A5112853"}
    print(instance[3])
    print(instance['S002'])
    print(instance.find({'id':'S002'}))
    print(instance.find({'name':'渡利雄祐'}))
    print(instance.find({'sex':'男'}))

    # instance.data = [{'id':'', 'name':'', 'yomi':'', 'idm':''}] # error test
