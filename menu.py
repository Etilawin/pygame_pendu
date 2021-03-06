# Hop on importe tout le bordel
import pygame, os, sys
from pygame.locals import *
from lib import *
from play import *
from tkinter.filedialog import askopenfilename
from tkinter import *

def start_menu(screen):
    """ écran principal, menu principal du joueur """
    # On met de la musikquent
    pygame.mixer.music.load(os.path.join("data", "halloween.mp3"))
    pygame.mixer.music.play(-1) # Loop = infinie
    pygame.mixer.music.set_volume(0.5) # On réduit le volume
    # On vérifie le dictionnaire
    if os.path.exists(os.path.join("data", "dictionary.txt")):
        dictionary = os.path.join("data", "dictionary.txt")
    else:
        pygame.quit()
        sys.exit('No default dictionnary in data, please add one')

    # Difficulté :
    nbr_coup = 15
    # Si os path marche pas ben... y'avait qu'a pas delete les fichiers pour rien
    # os.path.join est cross plateforme (pour les séparations)
    font = pygame.font.Font(os.path.join("data", "True_Lies.TTF"), 50) # On ajoute notre propre police d'écriture
    image = pygame.image.load(os.path.join("data", "select.png")) # Curseur
    cursor = pygame.transform.scale(image,  (50, 50)) # On le resize
    pos = 0 # Position du curseur
    # On définit les options
    option0 = font.render("1 PLAYER", True, (255, 255, 255))
    option1 = font.render("2 PLAYER", True, (255, 255, 255))
    option2 = font.render("IMPORT DICT", True, (255, 255, 255))
    option3 = font.render("DIFFICULTY", True, (255, 255, 255))
    option4 = font.render("QUIT", True, (255, 255, 255))
    # Le petit background
    bg = pygame.image.load(os.path.join("data", "background.jpg"))
    # Boucle infinie
    while 1:
        # On affiche tout
        screen.blit(bg,  (0, 0))
        screen.blit(option0, (150, 10))
        screen.blit(option1, (150, 110))
        screen.blit(option2, (150, 210))
        screen.blit(option3, (150, 310))
        screen.blit(option4, (150, 410))
        screen.blit(cursor,  (80, pos*100 + 10))
        for e in pygame.event.get():
            if e.type == QUIT: # Si il ferme la fenêtre on quitte tout
                pygame.quit()
                sys.exit("Quitting...")
            elif e.type == KEYDOWN: # Si il appuie sur une touche
                if e.key == K_DOWN: # Flèche du bas
                    pos += 1
                    if pos > 4: pos = 0 # Si TROP haut,  on redescend :D
                elif e.key == K_UP: # Flèche du haut
                    pos -= 1
                    if pos < 0: pos = 4 # Si TROP bas, on remonte (suspense)
                elif e.key == K_RETURN:
                    if pos == 0: # 1 PLAYER
                        play(screen, dictionary, nbr_coup) # On lance le jeu!
                    elif pos == 1: # 2 PLAYERS
                        play(screen, dictionary, nbr_coup, True)
                    elif pos == 2: # Si "IMPORT DICT"
                        # On utilise le gestionnaire de fichier Tkinter
                        root = Tk()
                        root.update()
                        dictionary = askopenfilename(title="Ouvrir votre dictionnaire perso",
                                                     filetypes=[('txt files', '.txt'), ('all files', '.*')])
                        root.destroy()
                    elif pos == 3: # DIFFICULTY
                        nbr_coup = difficulty_menu(screen, nbr_coup) # On choisit
                    elif pos == 4: # QUIT
                        pygame.quit()
                        sys.exit("Quitting...") # ça parle de lui-même....

        pygame.display.update() # On update tout l'écran

def difficulty_menu(screen, difficulty):
    # ET C'EST REPARTI (voir ligne 26)
    font = pygame.font.Font(os.path.join("data", "True_Lies.TTF"), 50)
    image = pygame.image.load(os.path.join("data", "select.png"))
    cursor = pygame.transform.scale(image, (50, 50))
    pos = 1 # Position du curseur
    option1 = font.render("FACILE", True, (255, 255, 255)) # ON ECRIT !!!!
    option2 = font.render("MOYEN", True, (255, 255, 255))
    option3 = font.render("DIFFICILE", True, (255, 255, 255))
    option4 = font.render("RETOUR", True, (255, 255, 255))
    bg = pygame.image.load(os.path.join("data", "background.jpg"))
    while 1:
        screen.blit(bg, (0, 0))
        screen.blit(option1, (150, 100))
        screen.blit(option2, (150, 200))
        screen.blit(option3, (150, 300))
        screen.blit(option4, (150, 400))
        screen.blit(cursor,  (80, pos*100))
        for e in pygame.event.get():
            if e.type == QUIT:
                pygame.quit()
                sys.exit("Quitting...")
            elif e.type == KEYDOWN:
                if e.key == K_DOWN:
                    pos += 1
                    if pos > 4: pos = 1
                elif e.key == K_UP:
                    pos -= 1
                    if pos < 1: pos = 4
                elif e.key == K_RETURN:
                    if pos == 1: # FACILE
                        return 15
                    elif pos == 2: # MOYEN
                        return 10
                    elif pos == 3:
                        return 5 # DIFFICILE
                    elif pos == 4:
                        return difficulty

        pygame.display.update()
