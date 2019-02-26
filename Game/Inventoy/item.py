from Game.Enum import enums

class ItemLoader:
    def __init__(self, file_name):
        self.__file_name = file_name
        self.__root = None
        self.__type = enums.LoadingConfig.NONE
        self.__set_file(file_name)
        print(self.__file_name)

    def __set_file(self, file_name):
        if(file_name.find(".xml") > -1):
            self.__init_xml(file_name)

    def __init_xml(self, file_name):
        import xml.etree.ElementTree as ET
        with open(file_name, "r") as xml_file:
            tree =  ET.parse(xml_file)

        self.__root = tree.getroot()
        self.__type = enums.LoadingConfig.XML

    def __get_item_xml(self, item_id):
        item_xml = self.__root.find("./items/item[@id='" + item_id + "']")

        if(item_xml == None):
            return None
        else:
            item = Item(item_id)
            item.load_xml(item_xml)
            return item

    def get_item(self, item_id):
        if(self.__type == enums.LoadingConfig.XML):
            return self.__get_item_xml(item_id)
        else:
            return None

class Item:
    def __init__(self, item_id):
        self.__info={}
        self.__id = item_id
        self.__name = ""

    def load_xml(self, xml):
        for v in xml.iter(): 
            if(v.tag == "name"):
                self.__name = v.text

    def get_name(self):
        return self.__name 

