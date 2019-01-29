class CharacterHolder:
    def __init__(self):
        self.__characters = {}
        self.__party = {}

    def add_character(self,id):
        self.__characters[id] = Character()

    def add_character_to_party(self, id_character, id_party):
        return 

    def remove_character_to_party(self, id_character, id_party = None):
        return 

    def add_xp_to_party(self, xp, id_party):
        return

class Character:
    def __init__(self):
        self.__name = None
        self.__class_id = None
        self.__level = 0
        self.__xp = 0
        self.__alive = True

    def is_alive(self):
        return self.__alive

