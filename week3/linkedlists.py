# This is where I will be practicing linked lists and playing around with how I can manipulate them.
# For me: remember to add self as the first parameter of each function in Py class

#  A linked list consists of nodes where each node contains a data field 
# and a reference(link) to the next node in the list.

# How to set up a linked list
# 1. I need a node class
# 2. I need a linked list class that houses all of my functions

# Node class

class Node:

    # Constructor that initializes a lined list 
    # self.data is the data point and self.next is the data point that we are pointing to
    def __init__(self, data = None):
        self.data = data
        self.next = None
    

class Linked_List:

    # Set up function for the linkedlist that establishes an empty head
    def __init__(self):
        self.head = Node()

    # Add
    # Create te new node with our data and traverse the linked list from our head on to see where there is
    # An empty next node and make that node where we put our new node.
    def addNode(self, data):
        newNode = Node(data)
        currNode = self.head

        while currNode.next != None:
            currNode = currNode.next
        
        currNode.next = newNode
    
    # Gets the length, but also acts as a helper for the delNode fucntion
    def listlength(self):
        currNode = self.head
        nodeTotal = 0

        while currNode.next != None:
            nodeTotal +=1
            currNode = currNode.next 

        return nodeTotal

    # Deletes node at an index
    def delnodeatindex(self,index):

        if index >= self.listlength():
            print("Out of bounds")
            return

        currIndex = 0
        currNode = self.head

        while True:
            lastNode = currNode
            currNode = currNode.next
            
            if currIndex == index:
                lastNode.next = currNode.next
                return
            
            currIndex +=1

    # Prints list
    def printList(self):
        nodeList = []
        currNode = self.head

        while currNode.next != None:
            currNode = currNode.next
            nodeList.append(currNode.data)
        print(str(nodeList))

    # This searches the list for an item
    def searchList(self,item):
        currNode = self.head
        indexNum = 0

        while currNode.next != None:
            currNode = currNode.next
            if item == currNode.data:
                print("Found the item at "+ str(indexNum))
            indexNum+=1
            
    
    # This is only for finding and replacing characters
    def findandreplace(self,char):
        currNode = self.head

        while currNode.next != None:
            currNode = currNode.next
            if char == currNode.data:
                currNode.data = chr(ord(char)+1)

    def swapnodes(self,item1,item2):

        if item1 == item2:
            return 

        #traverse and look for item1 and 2
        previ1 = None
        currNodei1 = self.head
    
        while currNodei1 != None and currNodei1.data != item1:
            previ1 = currNodei1
            currNodei1 = currNodei1.next

        
        previ2 = None
        currNodei2 = self.head

        while currNodei2 != None and currNodei2.data != item2:
            previ2 = currNodei2
            currNodei2 = currNodei2.next
        
        # print(previ2.data)
        # print(currNodei2.data)

        if currNodei1 == None or currNodei2 == None:
            print("Not found")
            return
        
        # # is there a previous node
        if previ1 != None:
            previ1.next = currNodei2
        else:
            self.head = currNodei2

        if previ2 != None:
            previ2.next = currNodei1
        else:
            self.head = currNodei1
        
        # # swap nodes
        currNodei1.next, currNodei2.next = currNodei2.next, currNodei1.next
        


list1 = Linked_List()
list1.printList()
list1.addNode(16)
list1.addNode(13)
list1.addNode(14)
list1.addNode(15)
list1.printList()
list1.delnodeatindex(2)
list1.printList()
list1.searchList(15)
list1.searchList(20)

list2 = Linked_List()
list2.addNode('a')
list2.addNode('b')
list2.addNode('c')
list2.addNode('d')
# list2.printList()
# list2.findandreplace('c')
list2.printList()

list2.swapnodes('b','c')
list2.printList()
