class VisitedScreenHolder:
    def __init__(self):
        self.__visited_screen = {}

    def get_visited_screen(self, id):
        r = self.__visited_screen.get(id)
        if(r == None):
            r = _VisitedScreen(id)
            self.__visited_screen[id] = r
        return r 

    def set_visited_screen(self, id):
        r = self.get_visited_screen(id)
        r._set_visited()

    def __str__(self):
        s = "Debug - VisitedScreenHolder:"

        for v in self.__visited_screen:
            s += v + ", "

        return s

class _VisitedScreen:
    def __init__(self, id):
        self.__id = id 
        self.__items = []
        self.__visitied = False 

    def _get_id(self):
        return self.__id

    def _set_visited(self):        
        self.__visitied = True  

    def get_items(self):
        return self.__items 

    def get_visited(self):
        return self.__visitied