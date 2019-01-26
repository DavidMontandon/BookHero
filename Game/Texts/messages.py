import random

class Messages:
    def __init__(self):
        self.messages = {'actionMove':[]}

    def add(self, cat, text):
        list = self.messages[cat]
        list.append( text )
        self.messages[cat] = list

    def getRandomText(self, cat):
        list = self.messages[cat]
        n = random.randint(0, len(list) - 1)
        return list[n]