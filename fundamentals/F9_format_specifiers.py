#format-specifier: {value:flag} formats the value based on the type of flag inserted

price1 = 3.14
price2 = -98.45
price3 = 12.66

#precision and decimals
print(f"price1 is {price1:10}") #add extra 10 spaces infront of price1
print(f"price2 is {price2:10.3f}") #add 10 extra space and 3 decimals
print(f"price3 is {price3:.4f}") #add 4 decimals

#Justification
print("+++++ Justification ++++++")
print(f"price3 is ${price3:<10}") #left justification
print(f"price3 is ${price3:>10}") #right justification
print(f"price3 is ${price3:^10}") #centre justification

#signs
print("++++ signs +++++")
print(f"price3 is ${price3:+}") #add positive sign and no sign for negatiev numbers
print(f"price3 is ${price3:-}") #add no sign for positive numbers jusification
print(f"price3 is ${price3: }") # add space for sign
print(f"price3 is ${price3:+10}") # 

#commas
price3 = 89424
print(f"price3 is ${price3:,}") # add commas for every three digits

#Combination of all 
print(f"price3 is ${price3:>+10,}") # positivr number right justified with 10 digit spacing






