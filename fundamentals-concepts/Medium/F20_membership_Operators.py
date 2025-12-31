'''
membership operators: Its used to test whethet the value/variables is present in the given 
sequence.

The types of sequence: List, Tuple, Set, Dictionary, String

Types:  1. in
        2. not in

'''

email = "coderafnan2824@gmai.com"

if '@' in email and '*' not in email and '.' in email:
    print("valid email")
else:
    print("Invalid email")


dic = {"afn":"A+",
       "sam":"S",
       "abhi":"A"}

for student in dic:
    print(f"{student}'s grade is {dic[student]}")