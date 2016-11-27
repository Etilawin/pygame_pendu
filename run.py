import pygame
from pygame.locals import *
pygame.init() # On initialise pygame et ses fonctions
from menu import *

screen = pygame.display.set_mode((640,480)) # Auto screen

start_menu(screen) # Let's go!
