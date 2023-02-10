from random import randint
import os

def clear(): os.system('cls')

#-----------------------HANGMAN----------------------
def painthangman(w,l,bl,gl):
    if len(bl) == 0:
        print("""
        .
        .
        .
        .
        .
        .
        .
        .
        .
        """)
    elif len(bl) == 1:
        print("""
        .
        .
        .
        .
        .
        .
        .
        .
        .      -----
        """)
    elif len(bl) == 2:
        print("""
        .	 
        .	 |
        .	 |
        .	 |
        .	 |
        .	 |
        .	 |
        .	 |
        .      -----
        """)
    elif len(bl) == 3:
        print("""
        .	 ________________
        .	 |
        .	 |
        .	 |
        .	 |
        .	 |
        .	 |
        .	 |
        .      -----
        """)
    elif len(bl) == 4:
        print("""
        .	 ________________
        .	 |              |
        .	 |
        .	 |
        .	 |
        .	 |
        .	 |
        .	 |
        .      -----
        """)
    elif len(bl) == 5:
        print("""
        .	 ________________
        .	 |              |
        .	 |              O
        .	 |
        .	 |
        .	 |
        .	 |
        .	 |
        .      -----
        """)
    elif len(bl) == 6:
        print("""
        .	 ________________
        .	 |              |
        .	 |              O
        .	 |              |
        .	 |
        .	 |
        .	 |
        .	 |
        .      -----
        """)
    elif len(bl) == 7:
        print("""
        .	 ________________
        .	 |              |
        .	 |              O
        .	 |             /|
        .	 |
        .	 |
        .	 |
        .	 |
        .      -----
        """)
    elif len(bl) == 8:
        print("""
        .	 ________________
        .	 |              |
        .	 |              O
        .	 |             /|\\
        .	 |
        .	 |
        .	 |
        .	 |
        .      -----
        """)
    elif len(bl) == 9:
        print("""
        .	 ________________
        .	 |              |
        .	 |              O
        .	 |             /|\\
        .	 |              |
        .	 |
        .	 |
        .	 |
        .      -----
        """)
    elif len(bl) == 10:
        print("""
        .	 ________________
        .	 |              |
        .	 |              O
        .	 |             /|\\
        .	 |              |
        .	 |             /
        .	 |
        .	 |
        .      -----
        """)
    elif len(bl) == 11:
        print("""
        .	 ________________
        .	 |              |
        .	 |             \\0/
        .	 |              |
        .	 |              |
        .	 |             / \\
        .	 |
        .	 |
        .      -----
        """)
    else: print("Many bad letters!!!!")
    #w ord,l etter,b ad_letterl,g ood_letters
    i = 0
    display_word = ""
    glc = 0
    for i in w:
        if gl.find(i) > -1: 
            display_word = display_word + i
            glc += 1
        else: display_word = display_word + "_"
    print("     Your letters:   " + display_word)
    print("     Wrong letters: "+ bl.upper())
    if len(bl) > 10: return 2
    elif len(w) == glc: return 3
    else: return 1

def get_words():
    words = []
    with open("D:/OneDrive/Programming/word_dictionary.txt","r") as f:
        for line in f:
            line = line.strip()
            words.append(line)
            #print(line)
    f.close()
    #print(words)
    return words

def hangman():
    #dictionary = ["EDIFICIO","Computador","Dinosaurio","Calculadora","Cientifico","Pensamiento","Algoritmico","Universidad","Tablero","Profesor","Ortopedia","Hanoi","Administracion","Gerencia","Miercoles","Yate","Microsoft","Curso","Talento","Beneficios","Futuro","Memoria","Encuentros","Importante","Limpieza","Escondido","Madrugada","Racionalista","Magnifico","Caudillo"]
    clear()
    print("""
    Welcome to Hangman.
    The guess letter board game!
    """)
    dictionary = get_words()
    bad_letters = ""
    good_letters = ""
    word = str(dictionary[randint(1,len(dictionary)-1)]).upper()
    cont = 1
    while cont == 1:
        letter = input("Please choose a letter: ").upper()[:1]
        if word.find(letter) == -1:
            if bad_letters.find(letter) == -1: bad_letters = bad_letters + letter
        else: 
            if good_letters.find(letter) ==-1: good_letters = good_letters + letter
        cont = painthangman(word,letter,bad_letters,good_letters)
        #cont = input("Do you want to play again? (y/n) ")
        #if cont == "y": cont = True
        #else: cont = False
    if cont == 3: print("You´ve WON!!!")
    else: print("You've Lost :-(  The word was " + word)
