from random import randint
import os

def clear(): os.system('cls')

def russiandice():
    print("""
    --- Russian Dice!!! ---

    You must achieve the highest number you can adding every number you get but the 1.
    if a 1 is achieve, you lose everything.
    You can stop at any time to save the score.
    Type 'y' to roll the dice or 'n' to stop
    """)
    record = score = 0
    cont = another_time = "y"
    while another_time == "y":
        while cont == "y":
            print("\nThe actual record is " + str(record))
            roll = randint(1,6)
            print("The roll was " + str(roll))
            if roll != 1:
                score = score + roll
                print("Your actual score is now: " + str(score))
            else:
                score = 0
                print("Sorry, you lose your score. Start again")
            print("Your score was:  " + str(score))
            cont = input("""
                Do you want to continue?
                Type 'y' to roll the dice or 'n' to stop.  
                If your score is higher than the actual record, it will be the new record.
                You option: """)
            while cont != "y" and cont != "n":
                cont = input("You must type only 'y'or 'n'.  Do you want to continue? (y/n): ")
        if score > record: 
            record = score
            print("You have achieve a new record!!!")
        else:
            print("Your score is not high enough :-(")
        score = 0
        another_time = input("Do you want to play again? (y/n) ")
        while another_time != "y" and another_time != "n":
            another_time = input("You must type only 'y'or 'n'.  Do you want to continue? (y/n): ")
        if another_time == "y":
            cont = "y"
    print("Bye!\n")