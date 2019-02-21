import xml.etree.ElementTree as ET
import os
from Game.Characters import characters
from Game.Characters import classes 
from Game.Util import util 
from Game.Core import instance
from Game.Screens import screnloader

class CoreEngine:
    def __init__(self, story_path, story_file):
        instance.Instance()
        self.__version = "0.1.1"
        self.__story_path = story_path
        self.__set_cur_game_file(story_file)
        self.__save_file = os.path.join(story_path, "save.bin")
        self.__engine_running = True
        self.__engine_name = "Python Hero Book Core"
        self.__engine_author = "David Montandon"
        self.__active_room = None

    def get_engine_info(self):
        engine_info = {}
        engine_info["name"] = self.__engine_name
        engine_info["version"] = self.__version
        engine_info["author"] = self.__engine_author
        return engine_info

    def __set_cur_game_file(self, file):
        mem = instance.Instance.get_instance()
        mem.set_cur_screen_file(file)
        self.__game_file = os.path.join(self.__story_path, file)

    def __load_xml_tree(self):
        self.root = self.__get_xml_root(self.__game_file)

    def __get_complete_file_path(self, file_name):
        print(os.path.join(self.__story_path, file_name))
        return os.path.join(self.__story_path, file_name)

    def __get_xml_root(self, file_name):
        with open(file_name, "r") as xml_file:
            tree =  ET.parse(xml_file)
        return tree.getroot() 

    def init_game(self):
        mem = instance.Instance.get_instance()
        self.__load_xml_tree() 
        self.__load_files()
        self.__init_party()

        mem.set_save_file(self.__save_file)
        mem.set_cur_screen(mem.get_config('GameStart'))

    def has_save_file(self):
        from pathlib import Path
        save_file = Path(self.__save_file)
        if save_file.exists():
            return True

        return False

    def load_game(self):
        if self.has_save_file():
            mem = instance.Instance.get_instance()
            mem.load()
            self.__set_cur_game_file(mem.get_cur_screen_file())
            self.__load_xml_tree() 

    def set_choice(self, m):
        r = {}
        r["continue"] = True 
        r["msg"] = ""

        mem = instance.Instance.get_instance()
        next_screen = m["next"]

        if(next_screen=="#Save"):
                mem.save()
                r["msg"] = "Game saved" 
        elif(next_screen=="#Quit"):
                r["continue"] = False 
                r["msg"] = "You left the game" 
        elif(next_screen=="#GameOver"):
                r["continue"] = False 
                r["msg"] = "You are dead."
        else:

            if(m["type"] == "move"):
                mem.set_visited_room(mem.get_cur_screen())
                mem.set_cur_screen(next_screen)
                
                if not m["file"]is None:
                    self.__set_cur_game_file(m["file"])
                    self.__load_xml_tree()
            elif(m["type"] == "classselector"):
                self.__active_room.set_class(m["next"])
                r["msg"] = "Class changed"

        return r

    def get_screen(self):
        mem = instance.Instance.get_instance()
        if(self.__active_room == None or mem.get_cur_screen() != self.__active_room.get_id()):
            room = self.__load_room(mem.get_cur_screen())
            self.__active_room = room
        else:
            room = self.__active_room
        return room.get_datas()

    def __init_party(self):
        mem = instance.Instance.get_instance()
        mem.add_party( mem.get_config("MainParty") )
        mem.add_character( mem.get_config("MainCharacter") )
        mem.add_character_to_party( mem.get_config("MainParty"), mem.get_config("MainCharacter") )

    def __load_files(self):
        """ Load game contents inside the instance singleton

        Parameters
        ----------
        None

        Returns
        -------
        None
        """ 
        class_load = False 
        message_load = False 
        config_load = False 

        for f in self.root.findall("./files/file"):
            for v in f.iter(): 
                if(v.tag == "file"):
                    data_type = v.attrib["type"]
                    if(data_type == "classes"):
                        class_load = True
                        self.__load_classes(self.__get_xml_root(self.__get_complete_file_path(v.text)))
                    elif(data_type == "messages"):
                        message_load = True
                        self.__load_messages(self.__get_xml_root(self.__get_complete_file_path(v.text)))
                    elif(data_type == "configs"):
                        config_load = True
                        self.__load_config(self.__get_xml_root(self.__get_complete_file_path(v.text)))


        if(not message_load):
            self.__load_messages(self.root)
    
        if(not class_load):
            self.__load_classes(self.root)

        if(not config_load):
            self.__load_config(self.root)

    def __load_config(self, root):
        mem = instance.Instance.get_instance()
        mem.init_config(root.findall("./configs/config"))

    def __load_classes(self, root):
        mem = instance.Instance.get_instance()
        mem.class_holder.init_from_xml(root.findall("./classes/class"))

    def __load_messages(self, root):
        mem = instance.Instance.get_instance()
        for msg in root.findall("./messages/message"):
            mem.message_holder.add(msg.attrib["type"], msg.text)

    def __load_room(self, room_name):
        room_xml = self.root.find("./screens/screen[@id='" + room_name + "']")
        s = screnloader.ScreenLoader.load_from_xml(room_xml)       
        return s
