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

    answer = input("Would you like to play again?\n\nAnswer: ").lower()
    if answer == 'yes' or answer == 'yea' or answer == 'y' or answer == 'yeah' or answer == 'ye':
        score = 0
        list = []
        main()
    else:
        print("Thanks for playing!")
        time.sleep(2)
        sys.exit()

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
    elif answer == 'seen' and word in list:
        print("Correct")
        list.append(word)
        score = score + 1
        print("\n" * 120)
        main()
    else:
        print("Wrong\n")
        time.sleep(2)
        again()

main()