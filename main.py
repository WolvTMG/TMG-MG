import sys
import time
import random

words = ["Assistance", "Fled", "Bread", "Escape", "Police", "Chicken", "Rice",
"Carpet", "Cheese", "Cake", "Factory", "Orange", "Juice", "Water", "Watermelon",
"Ice", "Ice Cream", "Laboratory", "Knife", "Gun", "Arm", "Armed", "Legacy"]

list = []
score = 0

def again():
    global score
    global list

    print("\n" * 120)
    print("Wrong\n")

    answer = input("Would you like to play again?\n\nAnswer: ").lower()
    if answer == 'yes' or answer == 'yea' or answer == 'y' or answer == 'yeah' or answer == 'ye':
        score = 0
        list = []
        main()
    elif answer == 'no' or answer == 'nah' or answer == 'naah' or answer == 'nein' or answer == 'nien' or answer == 'nahh':
        print("Thanks for playing!")
        time.sleep(2)
        sys.exit()
    else:
        print("\n" * 120)
        e = input("Please input a valid argument")
        again()

def main():
    global score

    word = random.choice(words)
    print("\n" * 120)
    print("Score:", score, "\n")
    print(word)
    
    answer = input("Is this word new or seen?\n\n     (New) (Seen)\n\nChoice: ").lower()
    if answer == 'new' and word not in list:
        print("Correct")
        list.append(word)
        score = score + 1
        print("\n" * 120)
        main()
    elif answer == 'new' and word in list:
        again()
    elif answer == 'seen' and word in list:
        print("Correct")
        list.append(word)
        score = score + 1
        print("\n" * 120)
        main()
    elif answer == 'seen' and word not in list:
        again()
    else:
        print("Please input a valid argument\n")
        time.sleep(2)
        main()

def start():
    print("\n" * 120)
    print("""
 ________  ________  __  ________
/_  __/  |/  / ___/ /  |/  / ___/
 / / / /|_/ / (_ / / /|_/ / (_ / 
/_/ /_/  /_/\___/ /_/  /_/\___/  
""")
    ready = input("\n\n\n\nStart\nCredits\n\nChoice: ").lower()

    if ready == 'start':
        main()
    elif ready == 'credits':
        print("\n" * 120)
        e = input("All coded by WolvTMG#0945\n\nPress [Enter] to return")
        print("\n" * 120)
        start()
    else:
        print("\n" * 120)
        e = input("Please input a valid argument")
        print("\n" * 120)
        start()

start()
