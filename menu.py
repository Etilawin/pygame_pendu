import pygame, os, sys
from pygame.locals import *
from lib import *
from play import *
from tkinter.filedialog import askopenfilename
from tkinter import *

def start_menu(screen):
    # Checking if default dictionnary exists
    if os.path.exists(os.path.join("data","dictionary.txt")):
        dictionary = os.path.join("data","dictionary.txt")
    else:
        pygame.quit()
        sys.exit('No default dictionnary in data, please add one')

    nbr_coup = 15
    font = pygame.font.Font(os.path.join("data","True_Lies.TTF"),50) # On ajoute notre propre police d'écriture
    image = pygame.image.load(os.path.join("data","select.png"))
    cursor = pygame.transform.scale(image, (50,50))
    pos = 1 # Position du curseur
    option1 = font.render("START",True,(0,0,0)) # On écrit ...
    option2 = font.render("IMPORT DICT",True,(0,0,0))
    option3 = font.render("DIFFICULTY",True,(0,0,0))
    option4 = font.render("QUIT",True,(0,0,0))
    while 1:
        screen.fill((255,255,255)) # Fond blanc
        screen.blit(option1,(150,100))
        screen.blit(option2,(150,200))
        screen.blit(option3,(150,300))
        screen.blit(option4,(150,400))
        screen.blit(cursor, (80,pos*100))
        for e in pygame.event.get():
            if e.type == QUIT:
                exit()
            elif e.type == KEYDOWN:
                if e.key == K_DOWN:
                    pos += 1
                    if pos > 4: pos = 1
                elif e.key == K_UP:
                    pos -= 1
                    if pos < 1: pos = 4
                elif e.key == K_RETURN:
                    if pos == 1:
                        play(screen, dictionary, nbr_coup)
                    elif pos == 2:
                        root = Tk()
                        root.update()
                        dictionary = askopenfilename(title="Ouvrir votre dictionnaire perso",
                                                     filetypes=[('txt files','.txt'),('all files','.*')])
                        root.destroy()
                    elif pos == 3:
                        nbr_coup = difficulty_menu(screen, nbr_coup)
                    elif pos == 4:
                        exit()

        pygame.display.update()

def difficulty_menu(screen, difficulty):
    font = pygame.font.Font(os.path.join("data","True_Lies.TTF"),50) # On ajoute notre propre police d'écriture
    image = pygame.image.load(os.path.join("data","select.png"))
    cursor = pygame.transform.scale(image, (50,50))
    pos = 1 # Position du curseur
    option1 = font.render("FACILE",True,(0,0,0)) # On écrit ...
    option2 = font.render("MOYEN",True,(0,0,0))
    option3 = font.render("DIFFICILE",True,(0,0,0))
    option4 = font.render("RETOUR",True,(0,0,0))
    while 1:
        screen.fill((255,255,255)) # Fond blanc
        screen.blit(option1,(150,100))
        screen.blit(option2,(150,200))
        screen.blit(option3,(150,300))
        screen.blit(option4,(150,400))
        screen.blit(cursor, (80,pos*100))
        for e in pygame.event.get():
            if e.type == QUIT:
                exit()
            elif e.type == KEYDOWN:
                if e.key == K_DOWN:
                    pos += 1
                    if pos > 4: pos = 1
                elif e.key == K_UP:
                    pos -= 1
                    if pos < 1: pos = 4
                elif e.key == K_RETURN:
                    if pos == 1:
                        return 15
                    elif pos == 2:
                        return 10
                    elif pos == 3:
                        return 5
                    elif pos == 4:
                        return difficulty

        pygame.display.update()
