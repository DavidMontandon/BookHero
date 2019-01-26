from Game.Util import util 

class Choice:
    def __init__(self, code, text, next):
        self.text = text 
        self.next = next 
        self.code = code 

#Screen

#StoryBoardScreen
#BattleScreen
#ShopScreen
#ClassScreen


class Screen:
    def __init__(self):
        self.choices = []

class StoryBoardScreen(Screen):
    def __init__(self):
        Screen.__init__(self)

    def load_xml(self, xml):
        return 

class ScreenLoader:
    def load_from_xml(xml):
        screen_type = xml.attrib["type"]

        if(screen_type == "StoryBoardScreen"):
            s = StoryBoardScreen()
            s.load_xml(xml)

        return "" 

        
class Room:
    def __init__(self, source):
        self.choices = [] 

        self.__init_from_xml(source)

        self.__add_default_choices()

    def __init_from_xml(self, xml):
        self.id = xml.attrib["id"]

        if 'name' in xml.attrib:     
            self.name = xml.attrib["name"] 
        else:
            self.name = xml.attrib["id"] 

        if 'type' in xml.attrib:     
            self.type = xml.attrib["type"] 
        else:
            self.type = "Room" 

        if 'randomActionMessage' in xml.attrib:   
            self.random_action_message = util.BooleanFromString.get_boolean(xml.attrib["randomActionMessage"]) 
        else:
            self.random_action_message = True

        for v in xml.iter(): 
            if(v.tag == "choice"):
                self.__add_choice(v.text, v.attrib["next"])
            elif (v.tag == "description"):
                self.__set_desc(v.text)
            elif (v.tag == "type"):
                self.__set_type(v.text)
        
    def info(self):
        print(self.name)

    def __set_desc(self, desc):
        self.desc = desc

    def __set_type(self, type):
        self.type = type

    def __add_choice(self, choice_text, choice_next_room):
        self.choices.append(Choice(str(len(self.choices) + 1),choice_text, choice_next_room))

    def __add_default_choices(self):
        self.choices.append(Choice("X","Quit the game WITHOUT saving","#Quit"))

    def __print_desc(self):
        print(self.desc)

    def __print_type(self):
        print("Type:" , self.type)

    def __print_choices(self):
        print("Choice(s) :\n===========")
        for c in self.choices:
            print(c.code, " : ", c.text)

    def check_choice(self, choice):
        for c in self.choices:
            if( str(choice) == c.code ):
                return c.next
        return "" 

    def print_text_room(self, actionMessage):
        print("\n\n\n============================================")
        print("ROOM TYPE:" + self.type)
        self.__print_desc()
        if(self.random_action_message):
            print(actionMessage)
        print("\n")
        self.__print_choices()
        print("============================================")

    def get_user_choice(self):
        return str(input("Enter your choice : ")).upper()