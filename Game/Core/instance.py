from Game.Characters import characters
from Game.Characters import classes
from Game.Texts import messages
from Game.Core import config
from Game.Screens import visit 
from Game.Core import flag
from Game.Core import save

class Instance:
    __instance = None
    __character_holder = characters.CharacterHolder() 
    class_holder = classes.ClassHolder()
    message_holder = messages.Messages() 
    __visited_screens_holder = visit.VisitedScreenHolder()  
    __config_holder = config.ConfigHolder()
    __flag_holder = flag.FlagHolder()
    __save_load_manager = save.SaveLoadMananger("save.bin")
    __cur_screen = ""
    __cur_screen_file = ""

#INSTANCE

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
    def __str__():
        return "==== Instance Debug ====\nThis Screen : {file}:{screen}\n{flag}\n{visited}".format(
                file=Instance.get_cur_screen_file(), screen=Instance.get_cur_screen(), flag=Instance.__flag_holder,visited=Instance.__visited_screens_holder)

    @staticmethod
    def set_cur_screen(id):
        Instance.__cur_screen = id

    @staticmethod
    def get_cur_screen():
        return Instance.__cur_screen

    @staticmethod
    def set_cur_screen_file(file_name):
        Instance.__cur_screen_file = file_name

    @staticmethod
    def get_cur_screen_file():
        return Instance.__cur_screen_file

#CONFIG HOLDER
    
    @staticmethod
    def get_config(key):
        return Instance.__config_holder.get_config(key)

    @staticmethod
    def init_config(xml):
        return Instance.__config_holder.init_from_xml(xml)

#FLAG HOLDER

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

#VISITED SCREEN HOLDER

    @staticmethod
    def set_visited_room(room_id):
        Instance.__visited_screens_holder.set_visited_screen(room_id)

#CHARACTER HOLDER

    @staticmethod
    def add_character_to_party(party_id, character_id):
        Instance.__character_holder.add_character_to_party(party_id, character_id)

    @staticmethod
    def add_party(party_id):
        Instance.__character_holder.add_party(party_id, party_id)
    
    @staticmethod
    def add_character(character_id):
        Instance.__character_holder.add_character(character_id)

    @staticmethod
    def set_class(character_id, class_id):
        Instance.__character_holder.set_character_class(character_id, class_id)

    @staticmethod
    def get_character(character_id):
        return Instance.__character_holder.get_character(character_id)

#CLASS HOLDER

    @staticmethod
    def get_class(class_id):
        return Instance.class_holder.get_class(class_id)

#SAVE LOAD MANAGER

    @staticmethod
    def set_save_file(file_name):
        Instance.__save_load_manager.change_file(file_name)

    @staticmethod
    def save():
        t = (Instance.get_cur_screen(), Instance.get_cur_screen_file(), Instance.__flag_holder, Instance.__visited_screens_holder)
        Instance.__save_load_manager.save(t)
    
    @staticmethod
    def load():
        t = ("", "", Instance.__flag_holder, Instance.__visited_screens_holder)
        t = Instance.__save_load_manager.load(t)

        Instance.set_cur_screen(t[0])
        Instance.set_cur_screen_file(t[1])
        #Instance.set_cur_screen_file("sample1.xml")
        Instance.__flag_holder = t[2]
        Instance.__visited_screens_holder = t[3]