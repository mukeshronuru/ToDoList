#Ikada number Guessing game
import random


number = random.randint(1,1000)
Guess = 0

while Guess != number:

    Guess = int(input("Enter the Number: "))

    if (Guess < number):
        print("Guess Higher!")
    elif (Guess > number):
        print("Guess Lower")
    else:
        print("Number Guessed Correctly")