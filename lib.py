import pygame, os, sys, string

font = pygame.font.SysFont("arial",30)

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
    new_word = word(list_word,dark_list_word,nbr_coups) # On créer notre nouveau mot
    return new_word
