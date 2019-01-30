from Game.Characters import characters
from Game.Characters import classes
from Game.Texts import messages
from Game.Core import config
from Game.Screens import visit 
from Game.Core import flag

class Instance:
    __instance = None
    character_holder = characters.CharacterHolder() 
    class_holder = classes.ClassHolder()
    message_holder = messages.Messages() 
    screens_holder = visit.VisitedScreenHolder()  
    config_holder = config.ConfigHolder()
    __flag_holder = flag.FlagHolder()

    @staticmethod
    def get_instance():
        if Instance.__instance == None:
            Instance()
        return Instance.__instance

    def __init__(self):
        if Instance.__instance != None:
            raise Exception("This class is a singleton!")
        else:
            Instance.__instance = self

    @staticmethod
    def add_flag(text):
        return Instance.__flag_holder.add(text)

    @staticmethod
    def has_flag(text):
        return Instance.__flag_holder.has_flag(text)

    @staticmethod
    def check_if(text):
        b = True

        values = text.split(",")
        for v in values:
            dec = v.split(":")
            if(dec[0] == "flag"):
                b = b and Instance.has_flag(dec[1])

        return b

    @staticmethod
    def check_if_not(text):
        return not Instance.check_if(text)
    
