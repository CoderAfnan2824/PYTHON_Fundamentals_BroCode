# Rock Paper Scissor Game

import random

choices = ["rock", "paper", "scissor"]

computer = random.choice(choices)

player_point = 0
coumputer_point = 0

counter = 0

while True:
    print("Lets start Rock Paper Scissor Game:")
    counter += 1
    
    player = input("Enter your choice [rock, paper, scissor] or q to quit: ").lower()
    
    if player == 'q':
        break
    elif player not in choices:
        print("Enter correct Value")
    elif player == computer:
        print("It's a tie")
        player_point += 1
        coumputer_point += 1
    elif player == "scissor" and computer == "paper":
        print("you win this")
        player_point += 1
    elif player == "paper" and computer == "rock":
        print("you win this")
        player_point += 1
    elif player == "rock" and computer == "scissor":
        print("You win this")
        player_point += 1
    else:
        print(f"You loose this, computer choose {computer}")
        coumputer_point += 1
        
print(f"After {counter} rounds, the winner is: ", end=" ")

if(player_point > coumputer_point):
    print("You")
elif player_point < coumputer_point:
    print("Computer")
else:
    print("Both")


print("Thanks for playing!")