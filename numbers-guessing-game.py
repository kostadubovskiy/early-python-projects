"""
Write a program that implements a simple guessing game. The computer will randomly select an integer between 0 and 100
(inclusive), and the user will repeatedly try to guess the computer's number. The computer will tell the player whether
her guess is too high or too low, and will tell the user when she's guessed the exact number. The program should also
output the number of guesses that it took the player to guess the correct number.

A sample run of the game is below. Your program doesn't have to look exactly like this -- you're encouraged to add
features to make it more fun.

I'm thinking of a number between 0 and 100
Enter your guess: 50
Sorry, 50 is too low.
Enter your guess: 70
Sorry, 70 is too high.
Enter your guess: 62
Sorry, 62 is too high.
Enter your guess: 53
Sorry, 53 is too low.
Enter your guess: 57
Good job! 57 is my number.
It took you 5 guesses.
"""
import random


def guessing_game():
    guesses = 0
    num = random.randint(0, 100)

    while True:

        guess = input("Enter your guess: ")

        if guess != num:
            guesses += 1

            if guess < num:
                print("Sorry, " + str(guess) + " is too low")

            elif guess > num:
                print("Sorry, " + str(guess) + " is too high")

        else:
            print("Good job! " + str(num) + " is my number")
            break

guessing_game()
