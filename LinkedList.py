class LinkedListNode():
    def __init__(self,data,nextNodePointer=None): #Init method with the data and the next pointer
        self.data = data #Assigns the default variables
        self.nextNodePointer = nextNodePointer #Sets the next node pointer to the nextnode variable if supplied

    def getNextNode(self): #Getter method for getting the pointer of the next node
        return self.nextNodePointer #returns the nextNode Pointer data structure

    def setNextNode(self,nodePointer): #Setter method for setting the pointer of the next node
        self.nextNode = nodePointer #Sets the next node pointer to the pointer supplied in the interface

    def getNodeData(self): #Getter method for getting the data associated with a node
        return self.data #Returns the data implied against that node

    def setNodeData(self,data): #Setter method for setting the data associated with a node
        self.data = data #Sets the data to the parameter in the interface

class LinkedList(): #LinkedList class
    def __init__(self,headPointer = None): #Headpointer set default to none
        self.headPointer = headPointer
        self.size = 0 #Assigns the headpointer and size

    def getSize(self): #Getter method for getting the size of the linked list
        return self.size

    def enqueueItem(self,dataToAdd): #Procedure for adding an item to the linked list
        newNode = LinkedListNode(dataToAdd,self.headPointer) #Creates a new node with the pointer to another node and the data
        self.headPointer = newNode #Assigns the variables and adds one to the size
        self.size += 1
        print("Item queued successfully!") #Prints a message to the user

    def displayQueue(self): #Procedure for displaying the queue
        print("The queue is: ")
        newPointer = self.headPointer #Sets the start pointer to the head
        while newPointer: #While there are still nodes
            print(newPointer.getNodeData()) #Prints the node data
            newPointer = newPointer.getNextNode() #Gets the next node from the pointer

    def dequeueItem(self,dataToRemove): #Procedure from dequeueing an item
        currentNode = self.headPointer #Sets the current node to the start of the linked list
        previousNode = None #Sets the previous node to none for the start of the list
        while currentNode: #While there are still nodes,
            if currentNode.getNodeData() == dataToRemove: #Checks to see if the node data matches the data the user wants to remove
                if previousNode: #If the data matches, and the item is not at the start of the list
                    previousNode.setNextNode(currentNode.getNextNode()) #Sets the previous node to the next node, removing the current node
                else: #At the start of the list
                    self.headPointer = currentNode #Sets the head pointer to the second node in the list
                self.size -= 1 #Adjusts the size variable
                return True #Returns the function to stop further unneccesary execution
            else: #Data doesn't match
                previousNode = currentNode #Sets the previous to the current
                currentNode = currentNode.getNextNode() #Sets the current to the next node
        return False #Returns to stop unneccesary execution of code

    def findDataItem(self,dataItem): #Procedure for checking whether an item is in the linked list
        currentNode = self.headPointer #Sets the current node to the head pointer (start of linked list)
        while currentNode: #While there are more nodes
            if currentNode.getNodeData() == dataItem: #Checks if the node data is equal to the data the user wants to find
                print("Data in list!")
                return
            else: #Current node doesn't contain data user is looking for
                currentNode = currentNode.getNextNode() #Adjusts the current node
        print("No item with that name found") #Once it gets through the whole list, the item hasn't been found and an appropriate message is shown
    
