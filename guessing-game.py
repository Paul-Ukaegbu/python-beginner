import random
import sys
import os
import time
import math

print("Hello World! This is a guessing game. \n")
print("I'm thinking of a number between 1 and 10.\n")
print("Try to guess the number in as few attempts as possible.\n")
print("Good luck!\n")

def guess_number():
    number = random.randint(1, 10) # Generate a random number between 1 and 10
    print(number)
    attempts = 3

    while attempts > 0:
        user_guess = int(input("Guess a number between 1 and 10: "))
        if user_guess == number:
            print("Congratulations! You guessed the number.")
            break
        elif user_guess < number:
            print("Your guess is too low.")
            attempts -= 1
            print(f"You have {attempts} attempts left.")
        elif user_guess > number:
            print("Your guess is too high.")
            attempts -= 1
            print("You have " + str(attempts) + " attempts left.")
        else:
            print("Invalid input. Please enter a number between 1 and 10.")
    else:
        print("You are out of attempts. The number was " + str(number))
        print("Game over!")

guess_number()