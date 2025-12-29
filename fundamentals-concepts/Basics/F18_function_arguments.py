'''
*agrs : Allows you to pass multiple non-key arguments ( parameters are stored in tuples)
**kwargs: : Allows you to pass muliple keyword arguments ( keyword parameters are stored in dictionary)

'''

def add(*args):
    total = 0
    for arg in args:
        total += arg
    return total

# we have flexibility to use any number of arguments
print(add(1,2,3))
print(add())
print(add(1,2,3,7,9))


#here we use any number of keyword parameters 
def school(**kwargs):

    print("------print items")
    for key, value in kwargs.items():
        print(f"{key} , {value}")
    
    print("------printing keys")
    for key in kwargs.keys():
        print(key)
    
    print("-----printing values")
    for value in kwargs.values():
        print(value)


school(classroom = "first", sub = "math", name="afn")
