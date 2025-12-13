
principle = -1
time = -1
rate = -1

while True:
    if principle < 0:
        print("principle should not be less than zero")
        principle = float(input("Enter principle amount in $"))
    else:
        break

while True:
    if rate < 0 or rate > 100:
        print("rate should not be less than zero or gt than 100")
        rate = float(input("Enter rate amount in (0-100)"))
    else:
        break

while True:
    if time < 0:
        print("Time should not be less than zero")
        time = float(input("Enter time in years: "))
    else:
        break

total = principle * pow((1+rate/100),time)

print(f'''
Total amount to be paid for 
principle: {principle} 
Rate: {rate} 
Time: {time} 
Final Amount: $ {total:,.2f}''')