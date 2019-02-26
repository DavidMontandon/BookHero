from Game.Screens import screen
from Game.Screens import choice
from Game.Util import util 
from Game.Texts import transform

class ClassSelectorScreen(screen.Screen):
    def __init__(self):
        screen.Screen.__init__(self)
        self.__class_choices = []
        self.__confirm = ""
        self.__random_class_message = True 
        self.__character_id = None
        self.__cur_action = "classselector"
        self._item_droppable = False 

    def load_xml(self, xml):
        from Game.Core import instance

        mem = instance.Instance.get_instance() 
        screen.Screen._Screen__load_xml(self, xml)
        self._add_default_choices()
        self.__set_character_id(xml.attrib["characterId"])

        for v in xml.iter(): 
            if(v.tag == "confirm"):
                self.__set_confirm(v.text)
            elif( v.tag == "randomSelectMessage"):
                self.__random_class_message = util.BooleanFromString.get_boolean(v.text)
            elif( v.tag == "next"):
                self.__random_class_message = util.BooleanFromString.get_boolean(v.text)
                
        for c in mem.class_holder.get_selectables_classes():
            self.__add_choice_class(c.name, c.id)


    def __set_character_id(self, character_id):
        self.__character_id = character_id 

    def has_random_class_message(self):
        return self.__random_class_message

    def __set_confirm(self, text):
        self.__confirm = text 

    def _add_default_choices(self):
        self._choices.append(choice.Choice("X","Quit the game WITHOUT saving","#Quit"))

    def __add_choice(self, choice_text, choice_next_room):
        self._choices.append(choice.Choice(str(len(self._choices) + 1),choice_text, choice_next_room))

    def __add_choice_class(self, class_text, class_id):
        self.__class_choices.append(choice.Choice(str(len(self.__class_choices) + 1),class_text, class_id))

    def __check_class_choice(self, choice):
        for c in self.__class_choices:
            if( str(choice) == c.code ):
                return c.get_continue()
                
        return ""

    def get_datas(self):
        from Game.Core import instance 
        mem = instance.Instance.get_instance() 

        if(self.__cur_action == "classselector"):
            data = {}
            data["type"] = "classselector"
            data["text"] = []
            data["text"].append(transform.Transform.get_transformated_text(self.get_desc()))
            if(self.has_random_message()):
                data["text"].append(mem.message_holder.getRandomText("actionSelectClass"))
            data["choices"] = self.__class_choices
        else:
            data = {}
            data["type"] = "move"
            data["text"] = []
            data["text"].append(transform.Transform.get_transformated_text(self.__confirm))
            if(self.has_random_message()):
                data["text"].append(mem.message_holder.getRandomText("actionMove"))
            data["choices"] = self.get_choices()

        return data

    def set_class(self, class_id):
        from Game.Core import instance
        mem = instance.Instance.get_instance() 
        mem.set_class(self.__character_id, class_id)
        self.__cur_action = "move"

