# 12 / 4 / 24
# Number guessing game
import random
import sys
import time

numGuesses = 0


print("Hello, I'm thinking of a random number between 1 and 100. Can you guess it? ")
print("Please select the difficulty level:\n1. Easy (10 chances)\n2. Medium (5 chances)\n3. Hard (3 chances)")

diff = 0

while diff > 3 or diff < 1:
    diff = int(input("Enter difficulty: "))
    if diff == 1:
        numGuesses = 10
        print("You have selected Easy.")
    elif diff == 2:
        numGuesses = 5
        print("You have selected Medium.")
    elif diff == 3:
        numGuesses = 3
        print("You have selected Hard.")
    else:
        print("Please input either 1, 2, or 3.")

        

def guesser(amount):
    timer = time.time()
    guess = ""
    goal = random.randint(1, 100)
    while guess != goal:
        if amount >= 1:
            try:
                guess = int(input("Enter your guess: "))
            except ValueError:
                guesser(amount)

            if guess > goal:
                amount -= 1
                print(f"Try again, the number is less than {guess}. You have {amount} guesses left.")

            elif guess < goal:
                amount -= 1
                print(f"Try again, the number is greater than {guess}. You have {amount} guesses left.")
            else:
                print(f"Congrats, you got it! My number was {goal}!")
                finishedTime = time.time() - timer
                print(f"It took you {round(finishedTime)} seconds to guess my number.")
                main()
                break
            
            
        else:
            print(f"Sorry, you ran out of guesses! My number was {goal}.")
            main()
            break
        



def main():
    decide = input("Are you sure you want to play? ( y / n )\n")
    if decide == "y":
        while decide == "y":
            guesser(numGuesses)
            decide = input("Are you sure you want to play? ( y / n )\n")
    elif decide == "n":
        print("I'll see you next time!")
        exit()
    else:
        print("Please input y or n.")
        main()
    


main()

