from Game.Util import util 
from Game.Screens import choice

class Screen:
    def __init__(self):
        self._choices = []
        self._items = []
        self._random_action_message = True 
        self._desc = ""

    def _load_xml(self, xml):
        self._id = xml.attrib["id"]

        for v in xml.iter(): 
            if(v.tag == "choice"):
                self._add_choice(v.text, v.attrib["next"])
            elif (v.tag == "description"):
                self._set_desc(v.text)
            elif (v.tag == "type"):
                self._set_type(v.text)
            elif( v.tag == "randomActionMessage"):
                self._random_action_message = util.BooleanFromString.get_boolean(v.text) 

    def _add_choice(self, choice_text, choice_next_room):
        self._choices.append(choice.Choice(str(len(self._choices) + 1),choice_text, choice_next_room))

    def has_item(self):
        return len(self._items) > 0

    def _set_desc(self, desc):
        self._desc = desc

    def _set_type(self, type):
        self._type = type

    def has_random_message(self):
        return self._random_action_message

    def get_desc(self):
        return self._desc

    def get_choices(self):
        return self._choices

    def check_choice(self, choice):
        for c in self._choices:
            if( str(choice) == c.code ):
                return c.next
        return "" 



