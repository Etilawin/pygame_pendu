import pygame, os
from pygame.locals import *
from lib import *
from play import *

def start_menu(screen):
    font = pygame.font.Font(os.path.join("data","maiden.TTF"),50) # On ajoute notre propre police d'écriture
    image = pygame.Surface((50,50)) # On crée une nouvelle surface
    image.fill((255,255,255)) # Blanc
    pygame.draw.polygon(image,(0,0,0),[(0,0),(25,25),(0,50)],5) # Carré
    pos = 1 # Position du curseur
    option1 = font.render("START",True,(0,0,0)) # On écrit ...
    option2 = font.render("FULLSCREEN",True,(0,0,0))
    option3 = font.render("QUIT",True,(0,0,0))
    while 1:
        screen.fill((255,255,255)) # Fond blanc
        screen.blit(option1,(200,100))
        screen.blit(option2,(200,200))
        screen.blit(option3,(200,300))
        screen.blit(image,(130,pos*100))
        for e in pygame.event.get():
            if e.type == QUIT:
                exit()
            elif e.type == KEYDOWN:
                if e.key == K_DOWN:
                    pos += 1
                    if pos > 3: pos = 1
                elif e.key == K_UP:
                    pos -= 1
                    if pos < 1: pos = 3
                elif e.key == K_RETURN:
                    if pos == 1:
                        play(screen)
                    elif pos == 2:
                        pygame.display.set_mode((0,0),pygame.FULLSCREEN)
                    elif pos == 3:
                        exit()
        pygame.display.update()
