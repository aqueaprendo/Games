from ast import AsyncFunctionDef
from random import randint, random
import hangman as hm
import find_number as fn
import russiandice as rd
import triqui as tq
import memory as mem 
import tictactoe as ttt
import hanoi as hn
import concentrate as ct
#import princess as pr
#import navalbattle as nb
#import othello as ot
#import line4 as l4
import maze as mz


import os

def clear(): os.system('cls')

def triqui():
    pass

def memory():
    pass

def tictactoe():
    pass

def hanoi():
    pass

#----------------------CONCENTRATE------------------
def concentrate():
    pass

def princess():
    pass

def navalbattle():
    pass

def othello():
    pass

def line4():
    pass

def maze():
    pass

#def findnumber():


def menu_option(opt):
    if opt == 1: triqui()
    elif opt == 2: memory()
    elif opt == 3: tictactoe()
    elif opt == 4: hanoi()
    elif opt == 5: hm.hangman()
    elif opt == 6: concentrate()
    elif opt == 7: princess()
    elif opt == 8: navalbattle()
    elif opt == 9: fn.findnumber()
    elif opt == 10: othello()
    elif opt == 11: rd.russiandice()
    elif opt == 12: line4()
    elif opt == 13: maze()
    elif opt == 0: exit()
    else: print("Incorrect option")


def main():
    again = True
    menu = """
    Hello and welcome to Multiple Board Games.
    A very simple but friendly program with multiple
    games you can play by yourself.
    --------------------------------------------------------
    Please choose the game you want to play
    1: Triqui (Pendiente)
    2: Memory (Pendiente)
    3: Tic Tac Toe (Pendiente)
    4: Torres de Hanoi (Pendiente)
    5: Hangman (OK)
    6: Concentrate (Pendiente)
    7: Princess and wolfs (Pendiente)
    8: Naval Battle (Pendiente)
    9: Find the number (OK)
    10: Othello (Pendiente)
    11: Russian Dice (Pendiente)
    12: Line 4 (Sin terminar)
    13: Maze (Pendiente)
    0: Exit
    ----------------------------------------------------------
    Please select the game you want to play by typing the correspondent number:
    """
    while again:
        #clear()
        opt = int(input(menu))
        menu_option(opt)
        #print(opt)


if __name__ == '__main__':
    main()
    