'''
List Comprehension: It's a concise and compact way to create collections
'''

#Example 1 to create list in concise way
list1 = [3,5,6,7,8,9]
list2 = [ x * 2 for x in range(1,10)]
list3 = [x * 2 for x in list2]
list4 = [ x **2 for x in [1,2,3,4]]

print(list3)


# example 2 to create upper_names set
names = {"afn","sam","abhi"}
upper_names = {x.upper() for x in names}
print(upper_names)

# with if case
nums = [2,7,4,1,6,8,0]
even_nums = [x for x in nums if x % 2 == 0]
print(even_nums)