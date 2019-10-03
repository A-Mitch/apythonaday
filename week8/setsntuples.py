# Lists (review), tuples, and sets

# Lists - mutable 
# Exclusive list

names = ['Alex','Samantha','Jun','Ravi','Eric']
morenames = ['Jeff','Michael']
# exlcusive range print/slicing
print(names[0:3])

names.insert(1,'Jay')
print(names)

print("adding multiple values with extend")
names.extend(morenames)
print(names)

names.remove("Ravi")
print(names)

# reverse a list
names.reverse()
print(names)
# names.sort()
sortednames = sorted(names)
print(sortednames)

numlist = [7,1,3,6,5,4]
print(sum(numlist))

# Find the index of a value
print(names.index('Samantha'))

# enumerating
for index,name in enumerate(names):
    print(index,name)

print("I know "+' and '.join(names))

# Tuples - inmutable ~ Like lists

nametupe = ('Alex', 'Samantha', 'Jun', 'Ravi', 'Eric')
nametupe2 = nametupe
print(nametupe)

# Sets - returns only unique values

nameset = {'Alex', 'Samantha', 'Jun', 'Ravi', 'Eric'}
nameset2 = {'Michael', 'Jin', 'Sarah', 'Ib', 'Eric'}
print(nameset)
print("Alex" in nameset)
print(nameset.intersection(nameset2))
# like a left join
print(nameset.difference(nameset2))
print(nameset.union(nameset2))

# How to create empty versions
emptyset = set()
