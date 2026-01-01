'''
Match case(switch): It helps prevent use of so many if statements
'''

def is_day(day):
    match day:
        case 1:
            return "It's Monday"
        case 2: 
            return "It's Tuesday"
        case 3:
            return "It's Wednesday"
        case 4:
            return "It's Thursday"
        case 5:
            return "It's Friday"
        case 6:
            return "It's Saturday"
        case 7:
            return "It's Sunday"
        case _: # It's default case
            return "Invalid entry"
        
def is_weekend(day):
    match day:
        case 1 | 2 | 3 | 4 | 5:
            return False
        case 6 | 7:
            return True
        case _:
            return -1
        

print(is_day(9))
print(is_weekend(7))
        