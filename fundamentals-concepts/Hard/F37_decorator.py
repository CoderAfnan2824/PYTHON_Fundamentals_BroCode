'''
Decorator; A function that extends the behaviour of another function without
        modifying the base function. 

        base function is given as argument 
'''


def get_chocos(func):
    #below wrapper will wrap base function around another function. This is called as closure
    def wrapper(*args, **kwargs):
        print("cherries have been added")
        func(*args, **kwargs)
    return wrapper

@get_chocos # if we use this line, we modify our base function without actually chaning the code
#If we don't mention above line, the base function behaves like the older version
def get_icecream(flavour):
    return f"Here is your {flavour} ice-Cream"


print(get_icecream("Vanilla"))