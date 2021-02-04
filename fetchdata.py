import json


class Stu:
    def __init__(self):
        self.data = None

    def connect(self, file1):
        with open(file1) as f1:
            self.__data = json.load(f1)

    def retrivedata(self, sname):
        for s in self.__data['stu']:
            if s['name'] == sname:
                return s
