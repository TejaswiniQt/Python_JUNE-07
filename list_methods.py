#list methods


# append()
'''
list1 = ['apple','orange','banana']
print(list1)
list1.append('grapes')
print(list1)
'''

# copy()
'''
list1 = [10,20,30,40]
list2 = []
print(list1)
print(list2)
list2 = list1.copy()
print(list1)
print(list2)
print(id(list1))
print(id(list2))
'''


# clear()
'''
list1 = [10,20,30,40,50]
print(list1)
list1.clear()
print(list1)
'''

# count()
'''
list1 = [1,2,4,5,6,1,5,3,6,9,5,7]
print(list1)
print(list1.count(5))
'''


# extend()
'''
list1 = [10,20,30,40]
print(list1)
list1.extend([50,60])
print(list1)
'''


# index()
'''
list1 = [10,20,30,40,50]
print(list1.index(30))
'''


# insert()
'''
list1 = [10,20,30,40,50]
print(list1)
list1.insert(3,80)
print(list1)
'''


# pop()
'''
list1 = [10,20,30,40,50]
print(list1)
print(list1.pop())
print(list1)
'''

# remove()
'''
list1 = [10,20,30,40,50]
print(list1)
list1.remove(30)
print(list1)
'''


# reverse()
'''
list1 = [10,20,30,40,50]
print(list1)
list1.reverse()
print(list1)
'''

# sort()
'''
list1 = [50,60,35,10,95,12]
print(list1)
list1.sort()
print(list1)
'''


# min() and max()

list1 = [45,62,85,12,10,56]
print(list1)
print(min(list1))
print(max(list1))
