# Variable scope: It's a property where a variable is visible and accessible

# priority of scope:
'''
1. local
2. enclosed
3. global
4. built-in
'''
from math import e  # inbuilt variable

global e               # Global variable

def fun1():
    global e    # here we create local e below. but if we use in below print before declaration, I get error.
    print(e)    # to fix that error, we declare e as global
    e='2'
    
    def fun2():
        e='3'
        print(e)        #if above e is not there, it will use enclosed e from fun1 
    print(e)            # prints local      
    fun2()          


e=1
print(e)           #prints global variable 
fun1()
