# This is for practicing the stack data structure a LIFO structure

# These are my push(add to stack) and pop (remove from stack methods).
def push(mylist,num):
    mylist.append(num)

def pop(mylist):
    mylist.pop()

# This prints my stack in an actual stack fashion
def printlist(mylist):
    counter = 0
    if mylist == []:
        print("the list is empty")
    
    for index in mylist:
        print(str(mylist[counter]))
        counter+=1
    
    print("^ This is the top of the stack")


# This gives the length of the stack
def stacklength(mylist):
    counter = 0
    if mylist == []:
        print("There is nothing in the stack")
    
    for index in mylist:
        counter += 1
    
    print("The length of the stack is: "+ str(counter))
    return counter

# Allows you to see what is at the top of the stack
def stackpeek(mylist):
    if mylist != []:
        print("The top of the stack is "+str(mylist[-1]))
        # I return just incase I need to use it in another function
        return mylist[-1]

# These two methods allow you to search by a number or by an index
def searchbynum(mylist,num):
    counter = 0
    if mylist == []:
        print("There is nothing in the stack")
    
    for index in mylist:
        if num == mylist[counter]:
            print("Found "+ str(num)+ " at stack index: "+ str(counter))
        counter += 1


def searchbyindex(mylist, index):
    counter = 0
    length = int(stacklength(mylist))
    if index > length:
        print("Index is out of range") 

    if mylist == []:
        print("There is nothing in the stack")

    for idx in mylist:
        if index == counter :
            print("At index " + str(index) +
                  " is value: " + str(mylist[counter]))
        counter += 1


list1 = []
print(list1)
push(list1,4)
print(list1)
pop(list1)
print(list1)
printlist(list1)

push(list1, 4)
push(list1, 5)
push(list1, 3)
push(list1, 2)
printlist(list1)

pop(list1)

printlist(list1)
stacklength(list1)
searchbynum(list1,5)
searchbyindex(list1,0)
stackpeek(list1)
searchbynum(list1,12)
