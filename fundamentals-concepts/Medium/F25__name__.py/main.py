# if __name__ = __main__ :This script can be imported or used as standalone

'''
Functions and classes from this module can be used without the execution of
main block

It's used for below good reasons:
1. code if moduler
2. Code readability
3. Leaves no global variables
4. avoid unintended execution
'''

def main():
    print("this code is run from main file")
    
if __name__ == "__main__":
    main()
else:
    print("This is not run directly")


