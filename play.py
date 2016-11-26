import pygame, random, time
from pygame.locals import *
from lib import *

def play(screen, dictionary, nbr_coups):
    if nbr_coups == 5:
        difficulty = "difficile"
    elif nbr_coups == 10:
        difficulty = "moyen"
    elif nbr_coups == 15:
        difficulty = "facile"
    winner = font.render("Tu as gagné!!!",True,(0,0,0))
    loser = font.render("Tu as perdu!!!",True,(0,0,0))
    words = load_words(dictionary)
    new_word = create_new_word(random.choice(words), nbr_coups)
    while new_word.errors < new_word.nbr_coups and new_word.guess < len(new_word.text):
        screen.fill((255,255,255))
        screen.blit(font.render("Le mot que tu cherches est: ",True,(0,0,0)),(20,100))
        screen.blit(font.render("Erreurs: {}/{}".format(new_word.errors, new_word.nbr_coups),True,(0,0,0)),(20,200))
        new_word.render(screen)
        if new_word.errors > 0:
            screen.blit(pygame.image.load(os.path.join("data",difficulty,"{}.jpg".format(str(new_word.errors)))), (250,200))
        for e in pygame.event.get():
            if e.type == QUIT:
                exit()
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
                else:
                    screen.blit(font.render("Ceci n'est pas une lettre!!!",True,(0,0,0)),(180,10))
            pygame.display.update()

    menu_font = pygame.font.Font(os.path.join("data","True_Lies.TTF"),50)
    option1 = menu_font.render("RESTART",True,(0,0,0))
    option2 = menu_font.render("QUIT",True,(0,0,0))
    image = pygame.image.load(os.path.join("data","select.png"))
    cursor = pygame.transform.scale(image, (50,50))
    pos = 1
    while 1:
        screen.fill((255,255,255))
        screen.blit(font.render("Le mot était : {}".format(new_word.string_text),
                                True,
                                (255,0,0)),
                    (170,10))
        if new_word.errors == new_word.nbr_coups: screen.blit(loser,(170,100))
        else: screen.blit(winner,(170,100))
        screen.blit(option1,(200,200))
        screen.blit(option2,(200,300))
        screen.blit(cursor, (130,pos*100 + 100))
        for e in pygame.event.get():
            if e.type == QUIT:
                exit()
            elif e.type == KEYDOWN:
                if e.key == K_DOWN:
                    pos += 1
                    if pos > 2: pos = 1
                elif e.key == K_UP:
                    pos -= 1
                    if pos < 1: pos = 2
                elif e.key == K_RETURN:
                    if pos == 1:
                        play(screen, dictionary, nbr_coups)
                    elif pos == 2:
                        exit()
        pygame.display.update()
