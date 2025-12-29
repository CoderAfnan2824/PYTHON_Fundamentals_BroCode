
# help() will provide key details of the keywords. Uncomment below line if you need more details
# print(help(str))


name = input("Enter your name: ")

# name: afNan
#find length of string
print(len(name))    # 5  

#find first occurance of given literal
print(name.find('fN'))  #   1

#find last occurance of given literals
print(name.rfind('n'))  #   4

#returns -1 if not found
print(name.find('z'))   #   -1

#capitalise first letter
print(name.capitalize())    #   AfNan

#capitalise all letters
print(name.upper()) #   AFNAN

#lower all letters
print(name.lower()) #   afnan

#isdigit returns true if string contains only numerics.Else it returns false
print(name.isdigit())   # false

#isalpha returns true if it contains only alphabets. It's opposite of isdigit
print(name.isalpha())   # true

#count the number of occurances of given literal
print(name.count('n')) # 2

number = '123-456-789'

#replace first literal with second one
print(number.replace('-',' '))
