#Awais guessing game

import random
while True:
    print("A. Play game")
    print("B. Quit")
    choise = input("Enter your choise A/B: ").lower()

    if choise == "b":
        print("EXIT")
        break
    elif choise == "a":
        guess = random.randint(1, 2)
        num = int(input("Enter number between (1 to 10): "))
        if num == guess:
            print("Conguratulations! your win", guess)
        else:
            print("Try again the number is ", guess)
    else:
        print("(Invalid try again)")

        
    
