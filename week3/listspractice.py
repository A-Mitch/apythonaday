# This is where I will be practicing lists (arrays) in Python and the operations that can be done to them

list1 = [1,2,3,4,5,6]
list2 = [6,4,3,1,5,2,29,12,1]

# Iterate through the list

def linearprint(inputlist):
    for items in inputlist:
        print(items)

# linearprint(list1)
print(list2)
def findandreplaceatindex(inputlist,num):
    for items in inputlist:
        if num == items:
            inputlist[items] = num*2

# findandreplaceatindex(list2,4)
# print(list2)

def findandreplacenum(inputlist,num):
    replace = num*2
    index = 0
    for items in inputlist:
        current = inputlist[index]
        index += 1
        if num in inputlist:
            inputlist[index] = replace
    

# findandreplacenum(list2,4)
# print(list2)
