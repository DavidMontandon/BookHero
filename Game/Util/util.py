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

class Console:
    @staticmethod
    def clear():
        import os
        import platform
        
        if(platform.system()=="Windows"):
            os.system('cls')
        elif(platform.system()=="Linux"):
            os.system('clear')

    @staticmethod
    def center(text, cwidth=120, width=80):
        import textwrap
        import re

        s = re.sub(r'(^[ \t]+|[ \t]+(?=:))', '', text, flags=re.M)

        lines = textwrap.wrap(s, width)
        for line in lines:
            print(line.center(cwidth))
