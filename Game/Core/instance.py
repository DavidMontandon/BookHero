from Game.Characters import characters
from Game.Characters import classes
from Game.Texts import messages
from Game.Core import config
from Game.Screens import visit 

class Instance:
    __instance = None
    character_holder = characters.CharacterHolder() 
    class_holder = classes.ClassHolder()
    message_holder = messages.Messages() 
    screens_holder = visit.VisitedScreenHolder()  
    config_holder = config.ConfigHolder()

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
