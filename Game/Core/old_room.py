from Game.Util import util 

class VisitedScreenHolder:
    def __init__(self):
        self.__visited_screen = {}

    def get_visited_screen(self, id):
        r = self.__visited_screen.get(id)
        if(r == None):
            r = _VisitedScreen(id)
            self.__visited_screen[id] = r
        return r 

    def set_visited_screen(self, id):
        r = self.get_visited_screen(id)
        r._set_visited()

class _VisitedScreen:
    def __init__(self, id):
        self.__items = []
        self.__visitied = False 

    def _set_visited(self):        
        self.__visitied = True  

    def get_items(self):
        return self.__items 

    def get_visited(self):
        return self.__visitied

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




        
class Room:
    def __init__(self, source):
        self.__choices = [] 
        self.__init_from_xml(source)
        self.__add_default_choices()

    def __init_from_xml(self, xml):
        from Game.Core import instance

        self.id = xml.attrib["id"]

        mem = instance.Instance.get_instance()
        visited_screen = mem.screens_holder.get_visited_screen(self.id)

        self.__random_action_message = True 

        if 'name' in xml.attrib:     
            self.name = xml.attrib["name"] 
        else:
            self.name = xml.attrib["id"] 

        if 'type' in xml.attrib:     
            self.type = xml.attrib["type"] 
        else:
            self.type = "Room" 

        for v in xml.iter(): 
            if(v.tag == "choice"):
                self.__add_choice(v.text, v.attrib["next"])
            elif (v.tag == "description"):
                self.__set_desc(v.text)
            elif (v.tag == "type"):
                self.__set_type(v.text)
            elif( v.tag == "randomActionMessage"):
                self.__random_action_message = util.BooleanFromString.get_boolean(v.text) 

        #screen has been visited already
        if(visited_screen.get_visited()):
            print("Already visited room")
            

    def __set_desc(self, desc):
        self.__desc = desc

    def __set_type(self, type):
        self.type = type

    def __add_choice(self, choice_text, choice_next_room):
        self.__choices.append(Choice(str(len(self.__choices) + 1),choice_text, choice_next_room))

    def __add_default_choices(self):
        self.__choices.append(Choice("X","Quit the game WITHOUT saving","#Quit"))

    def __print_desc(self):
        print(self.__desc)

    def __print_type(self):
        print("Type:" , self.type)

    def __print_choices(self):
        for c in self.__choices:
            print(c.code, " : ", c.text)

    def check_choice(self, choice):
        for c in self.__choices:
            if( str(choice) == c.code ):
                return c.next
        return "" 

    def has_random_message(self):
        return self.__random_action_message

    def get_desc(self):
        return self.__desc

    def get_choices(self):
        return self.__choices
