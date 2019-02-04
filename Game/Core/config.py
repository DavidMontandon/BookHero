class ConfigHolder:
    def __init__(self):
        self.__config = {}
        self.__set_default()

    def __set_default(self):
        self.__config["VisitXP"] = 1
        self.__config["GameStart"] = "#GameStart"
        self.__config["MainCharacter"] = "Hero"
        self.__config["MainParty"] = "Your party"

    def get_config(self, id):
        return self.__config[id]

    def init_from_xml(self, xml):
        for data in xml:
            if 'type' in data.attrib:     
                self.__config[data.attrib["type"]] = data.text
 