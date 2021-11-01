import pygame
from pygame.locals import *
#from Screen_abc import Screen
from TestScreen import TestScreen
from TestScreen2 import TestScreen2
from test import test
import Screen_abc as SC
from MainScreen import MainScreen


#screen = [TestScreen(),TestScreen2(),test(),MainScreen()]     
screen = [MainScreen()]
if __name__ == '__main__':
    while True:
        screen[SC.ScreenNum].display()
        screen[SC.ScreenNum].getEvent()

       


