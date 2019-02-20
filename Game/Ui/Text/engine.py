import xml.etree.ElementTree as ET
import os
from ...Core import core
from ...Util import util 

class TextEngine:
    def __init__(self, cur_folder, story_path, story_folder, story_file):
        self.__set_story(cur_folder, story_path, story_folder, story_file)

    def __set_story(self, cur_folder, story_path, story_folder, story_file):
        self.__cur_folder = cur_folder 
        self.__cur_story_path = story_path
        self.__story_folder = story_folder
        self.__story_file = story_file
        self.__main_folder = os.path.join(cur_folder, story_path)

    def __str__(self):
        return "TextEngine root={root},  story={story}, file={file}".format(root=self.__main_folder, story=self.__story_folder, file=self.__story_file)

    def __get_core(self):
        return self.__core

    def __set_core(self, core):
        self.__core = core 

    def __init_core(self):
        self.__set_core(core.CoreEngine(os.path.join(self.__main_folder, self.__story_folder), self.__story_file))

    def engine_start(self):
        self.__init_core()
        self.__engine_start_message()
        self.__game_start()
        self.__engine_stop_message()

    def __game_start(self):
        """ Gameloop

        Parameters
        ----------
        None

        Returns
        -------
        None
        """ 
        
        self.__core.init_game() 
        
        if self.__core.has_save_file():
            self.__core.load_game()

        running = True

        while running:
            m = self.__print(self.__core.get_screen())

            r = self.__core.set_choice(m)
            running = r["continue"]
            if(r["msg"] != ""):
                util.Console.clear()
                print(r["msg"])
                input("Press Enter to continue...")


    def __print(self, data):
        """ Print - Print the text and choices of the screen

        Parameters
        ----------
        data : dictionary
            Informations to print

        Returns
        -------
        dictionary
            Choosed choices
        """
        self.__print_header()

        next_screen = ""
        for text in data["text"]:
            util.Console.center(text)

        print("")

        for c in data["choices"]:
            print(c.code, " : ", c.text)

        while(next_screen == ""):
            m = {}
            m["next"] = ""

            choice = str(input("Enter your choice : ")).upper()

            for c in data["choices"]:
                if( str(choice) == c.code ):
                    m = c.get_screen_map()
            
            next_screen = m["next"]
            if( next_screen == ""):
                print("Invalid choice.")

        m["type"] = data["type"]
        return m 

    def __print_header(self):
        """ Print - Page header

        Parameters
        ----------
        None

        Returns
        -------
        None
        """

        util.Console.clear()
        engine_info = self.__get_core().get_engine_info()
        print("=======================================================================================================================")
        print("{name} {version} by {author}".format(name=engine_info["name"], version=engine_info["version"], author=engine_info["author"]))
        print("=======================================================================================================================")

    def __engine_start_message(self):
        """ Print - Welcome message

        Parameters
        ----------
        None

        Returns
        -------
        None
        """ 

        util.Console.clear()
        engine_info = self.__get_core().get_engine_info()

        print("\n\n")
        print("=======================================================================================================================")
        print("TEXT ENGINE STARTED - Running {name} {version} by {author}".format(name=engine_info["name"], version=engine_info["version"], author=engine_info["author"]))
        if(self.__story_folder=="Sample"):
            print("\nYou can also run you own Story directly by using the command line : python herobook.py -s <storyfolder>")
        print("=======================================================================================================================\n\n")
        print("For more informations, please visit : https://github.com/DavidMontandon/BookHero")
        print("\n")
        input("Press Enter to continue...")

    def __engine_stop_message(self):
        """ Print - Closing message

        Parameters
        ----------
        None

        Returns
        -------
        None
        """

        util.Console.clear()
        engine_info = self.__get_core().get_engine_info()

        print("\n\n")
        print("=======================================================================================================================")
        print("TEXT ENGINE STOPPED - Running {name} {version} by {author}".format(name=engine_info["name"], version=engine_info["version"], author=engine_info["author"]))
        print("=======================================================================================================================\n\n")
        print("For more informations, please visit : https://github.com/DavidMontandon/BookHero")
        print("\n")


    def __get_stories_list(self, path):
        """ Fetch the list of stories inside the parent folder

        Parameters
        ----------
        path : str
            Path of the parent folder
 
        Returns
        -------
        list
            A list of folder
        """
        
        return []