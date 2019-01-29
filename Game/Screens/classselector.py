from Game.Screens import screen
from Game.Screens import choice

class ClassSelectorScreen(screen.Screen):
    def __init__(self):
        screen.Screen.__init__(self)

    def load_xml(self, xml):
        screen.Screen._load_xml(self, xml)
        self._add_default_choices()

    def _add_default_choices(self):
        self._choices.append(choice.Choice("X","Quit the game WITHOUT saving","#Quit"))
