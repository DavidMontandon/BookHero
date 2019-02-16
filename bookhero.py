# -*- coding: utf-8 -*
import sys
import os

from Game.Core import engine

def main():
    story_folder = "Stories"
    story_package = "Sample"
    story_file = "start.xml"

    if(len(sys.argv) == 2):
        story_package = sys.argv[1] 

    story_path = os.path.join(story_folder, story_package)

    game = engine.BookHeroText( story_path, story_file )
    game.engine_start()

if __name__ == "__main__":
    main() 