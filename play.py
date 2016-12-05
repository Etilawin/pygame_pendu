import pygame, random, time
from pygame.locals import *
from lib import *


def play(screen, dictionary, nbr_coups, players = False):
    """ Fonction principale de jeu, corps général qui marche pour un
        ou deux joueurs """
    bg = pygame.image.load(os.path.join("data","background.jpg"))
    if players:
        dictionary = ask(screen, "Veuillez entrer votre mot : ")
    # On définit la difficulté (donc le chemin)
    if nbr_coups == 5:
        difficulty = "difficile"
    elif nbr_coups == 10:
        difficulty = "moyen"
    elif nbr_coups == 15:
        difficulty = "facile"
    # Messages de fin
    winner = font.render("BRAVO !!!", True, (255, 255, 255))
    loser = font.render("Tu as perdu !!!", True, (255, 255, 255))
    if not players: # Si on est pas à deux joueurs :
        words = load_words(dictionary) # On charge le dictionnaire
    else: # Sinon le mot beh c'est le mot entré
        words = [dictionary]
    # Le mot est choisi au hasard
    new_word = create_new_word(random.choice(words), nbr_coups)
    # Tant qu'on à pas dépassé le nombre de coups ou qu'on à pas trouvé le mot
    while new_word.errors < new_word.nbr_coups and new_word.guess < len(new_word.text):
        # On met tout à l'écran
        screen.blit(bg, (0, 0))
        screen.blit(font.render("Le mot que tu cherches est : ", True, (255, 255, 255)), (20, 100))
        screen.blit(font.render("Erreurs : {} / {} ".format(new_word.errors, new_word.nbr_coups),
                                True,
                                (255, 255, 255)),
                    (20, 200))
        new_word.render(screen) # MEME LE MOT OLALALALA
        if new_word.errors > 0:
            # On affiche l'image correspondant au nombres d'erreurs
            screen.blit(pygame.image.load(os.path.join("data",
                                                       difficulty,
                                                       "{}.png".format(str(new_word.errors)))),
                        (250, 200))
        for e in pygame.event.get():
            if e.type == QUIT:
                pygame.quit()
                sys.exit("Quitting...") # On dit que ça quitte
            elif e.type == KEYDOWN: # Weird because AZERTY (Vive la France)
                if e.key == K_a:
                    new_word.update("q")
                elif e.key == K_b:
                    new_word.update("b")
                elif e.key == K_c:
                    new_word.update("c")
                elif e.key == K_d:
                    new_word.update("d")
                elif e.key == K_e:
                    new_word.update("e")
                elif e.key == K_f:
                    new_word.update("f")
                elif e.key == K_g:
                    new_word.update("g")
                elif e.key == K_h:
                    new_word.update("h")
                elif e.key == K_i:
                    new_word.update("i")
                elif e.key == K_j:
                    new_word.update("j")
                elif e.key == K_k:
                    new_word.update("k")
                elif e.key == K_l:
                    new_word.update("l")
                elif e.key == K_SEMICOLON:
                    new_word.update("m")
                elif e.key == K_n:
                    new_word.update("n")
                elif e.key == K_o:
                    new_word.update("o")
                elif e.key == K_p:
                    new_word.update("p")
                elif e.key == K_q:
                    new_word.update("a")
                elif e.key == K_r:
                    new_word.update("r")
                elif e.key == K_s:
                    new_word.update("s")
                elif e.key == K_t:
                    new_word.update("t")
                elif e.key == K_u:
                    new_word.update("u")
                elif e.key == K_v:
                    new_word.update("v")
                elif e.key == K_w:
                    new_word.update("z")
                elif e.key == K_x:
                    new_word.update("x")
                elif e.key == K_y:
                    new_word.update("y")
                elif e.key == K_z:
                    new_word.update("w")
                elif e.key == K_ESCAPE:
                    return 0
                else: # Faudrait vraiment être stupide...
                    screen.blit(font.render("Ceci n'est pas une lettre!!!",
                                            True,
                                            (255, 255, 255)),
                                (180, 10))
            pygame.display.update() # On met de l'eau (rafraîchit la fenêtre)

    # Pour voir comment un menu fonctionne GOTO: menu.py
    menu_font = pygame.font.Font(os.path.join("data", "True_Lies.TTF"), 50)
    option1 = menu_font.render("RESTART", True, (255, 255, 255))
    option2 = menu_font.render("QUIT", True, (255, 255, 255))
    option3 = menu_font.render("MENU PRINCIPAL", True, (255, 255, 255))
    image = pygame.image.load(os.path.join("data", "select.png"))
    cursor = pygame.transform.scale(image, (50, 50))
    pos = 1
    while 1: # Boucle infinie
        screen.blit(bg, (0, 0))
        screen.blit(font.render("Le mot etait : {} ".format(new_word.string_text),
                                True,
                                (0, 255, 0)),
                    (170, 10))
        if new_word.errors == new_word.nbr_coups: screen.blit(loser, (170, 100))
        else: screen.blit(winner, (170, 100))
        screen.blit(option1, (200, 200))
        screen.blit(option2, (200, 300))
        screen.blit(option3, (200, 400))
        screen.blit(cursor,  (130, pos*100 + 100))
        for e in pygame.event.get():
            if e.type == QUIT:
                pygame.quit()
                sys.exit("Quitting...")
            elif e.type == KEYDOWN:
                if e.key == K_DOWN:
                    pos += 1
                    if pos > 3: pos = 1
                elif e.key == K_UP:
                    pos -= 1
                    if pos < 1: pos = 3
                elif e.key == K_RETURN:
                    if pos == 1:
                        returned = play(screen, dictionary, nbr_coups, players)
                        if not returned:
                            return 0
                    elif pos == 2:
                        pygame.quit()
                        sys.exit("Quitting...")
                    elif pos == 3:
                        return 0
        pygame.display.update()
