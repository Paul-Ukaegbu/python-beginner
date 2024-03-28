import os
import random

def guess_word():
    words = ["apple", "banana", "cherry", "date", "elderberry", "fig", "grape", "honeydew", "kiwi", "lemon", "mango", "nectarine", "orange", "pear", "quince", "raspberry", "strawberry", "tangerine", "ugli", "watermelon"]
    word = random.choice(words)
    print(word)
    attempts = 3

    while attempts > 0:
        user_guess = input("Guess a fruit: ")
        if user_guess.lower() == word:
            print("Congratulations! You guessed the word.")
            break
        else:
            attempts -= 1
            print(f"Your guess is incorrect. You have {attempts} attempts left.")
    else:
        print(f"You are out of attempts. The word was {word}")
        print("Game over!")

guess_word()