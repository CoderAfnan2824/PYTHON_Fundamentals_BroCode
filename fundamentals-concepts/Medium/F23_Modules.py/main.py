# Module: It's a file containing code which can be included in the program
#           to use it's functions

#bring whole 'mymodule' file into your program
import mymodule, math


#bring only 'adder' method from 'mymodule' file into your program
from mymodule2 import multiplier

print(mymodule.adder(7,6)) # here we need to reference module
print(multiplier(7,6))

a, b, c, d, e = 1, 2, 3, 4, 5

print(e)    # It prints e from variable, not the imported 'e'
print(math.e)   # Here it prints 'imported e'


