class FlagHolder:
    def __init__(self):
        self.__flags = []

    def add(self, text):
        if not self.has_flag(text):
            self.__flags.append(text)

    def has_flag(self, text):
        if text in self.__flags:
            return True

        return False

    def __str__(self):
        s = "Debug - FlagHolder:"
        for f in self.__flags:
            s = s + f + ", "

        return s