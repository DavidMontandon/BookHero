import xml.etree.ElementTree as ET
import os
from Game.Characters import characters
from Game.Characters import classes 
from Game.Util import util 
from Game.Core import instance
from Game.Screens import screnloader

class BookHeroText:
    def __init__(self, story_path, story_file):
        instance.Instance()
        self.__version = "0.0.10"
        self.__story_path = story_path
        self.__set_cur_game_file(story_file)
        self.__save_file = os.path.join(story_path, "save.bin")
        self.__engine_running = True
        self.__engine_name = "Python Book Hero Engine"
        self.__engine_author = "David Montandon"

    def __engine_start_message(self):

        util.Console.clear()
        print("\n\n")
        print("=======================================================================================================================")
        print(self.__engine_name ,  self.__version , "by" , self.__engine_author , "- STARTED")
        if(self.__game_file=="sample.xml"):
            print("\nYou can also run you own StoryFile using the command line : python bookhero.py yourworld.xml")
        print("=======================================================================================================================\n\n")
        print("For more informations, please visit : https://github.com/DavidMontandon/BookHero")
        print("\n")
        input("Press Enter to continue...")

    def __engine_stop_message(self):
        util.Console.clear()
        print("\n\n")
        print("=======================================================================================================================")
        print(self.__engine_name ,  self.__version , "by" , self.__engine_author , "- STOPPED")
        print("=======================================================================================================================\n\n")
        print("For more informations, please visit : https://github.com/DavidMontandon/BookHero")
        print("\n")

    def __set_cur_game_file(self, file):
        mem = instance.Instance.get_instance()
        mem.set_cur_screen_file(file)
        self.__game_file = os.path.join(self.__story_path, file)

    def __load_xml_tree(self):
        with open(self.__game_file, "r") as xml_file:
            self.tree = ET.parse(xml_file)
        
        self.root = self.tree.getroot()

    def engine_start(self):
        mem = instance.Instance.get_instance()
        self.__engine_start_message() 
        self.__load_xml_tree() 
        self.__load_messages()
        self.__load_classes()
        self.__load_config()
        self.__init_party()

        mem.set_save_file(self.__save_file)
        mem.set_cur_screen(mem.get_config('GameStart'))

        from pathlib import Path
        save_file = Path(self.__save_file)
        if save_file.exists():
            mem.load()
            self.__set_cur_game_file(mem.get_cur_screen_file())
            self.__load_xml_tree() 

        while(self.__engine_running):
            self.__this_room = mem.get_cur_screen()
            self.__next_room = ""
            room = self.__load_room(mem.get_cur_screen())

            self.__screen_print( room )

            cur_room = mem.get_cur_screen()

            if(cur_room=="#Save"):
                mem.set_cur_screen(self.__this_room)
                mem.save()
            elif(cur_room=="#Quit"):
                self.__engine_running = False
            elif(cur_room=="#GameOver"):
                self.__engine_running = False

        self.__engine_stop_message() 

    def __init_party(self):
        mem = instance.Instance.get_instance()
        mem.add_party( mem.get_config("MainParty") )
        mem.add_character( mem.get_config("MainCharacter") )
        mem.add_character_to_party( mem.get_config("MainParty"), mem.get_config("MainCharacter") )

    def __screen_print(self, load_screen):
        mem = instance.Instance.get_instance() 
        util.Console.clear()

        print("=======================================================================================================================")
        print(self.__engine_name ,  self.__version , "by" , self.__engine_author )
        print("=======================================================================================================================\n")

        m = load_screen.print_text()

        next_screen = m["next"]

        mem.set_visited_room(mem.get_cur_screen())
        
        if not m["file"]is None:
            self.__set_cur_game_file(m["file"])
            self.__load_xml_tree()

        mem.set_cur_screen(next_screen)

    def __load_config(self):
        mem = instance.Instance.get_instance()
        mem.init_config(self.root.findall("./configs/config"))

    def __load_classes(self):
        mem = instance.Instance.get_instance()
        mem.class_holder.init_from_xml(self.root.findall("./classes/class"))

    def __load_messages(self):
        mem = instance.Instance.get_instance()
        for msg in self.root.findall("./messages/message"):
            mem.message_holder.add(msg.attrib["type"], msg.text)

    def __load_room(self, room_name):
        room_xml = self.root.find("./screens/screen[@id='" + room_name + "']")
        s = screnloader.ScreenLoader.load_from_xml(room_xml)       
        return s
