from Game.Util import util 

class ClassHolder:
    def __init__(self):
        self.classes = []

    def init_from_xml(self, xml):
        for data in xml:
            c = CharacterClass()
            c._init_from_xml(data)
            self.classes.append(c)


class CharacterClass:
    def __init__(self):
        self.name = ""

    def _init_from_xml(self, xml):
        self.id = xml.attrib["id"]

        if 'name' in xml.attrib:     
            self.name = xml.attrib["name"] 
        else:
            self.name = xml.attrib["id"] 

        if 'selectable' in xml.attrib:     
            self.selectable = util.BooleanFromString.get_boolean(xml.attrib["selectable"])
        else:
            self.selectable = True
