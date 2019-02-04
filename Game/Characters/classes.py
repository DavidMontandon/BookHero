from Game.Util import util 

class ClassHolder:
    def __init__(self):
        self.classes = []

    def get_selectables_classes(self):
        l = []

        for c in self.classes:
            if c.selectable == True:
                l.append(c)

        return l

    def get_classes(self):
        return self.classes

    def init_from_xml(self, xml):
        for data in xml:
            c = CharacterClass()
            c._init_from_xml(data)
            self.classes.append(c)


class Skill:
    def __init__(self, name, value, dice=None):
        self.__value = value
        self.__dice = dice
        self.__name = name 

    def get_value(self):
        return self.__value

    def get_dice(self):
        return self.__dice 


class CharacterClass:
    def __init__(self):
        self.name = ""

    def _init_from_xml(self, xml):
        self.id = xml.attrib["id"]
        self.name = self.id
        self.__skills = {}
        self.__skills["hp"] = Skill("hp", 10)

        if 'selectable' in xml.attrib:     
            self.selectable = util.BooleanFromString.get_boolean(xml.attrib["selectable"])
        else:
            self.selectable = True

        for v in xml.iter(): 
            if(v.tag == "name"):
                self.name  = v.text 
            elif (v.tag == "description"):
                self.description = v.text
            elif (v.tag == "initialize"):

                value = None
                dice = None
                name = None 

                for s in v.iter():
                    if( s.tag != "initialize"):
                        if(s.tag == "value"):
                            value = s.text
                        elif(s.tag == "dice"):
                            dice = s.text 
                        else:
                            if name is not None:
                                self.__skills[name] = Skill(name, value, dice)

                            value = None
                            dice = None
                            name = s.tag 

        if name is not None:
            self.__skills[name] = Skill(name, value, dice)
