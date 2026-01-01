# Hangman Game

from words import animals
import random

hangman = {0:
           ' O',
           1:
           ' |',
           2:
           '/|\\',
           3:
           ' |',
           4:
           '/ \\'
           }

print('* '*5)

for value in hangman.values():
    print(value)
print('* '*5)


def game_logic():

    answer = random.choice(animals)
    ans_length = len(answer)
    wrong_guess = 0
    guess_entries = 0
    stored_answer = ['_'] * ans_length

    game_running = True

    print('_ ' * len(answer))
    print("Guess the answer correctly : ) ")
    print(f"answer: {answer}")
    answer = list(answer)
    while game_running:

        if wrong_guess > 4:
            print("You loose. too many wrong guesses")
            game_running = False
            continue
        
        print('*'*10)
        user_input = input("Enter the correct letter: ").lower()
        guess_entries += 1

        if not user_input.isalpha() or len(user_input) > 1:
            print("Incorrect entry. Enter correct letter for guessing: ")
            continue
        
        if user_input in answer:
            
            if user_input in stored_answer:
                print("Already guessed")
                continue
            
            for i in range(ans_length):
                if answer[i] == user_input:
                    stored_answer[i] = user_input
            
            print(stored_answer)
            if(answer == stored_answer):
                print("You win!!!")
                print(f"You guessed in {guess_entries} chances")
                game_running = False
                continue

            print("You guessed the correct letter. Enter next letter")
            
        else:
            wrong_guess += 1
            print(f'You guessed wrong, {5-wrong_guess} chances left!')
            for i in range(wrong_guess):
                print(hangman.get(i))
        


def main():
    print("Welcome to Hangman Game...!")
    is_running = True

    while is_running:
        game_start = input("Enter the input to start or end the game(Y to start/N to exit): ")

        if game_start == 'Y':
            game_logic()
        elif game_start == 'N':
            print("GAME ENDED")
            is_running = False
        else:   
            print("Wrong input entered ")


if __name__ == '__main__':
    main()