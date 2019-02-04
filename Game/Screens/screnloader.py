from Game.Screens import storyboard
from Game.Screens import classselector

class ScreenLoader:
    @staticmethod
    def load_from_xml(xml):
        s = None 
        screen_type = xml.attrib["type"]

        if(screen_type == "StoryBoard"):
            s = storyboard.StoryBoardScreen()
        elif(screen_type == "ClassSelector"):
            s = classselector.ClassSelectorScreen()
        
        if (s != None):
            s.load_xml(xml)
            
        return s