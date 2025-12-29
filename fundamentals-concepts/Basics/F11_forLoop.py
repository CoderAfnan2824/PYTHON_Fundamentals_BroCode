
# 21 is exclusive, so range is from 1 to 20 with step count as 1
for x in range(1,21):
    print(f"{x} ",end="")

print()

# Now pointer moved 3 steps after each iteration
for x in range(1,21,3):
    print(f"{x} ",end="")

print()
# Now loop iterates in reverse order from 20 to 1
for x in reversed(range(1,21,3)):
    print(f"{x} ",end="")


row = int(input())
column = int(input())
s = (input())

for i in range(row):
    for j in range(0,column):
        print(s,end="")
    print()