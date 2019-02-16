import pickle

class SaveLoadMananger:
    def __init__(self, file_name):
        self.__file_name = file_name

    def change_file(self, file_name):
        self.__file_name = file_name

    def load(self, template):
        f = open(self.__file_name,"rb")

        lst = list(template)
        idx = 0 

        for t in template:
            lst[idx] = pickle.load(f)
            idx += 1

        f.close()

        return lst

    def save(self, data):
        f = open( self.__file_name,"wb")

        for d in data:
            pickle.dump(d, f)

        f.close()



