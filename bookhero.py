# -*- coding: utf-8 -*
import sys

from Game.Core import engine

def main():
    story_file = "sample.xml"

    if(len(sys.argv) == 2):
        story_file = sys.argv[1] 

    game = engine.BookHeroText( story_file )
    game.engine_start()

if __name__ == "__main__":
    main() 