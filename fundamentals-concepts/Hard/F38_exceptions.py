'''
Exception Handling: It's a way we handle/interrupt the flow of the program when any kind of error occurs

Common types of errors:
1. ZeroDivisionError: 1/0
2. TypeError: int("Pizza")
3. ValueError: 1 + "1"

Try: here we place the code which can cause error
catch: It is triggered when there's any type of exception
finally: It's executed with/without error

'''

try:
    user_input = int(input("Enter the value: "))
    print(100/user_input)
except ZeroDivisionError:
    print(" Don't give zero as input")
except ValueError:
    print("Don't give alphanumeric")
except Exception:
    print("smtg is wrong")
finally:
    print("End of program")

