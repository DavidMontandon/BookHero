# -*- coding: utf-8 -*
import xml.etree.ElementTree as ET
import sys

class BookHeroEngine:
    def __init__(self, gameFile):
        self.version = "0.0.1"
        self.gameFile = gameFile 
        self.engineRunning = True
        self.curRoom = "#GameStart"
        self.engineName = "Python Book Hero Engine"
        self.engineAuthor = "David Montandon"

    def engineStartMessage(self):
        print("\n\n\n============================================")
        print(self.engineName ,  self.version , "by" , self.engineAuthor , "- STARTED")
        if(self.gameFile=="sample.xml"):
            print("\nYou can also run you own StoryFile using the command line : python bookhero.py yourworld.xml")
        print("============================================")

    def engineStopMessage(self):
        print("\n\n\n============================================")
        print(self.engineName ,  self.version , "by" , self.engineAuthor , "- STOPPED")
        print("============================================")

    def loadXMLTree(self):
        with open(self.gameFile, "r") as xml_file:
            self.tree = ET.parse(xml_file)
        
        self.root = self.tree.getroot()

    def engineStart(self):
        choice = "" 
        self.engineStartMessage() 
        self.loadXMLTree() 

        while(self.engineRunning):
            nextRoom = ""
            room = self.loadRoom(self.curRoom)
            room.printTextRoom()

            while(nextRoom == ""):
                choice = room.getUserChoice()
                nextRoom = room.checkChoice(choice)
                if( nextRoom == ""):
                    print("Invalid choice.")

            if(nextRoom=="#Quit"):
                self.engineRunning = False
            elif(nextRoom=="#GameOver"):
                self.engineRunning = False

            self.curRoom = nextRoom

        self.engineStopMessage() 

    def loadRoom(self, roomName):
        roomXML = self.root.find("./room[@id='" + roomName + "']")
        room = Room(roomName)
        for v in roomXML.iter(): 
            if(v.tag == "choice"):
                room.addChoice(v.text, v.attrib["next"])
            elif (v.tag == "description"):
                room.addDesc(v.text)
            elif (v.tag == "type"):
                room.addType(v.text)
            
        room.addDefaultChoices()
        return room

class Choice:
    def __init__(self, code, text, next):
        self.text = text 
        self.next = next 
        self.code = code 

class Room:
    def __init__(self, name):
        self.name = name 
        self.choices = [] 
        
    def info(self):
        print(self.name)

    def addDesc(self, desc):
        self.desc = desc

    def addType(self, desc):
        self.type = desc

    def addChoice(self, choiceText, choiceNextRoom):
        self.choices.append(Choice(str(len(self.choices) + 1),choiceText, choiceNextRoom))

    def addDefaultChoices(self):
        self.choices.append(Choice("X","Quit the game WITHOUT saving","#Quit"))

    def printDesc(self):
        print(self.desc)

    def printType(self):
        print("Type:" , self.type)

    def printChoices(self):
        print("Choice(s) :\n===========")
        for c in self.choices:
            print(c.code, " : ", c.text)

    def checkChoice(self, choice):
        for c in self.choices:
            if( str(choice) == c.code ):
                return c.next
        return "" 

    def printTextRoom(self):
        print("\n\n\n============================================")
        self.printDesc()
        print("\n")
        self.printChoices()
        print("============================================")

    def getUserChoice(self):
        return str(input("Enter your choice : ")).upper()

def main():
    storyFile = "sample.xml"

    if(len(sys.argv) == 2):
        storyFile = sys.argv[1] 

    engine = BookHeroEngine( storyFile )
    engine.engineStart()

if __name__ == "__main__":
    main() 