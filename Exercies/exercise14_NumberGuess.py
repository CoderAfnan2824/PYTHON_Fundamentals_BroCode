# Number Guessing Game
import random

low = 1
high = 100

number = random.randint(low, high)

guess = 0
still_guessing = True

print("NUMBER GUESSING GAME...!")
number_guess = (input("Enter correct Guess: "))

while still_guessing:

    
    if number_guess.isdigit():
        number_guess = int(number_guess)
        if number_guess > number:
            print("Too high..!")
            guess += 1
            number_guess = (input("Enter correct Guess: "))
        elif number_guess < number:
            print("Too low..!")
            guess += 1
            number_guess = (input("Enter correct Guess: "))
        else:
            guess += 1
            print("Guessed Correct number : )")
            print(f"Total guesses took: {guess}")
            still_guessing = False
    else:
        print("Invalid number entered.")
        number_guess = (input("Enter correct Guess between 1 and 100: "))
    
