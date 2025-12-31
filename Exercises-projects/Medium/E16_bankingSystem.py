
# Banking program

def show_balance():
    print(f"Your balance is ${balance:.2f}")

def deposit():
    
    amount = int(input("Enter the amount to be deposited: "))
    
    if amount < 0 or amount > 10000:
        print("Enter amount in between 0 and 10000 ")
        return 0 
    else:
        return amount

def withdrawal():
    amount = int(input("Enter the amount to be withdrawn: "))
    
    if amount > balance:
        print("Insufficient balance..! ")
        return 0 
    else:
        return amount


balance = 0
is_running = True

while is_running:
    print("Welcome to Banking:")
    print('''
        **********************
        1. Show balance
        2. Deposit Money
        3. Withdraw Money
        4. Exit
        **********************''')
    
    user_input = input("Choose the given options (1-4):")
    
    if user_input == '1':
        show_balance()
    elif user_input == '2':
        balance += deposit()
    elif user_input == '3':
        balance -= withdrawal()
    elif user_input == '4':
        is_running = False
    else:
        print("Invalid value entered. Retry..!")

print("Thanks for visiing..!")
    
    