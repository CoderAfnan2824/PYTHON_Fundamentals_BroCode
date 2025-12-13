
#string indexing: it take 3 values [start, end, step]
# if [::1] it takes 1-1 steps, so all characters are returned
# if [::-1], it rever whole string

# if [::2], it skips 2-1 characters
num = '123-456-789'

print(num[1])   # 2
print(num[1:5]) # 23-4

print(num[1:])  # 23-456-789
print(num[: 5]) # 123-4

print(num[1:6:2])   #2-5
print(num[::3]) # 1-68

#reverse the string
print(num[::-1])    # 987-654-321

#negative index returns values in reverse

print(num[-2])  # 8

#print last 4 digits
print(num[-4:])

