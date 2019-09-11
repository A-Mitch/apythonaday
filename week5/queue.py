# This is where I will be practicing the queue data structure

# Enqueue (add to the queue) and dequeue (remove from the data structure)

def enqueue(mylist,num):
    mylist.insert(0,num)

def dequeue(mylist):
   del mylist[-1]

def printqueue(mylist):
    counter = 0

    print("last item inserted")
    for idx in mylist:
        print(str(mylist[counter]))
        counter+=1

    print("^ first item inserted")




list1 = []
enqueue(list1,4)
print(list1)
enqueue(list1, 5)
print(list1)
dequeue(list1)
print(list1)
enqueue(list1, 6)
enqueue(list1, 19)
enqueue(list1, 2)
enqueue(list1, 7)
enqueue(list1, 3)
print(list1)
printqueue(list1)
