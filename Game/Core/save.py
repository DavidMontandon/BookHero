class SaveLoadMananger:
    def __init__(self, file_name):
        self.__file_name = file_name

    def load(self):
        f = open( self.__file_name,"rb")
        f.close()
        return

    def save(self):
        f = open( self.__file_name,"wb")
        f.close()
        return 

