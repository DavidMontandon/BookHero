from Game.Core import instance

class VisitedScreenHolder:
    def __init__(self):
        self.__visited_screen = {}

    def is_visited(self, screen_id):
        return self.get_visited_screen(screen_id).is_visited()

    def get_visited_screen(self, screen_id):
        s = self.__visited_screen.get(screen_id)
        if(s == None):
            s = _VisitedScreen(screen_id)
            self.__visited_screen[screen_id] = s
        return s

    def add_item(self, screen_id, item_id, quantity):
        s = self.get_visited_screen(screen_id)
        s.add_item(item_id, quantity)
        self.__visited_screen[screen_id] = s

    def set_visited_screen(self, screen_id):
        s = self.get_visited_screen(screen_id)
        s._set_visited()

    def get_items(self, screen_id):
        return self.get_visited_screen(screen_id).get_items()
        
    def __str__(self):
        s = "Debug - VisitedScreenHolder:"

        for v in self.__visited_screen:
            s += v + ", "

        return s

class _VisitedScreen:
    def __init__(self, screen_id):
        self.__id = screen_id 
        self.__items = {}
        self.__visitied = False 

    def __str__(self):
        return self.__id

    def _get_id(self):
        return self.__id

    def _set_visited(self):        
        self.__visitied = True  

    def add_item(self, item_id, quantity):
        item = self.get_item(item_id)
        if(item == None):
            mem = instance.Instance.get_instance()

            source = mem.get_item(item_id)

            item = {}
            item["quantity"] = quantity

            if(source == None):
                item["name"] = "Object not found"
            else:
                item["name"] = source.get_name()

            self.__items[item_id] = item
        else:
            item["quantity"] += quantity
            self.__items[item_id] = item


    def get_item(self, item_id):
        if item_id in self.__items:
            return self.__items[item_id] 
        else:
            return None

    def get_items(self):
        return self.__items 

    def is_visited(self):
        return self.__visitied