class BooleanFromString:
    @staticmethod
    def get_boolean(v):
        try:
            if(v == "true" or v == "True"):
                return True
            else:
                return False
        except:
                return False 

class ClearConsole:
    @staticmethod
    def clear():
        import os
        import platform

        if(platform.system()=="Windows"):
            os.system('cls')
        elif(platform.system()=="Linux"):
            os.system('clear')
