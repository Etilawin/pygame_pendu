import pygame, os, sys, string
from pygame.locals import *

font = pygame.font.Font(os.path.join("data","True_Lies.TTF"),30)

class word:
    """ Classe word pour le jeu du pendu """
    def __init__(self,text,dark,nbr_coups):
        """ On initialise tout comme d'hab """
        self.text = text
        self.dark = dark
        self.string_dark = ''.join(self.dark) # Liste en mot
        self.string_text = ''.join(self.text)
        self.nbr_coups = nbr_coups
        self.errors = 0
        self.guess = 0
        self.true_letters = []
        self.wrong_letters = []
        self.tested_letters = []
        self.wrong = "" # Si la lettre rentrée est déjà entrée on changera sa valeur

    def update(self,letter):
        """ On met a jour le mot """
        if letter not in self.tested_letters: # Si on a pas déjà entré la lettre
            self.wrong = "" # Pas de fausse lettre
            self.tested_letters.append(letter) # On ajoute aux lettres entrées
            found = False
            for i in range(len(self.text)): # On cherche la lettre dans le mot
                if self.text[i] == letter: # On le met à jour si elle est dans le mot
                    self.dark[i] = letter
                    found = True
                    self.guess += 1 # Lettres trouvées += 1
                    self.true_letters.append(letter)
            if not found: # Sinon
                self.errors += 1 # Erreurs += 1
                self.wrong_letters.append(letter)
        else:
            self.wrong = letter

    def render(self,surface):
        """ On affiche le mot à chercher et l'erreur si il y en a une """
        self.string_dark = ''.join(self.dark)
        surface.blit(font.render(self.string_dark,True,(255,255,255)),(20,150))
        if self.wrong != "":
            surface.blit(font.render("Tu as déjà essayé {}".format(self.wrong),
                                     True,
                                     (255,0,0)),
                         (20,20))

def load_words(dictionary):
    """ Charge les mots d'un dictionnaire """
    if os.path.exists(dictionary): # On vérifie si le dic existe (ENCORE?)
                                   # A cause de l'importation
        filein = open(dictionary,"r") # On l'ouvre en read-only
        lines = filein.readlines() # On lit ligne par ligne et on met en liste
        for l in range(0,len(lines)):
            lines[l] = lines[l].replace("\n","") # On enlève les token newline
        filein.close()
        return lines
    else:
        print("Impossible de trouver un dictionnaire!!!")
        exit()

def clear_word(ligne):
        """ supprime les charactères non compris dans string.ascii_letters"""
        ligne_propre = ""
        accents = {'a': ['à', 'ã', 'á', 'â'],
                    'e': ['é', 'è', 'ê', 'ë'],
                    'i': ['î', 'ï'],
                    'u': ['ù', 'ü', 'û'],
                    'o': ['ô', 'ö'],
                    'y': ['ÿ'],
                    'oe': ['œ'],
                    '': ['\n']}
        # On supprime d'abord les accents
        for (char, accented_chars) in accents.items():
            for accented_char in accented_chars:
                ligne = ligne.replace(accented_char, char)
        # Puis on supprime les charactères spéciaux
        for letter in ligne:
            if letter in string.ascii_letters:
                ligne_propre += letter
        return ligne_propre.lower()

def create_new_word(Word,nbr_coups):
    list_word = []
    dark_list_word = []
    my_word = clear_word(Word) # On néttoie le bazar
    for i in my_word:
        list_word.append(i)
        dark_list_word.append(" _ ")
    new_word = word(list_word,dark_list_word,nbr_coups) # On crée notre nouveau mot
    return new_word

def ask(screen, question):
    """ ask(screen, question) -> answer """
    bg = pygame.image.load(os.path.join("data","background.jpg"))
    word_to_find = [] # Le mot que l'autre decra trouver
    while 1:
        screen.blit(bg, (0,0)) # Bg
        for e in pygame.event.get():
            if e.type == QUIT:
                exit()
            elif e.type == KEYDOWN: # Weird because AZERTY (Vive la France)
                if e.key == K_a:
                    word_to_find.append("q")
                elif e.key == K_b:
                    word_to_find.append("b")
                elif e.key == K_c:
                    word_to_find.append("c")
                elif e.key == K_d:
                    word_to_find.append("d")
                elif e.key == K_e:
                    word_to_find.append("e")
                elif e.key == K_f:
                    word_to_find.append("f")
                elif e.key == K_g:
                    word_to_find.append("g")
                elif e.key == K_h:
                    word_to_find.append("h")
                elif e.key == K_i:
                    word_to_find.append("i")
                elif e.key == K_j:
                    word_to_find.append("j")
                elif e.key == K_k:
                    word_to_find.append("k")
                elif e.key == K_l:
                    word_to_find.append("l")
                elif e.key == K_SEMICOLON:
                    word_to_find.append("m")
                elif e.key == K_n:
                    word_to_find.append("n")
                elif e.key == K_o:
                    word_to_find.append("o")
                elif e.key == K_p:
                    word_to_find.append("p")
                elif e.key == K_q:
                    word_to_find.append("a")
                elif e.key == K_r:
                    word_to_find.append("r")
                elif e.key == K_s:
                    word_to_find.append("s")
                elif e.key == K_t:
                    word_to_find.append("t")
                elif e.key == K_u:
                    word_to_find.append("u")
                elif e.key == K_v:
                    word_to_find.append("v")
                elif e.key == K_w:
                    word_to_find.append("z")
                elif e.key == K_x:
                    word_to_find.append("x")
                elif e.key == K_y:
                    word_to_find.append("y")
                elif e.key == K_z:
                    word_to_find.append("w")
                elif e.key == K_KP_ENTER or e.key == K_RETURN:
                    return ''.join(word_to_find) # Si entrer : on balance le mot
                elif e.key == K_BACKSPACE:
                    word_to_find = word_to_find[:-1] # On supprime
                else: # Faudrait vraiment être stupide...
                    screen.blit(font.render("Ceci n'est pas une lettre!!!",True,(255,255,255)),(180,10))
        screen.blit(font.render("{}_".format(''.join(word_to_find)), True, (255,255,255)), (250, 220))
        screen.blit(font.render(question ,True,(255,255,255)),(180,100))
        pygame.display.update()
