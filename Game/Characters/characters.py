class CharacterHolder:
    def __init__(self):
        self.__characters = {}
        self.__party = {}

    def add_party(self, party_id, party_name):
        self.__party[party_id] = Party(party_id, party_name)

    def get_party(self, party_name):
        return self.__party[party_name]

    def add_character(self, character_id):
        self.__characters[character_id] = Character()

    def set_character_class(self, character_id, class_id):
        c = self.__characters[character_id]
        c.set_class(class_id)
        self.__characters[character_id] = c

    def add_character_to_party(self, party_id, character_id):
        p = self.get_party(party_id)
        p.add_character(character_id)
        self.__party[party_id] = p

    def remove_character_to_party(self, character_id, party_id):
        return 

    def add_xp_to_party(self, xp, party_id):
        return

class Party:
    def __init__(self, party_id, party_name):
        self.__characters = []
        self.__party_name = party_name
        self.__party_id = party_id

    def add_character(self, character_id):
        self.__characters.append(character_id)

class Character:
    def __init__(self):
        self.__name = None
        self.__class_id = None
        self.__level = 0
        self.__xp = 0
        self.__alive = True

    def set_class(self, class_id):
        self.__class_id = class_id

    def is_alive(self):
        return self.__alive

