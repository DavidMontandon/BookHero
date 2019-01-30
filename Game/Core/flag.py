class FlagHolder:
    def __init__(self):
        self.__flags = []

    def add(self, text):
        if not self.has_flag(text):
            self.__flags.append(text)

        print(self.__flags)

    def has_flag(self, text):
        if text in self.__flags:
            return True

        return False
