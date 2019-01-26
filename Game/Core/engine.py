import xml.etree.ElementTree as ET
from Game.Characters import characters
from Game.Characters import classes 
from Game.Core import room
from Game.Util import util 
from Game.Texts import messages

class BookHeroText:
    def __init__(self, game_file):
        self.__version = "0.0.3"
        self.__game_file = game_file 
        self.__engine_running = True
        self.__cur_room = "#GameStart"
        self.__engine_name = "Python Book Hero Engine"
        self.__engine_author = "David Montandon"
        self.__messages = messages.Messages() 
        self.__classes = classes.ClassHolder()

    def __engine_start_message(self):
        print("\n\n\n============================================")
        print(self.__engine_name ,  self.__version , "by" , self.__engine_author , "- STARTED")
        if(self.__game_file=="sample.xml"):
            print("\nYou can also run you own StoryFile using the command line : python bookhero.py yourworld.xml")
        print("============================================")

    def __engine_stop_message(self):
        print("\n\n\n============================================")
        print(self.__engine_name ,  self.__version , "by" , self.__engine_author , "- STOPPED")
        print("============================================")

    def __load_xml_tree(self):
        with open(self.__game_file, "r") as xml_file:
            self.tree = ET.parse(xml_file)
        
        self.root = self.tree.getroot()

    def engine_start(self):
        choice = "" 
        self.__engine_start_message() 
        self.__load_xml_tree() 
        self.__load_messages()
        self.__load_classes()

        while(self.__engine_running):
            next_room = ""
            room = self.__load_room(self.__cur_room)
            room.print_text_room(self.__messages.getRandomText("actionMove"))

            while(next_room == ""):
                choice = room.get_user_choice()
                next_room = room.check_choice(choice)
                if( next_room == ""):
                    print("Invalid choice.")

            if(next_room=="#Quit"):
                self.__engine_running = False
            elif(next_room=="#GameOver"):
                self.__engine_running = False

            self.__cur_room = next_room

        self.__engine_stop_message() 

    def __load_classes(self):
        self.__classes.initFromXML(self.root.findall("./classes/class"))

    def __load_messages(self):
        for msg in self.root.findall("./messages/message"):
            self.__messages.add(msg.attrib["type"], msg.text)

    def __load_room(self, room_name):
        room_xml = self.root.find("./rooms/room[@id='" + room_name + "']")
        r = room.Room(room_xml)     
        room.ScreenLoader.load_from_xml(room_xml)               
        return r
