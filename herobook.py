# -*- coding: utf-8 -*
import sys, os, getopt

from Game.Ui.Text import engine as TE 

def main(argv):
    story_engine = "Text"
    story_folder = "Stories"
    story_package="Sample"
    story_file = "start.xml"
    command = "herobook.py -e <Text/QT> -s <storyfolder> -f <file>"
    cur_folder =os.getcwd()

    try:
        opts, args = getopt.getopt(argv, "he:s:")
    except getopt.GetoptError:
        print(command)
        sys.exit(2)

    for opt, arg in opts:
        if opt == "-h":
            print(command)
            sys.exit() 
        elif opt in ("-e"):
            story_engine = arg
        elif opt in ("-s"):
            story_package = arg
        elif opt in ("-f"):
            story_file = arg

    if(story_engine == "Text"):
        game = TE.TextEngine(cur_folder, story_folder, story_package, story_file)
        game.engine_start()
    else:
        print("HeroBook Engine {engine} is unknow.".format(engine=story_engine))
        print(command)
        sys.exit(2)


if __name__ == "__main__":
    main(sys.argv[1:])  