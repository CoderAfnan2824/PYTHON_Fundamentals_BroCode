
# Slot machine Game

import random
symbols = ['🍊','🍉','🍒','⭐']

def print_balance():
    pass

def make_bet():
    
    return [random.choice(symbols) for _ in range(3)]

def calculate_bet(result, bet_amount):
    
    if result[0] == result[1] == result[2]:
        print(f"You Won: {result}")
        final = 0
        if result[0] == '⭐':
            final =  bet_amount * 5
        elif result[0] == '🍒':
            final = bet_amount * 4
        elif result[0] == '🍉':
            final = bet_amount * 3
        elif result[0] == '🍊':
            final = bet_amount * 2
        return final
    else:
        print(f"You Lost: {result}")
        
    return 0

def main():
    print("Welcome to Slot Machine Game: ")
    
    balance = int(input("Enter your balance for playing: "))
    is_running =True
    final_amount = 0
    while is_running and balance > 0:
        
        bet_amount = input("Enter the amount you want to bet ( q to quit): ")
    
        if not bet_amount.isdigit():
            if bet_amount == 'q':
                is_running = False
            else:
                print("Enter the valid amount. ")
        else:
            balance -= int(bet_amount)
            bet_amount = int(bet_amount)
            
            result = make_bet()
            result_amount = calculate_bet(result, bet_amount)
            if result_amount > 0:
                balance += result_amount
            final_amount +=result_amount
            
        
        print(f"Balance now : {balance}, Amount won till now: {final_amount}")
                        
    
    if final_amount > 0:
        print(f"You won ${final_amount:.2f}")
    
    print("Thanks for playing!")
    print(f"Balance left: {balance}, Amount won: {final_amount}")
    

if __name__ == "__main__":
    main()

        