# -*- coding: utf-8 -*
import xml.etree.ElementTree as ET
import sys
import random

class BookHeroEngine:
    def __init__(self, gameFile):
        self.version = "0.0.2"
        self.gameFile = gameFile 
        self.engineRunning = True
        self.curRoom = "#GameStart"
        self.engineName = "Python Book Hero Engine"
        self.engineAuthor = "David Montandon"
        self.messages = Messages() 
        self.roomID = ""

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
        self.loadMessages()

        while(self.engineRunning):
            nextRoom = ""
            room = self.loadRoom(self.curRoom)
            room.printTextRoom(self.messages.getRandomText("actionMove"))

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

    def loadMessages(self):
        for msg in self.root.findall("./messages/message"):
            self.messages.add(msg.attrib["type"], msg.text)

    def loadRoom(self, roomName):
        roomXML = self.root.find("./rooms/room[@id='" + roomName + "']")
        room = Room(roomXML)                    
        return room

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

class BooleanFromString:
    def getBoolean(v):
        if(v == "true" or v == "True"):
            return True
        else:
            return False

class Choice:
    def __init__(self, code, text, next):
        self.text = text 
        self.next = next 
        self.code = code 

class Room:
    def __init__(self, source):
        self.choices = [] 

        self.initFromXML(source)

        self.addDefaultChoices()

    def initFromXML(self, xml):
        self.id = xml.attrib["id"]

        if 'name' in xml.attrib:     
            self.name = xml.attrib["name"] 
        else:
            self.name = xml.attrib["id"] 

        if 'type' in xml.attrib:     
            self.type = xml.attrib["type"] 
        else:
            self.type = "Room" 

        if 'randomActionMessage' in xml.attrib:   
            self.randomActionMessage = BooleanFromString.getBoolean(xml.attrib["randomActionMessage"]) 
        else:
            self.randomActionMessage = True

        for v in xml.iter(): 
            if(v.tag == "choice"):
                self.addChoice(v.text, v.attrib["next"])
            elif (v.tag == "description"):
                self.addDesc(v.text)
            elif (v.tag == "type"):
                self.addType(v.text)
        
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

    def printTextRoom(self, actionMessage):
        print("\n\n\n============================================")
        self.printDesc()
        if(self.randomActionMessage):
            print(actionMessage)
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