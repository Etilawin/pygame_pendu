import pygame, os, sys, string

font = pygame.font.SysFont("arial",30)

class word:

    def __init__(self,text,dark):
        self.text = text
        self.dark = dark
        self.string_dark = ''.join(self.dark)
        self.string_text = ''.join(self.text)
        self.errors = 0
        self.guess = 2
        self.true_letters = []
        self.wrong_letters = []

    def update(self,letter):
        if letter not in self.true_letters and letter not in self.wrong_letters:
            found = False
            for i in range(1,len(self.text)-1):
                if self.text[i] == letter:
                    self.dark[i] = letter
                    found = True
                    self.guess += 1
                    self.true_letters.append(letter)
            if not found:
                self.errors += 1
                self.wrong_letters.append(letter)

    def render(self,surface):
        self.string_dark = ''.join(self.dark)
        surface.blit(font.render(self.string_dark,True,(0,0,0)),(20,150))

def load_words():
    if len(sys.argv) > 1:
        if os.path.exists(sys.argv[1]):
            filein = open(sys.argv[1],"r")
            lines = filein.readlines()
            for l in range(0,len(lines)):
                lines[l] = lines[l].replace("\n","")
            return lines
        else:
            if os.path.exists(os.path.join("data","dictionary.txt")):
                filein = open(os.path.join("data","dictionary.txt"),"r")
                lines = filein.readlines()
                for l in range(0,len(lines)):
                    lines[l] = lines[l].replace("\n","")
                filein.close()
                return lines
            else:
                print("Cannot find a valid dictionary!!!")
                exit()
    else:
        if os.path.exists(os.path.join("data","dictionary.txt")):
            filein = open(os.path.join("data","dictionary.txt"),"r")
            lines = filein.readlines()
            for l in range(0,len(lines)):
                lines[l] = lines[l].replace("\n","")
            filein.close()
            return lines
        else:
            print("Cannot find a valid dictionary!!!")
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

def create_new_word(Word):
    list_word = []
    dark_list_word = []
    my_word = clear_word(Word)
    for i in my_word:
        list_word.append(i)
        dark_list_word.append(" _ ")
    # dark_list_word[0] = list_word[0] # Help w/ first and last letter
    # dark_list_word[-1] = list_word[-1] # But we aren't so stupid right ;)
    new_word = word(list_word,dark_list_word)
    return new_word
