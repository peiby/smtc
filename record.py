import os, glob, shutil


local_path = 'D:/python/project/smtc'
data_path = 'E:/other/data race/topic4'


class User_path(object):
    def __init__(self):
        pass

    @staticmethod
    def csv_txt():
        path = f'{local_path}/_csv/record-filt.txt'
        return path
        pass

    pass


class Document(object):
    def __init__(self):
        pass

    # 检验是否有该文件夹, 没有则创建
    @staticmethod
    def mkdir(path):
        isExists = os.path.exists(path)
        if not isExists:
            os.makedirs(path)
        return path
        pass

    pass
