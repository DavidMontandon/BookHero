from Game.Screens import storyboard as SB
from Game.Screens import classselector as CS

class ScreenLoader:
    @staticmethod
    def load_from_xml(xml):
        s = None 
        screen_type = xml.attrib["type"]

        if(screen_type == "StoryBoard"):
            s = SB.StoryBoardScreen()
        elif(screen_type == "ClassSelector"):
            s = CS.ClassSelectorScreen()
        
        if (s != None):
            s.load_xml(xml)
            
        return s