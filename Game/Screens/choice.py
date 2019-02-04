class Choice:
    def __init__(self, code, text, next):
        c = next.split(":")
        map = {}
        if(len(c) == 2): 
            map["file"] = c[0]
            map["next"] = c[1]
            self.file = c[0] 
            self.next = c[1] 
        else:
            map["file"] = None
            map["next"] = next
            self.next = next 
            self.file = None

        self.__screen_map = map
        self.text = text
        self.code = code


    def get_continue(self):
        return self.next

    def get_text(self):
        return self.text

    def get_code(self):
        return self.code

    def get_screen_map(self):
        return self.__screen_map