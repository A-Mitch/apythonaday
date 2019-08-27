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
    
    # gets the length, but also acts as a helper for the delNode fucntion
    def listlength(self):
        currNode = self.head
        nodeTotal = 0

        while currNode.next != None:
            nodeTotal +=1
            currNode = currNode.next 

        return nodeTotal


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

        print("lol")
    
    def printList(self):
        nodeList = []
        currNode = self.head

        while currNode.next != None:
            currNode = currNode.next
            nodeList.append(currNode.data)
        print(str(nodeList))

        



list1 = Linked_List()
list1.printList()
list1.addNode(16)
list1.addNode(13)
list1.addNode(14)
list1.addNode(15)
list1.printList()
list1.delnodeatindex(2)
list1.printList()
