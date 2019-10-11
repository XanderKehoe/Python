# Xander Kehoe
import random
ranNum = random.randint(1, 101) # Generating number to guess 1-100
guess = int(input("Insert an initial guess (1-100): "))

while guess != ranNum:  # Whole loop instructs user on how they should proceed
    if guess < ranNum:
        print(guess, " is to low")
    else:
        print(guess, " is to high")
    guess = int(input("Try again: "))

print(guess, " is the correct number!")  # Prints if user guesses correct number
