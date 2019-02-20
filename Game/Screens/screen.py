from Game.Util import util 
from Game.Screens import choice
from Game.Texts import transform

class Screen:
    def __init__(self):
        self._choices = []
        self._items = []
        self._desc = ""
        self._random_action_message = True 
        self._center_description = True

    def __load_xml(self, xml):
        from Game.Core import instance
        mem = instance.Instance.get_instance() 

        self._id = xml.attrib["id"]

        for v in xml.iter(): 
            if(v.tag == "choice"):
                if("ifnot" in v.attrib):
                    if not mem.check_if_not(v.attrib["ifnot"]):
                        continue

                if("if" in v.attrib):
                    if not mem.check_if(v.attrib["if"]):
                        continue

                self.__add_choice(v.text, v.attrib["next"])
            elif (v.tag == "description"):
                self.__set_desc(v.text)

                if("center" in v.attrib):
                    self._center_description = util.BooleanFromString.get_boolean(v.attrib["center"])

            elif (v.tag == "type"):
                self.__set_type(v.text)
            elif( v.tag == "randomActionMessage"):
                self._random_action_message = util.BooleanFromString.get_boolean(v.text)
            elif (v.tag == "flag"):
                mem.add_flag( v.text )

    def get_id(self):
        return self._id

    def get_datas(self):
        from Game.Core import instance 
        mem = instance.Instance.get_instance() 

        data = {}
        data["type"] = "move"
        data["text"] = []
        data["text"].append(transform.Transform.get_transformated_text(self.get_desc()))
        if(self.has_random_message()):
            data["text"].append(mem.message_holder.getRandomText("actionMove"))
        data["choices"] = self.get_choices()

        return data

    def __add_choice(self, choice_text, choice_next_room):
        self._choices.append(choice.Choice(str(len(self._choices) + 1),choice_text, choice_next_room))

    def has_item(self):
        return len(self._items) > 0

    def __set_desc(self, desc):
        self._desc = desc

    def __set_type(self, type):
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
                return c.get_screen_map()
                
        m = {}
        m["next"] = ""
        return m



