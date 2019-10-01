class myQueue():
    def __init__(self,maxSize): #Constructor class method
        self.size = 0 #Initialises the variables to 0 and the maxSize as the input to the constructor method
        self.maxSize = maxSize
        self.currentQueue = []
        self.startingPointer = 0
        self.rearPointer = 0

    def enQueue(self,itemToQueue): #Procedure to add item to queue
        if (self.rearPointer+1) != self.maxSize: #Checks that the rearpointer hasn't reached the max size
            self.currentQueue.append(itemToQueue) #Appends the item to the queue list
            self.size += 1 #Adds one to the current size
            self.rearPointer +=1 #Updates the rear pointer to point to the back of the queue
            print("The new queue is: ", self.currentQueue)
        else: #Else, the queue is at its maximum size
            print("Queue reached max size!")#Displays a relevant error message to the user

    def deQueue(self): #Procedure to remove item from the queue
        if self.size !=0: #Checks that the size isn't nothing
            self.startingPointer +=1 #Adds one to the starting pointer to remove item from queue
            print("The item you have removed from the queue is: ", self.currentQueue[self.startingPointer-1]) #Prints the item removed
            self.size -=1
    def isFull(self):#Procedure to check if the queue is full
        if (self.rearPointer +1) == self.maxSize: #Checks if the rear pointer is at its maximum
            print("Queue is full!") #Size is maxsize so queue is full
        else: #Else, queue is not full
            print("Queue is not full!")

    def isEmpty(self): #Procedure to check if the queue is empty
        if self.size == 0: #Checks if there is nothing in the queue
            print("Queue is empty!") #Prints the relevant message to the user
        else:
            print("Queue is not empty!")#Else, queue is not empty!
    
    def printQueue(self):
        if self.size !=0:
            for x in range(self.startingPointer,self.startingPointer+self.size):
                print(self.currentQueue[x])
                
myQueue1 = myQueue(5) #Initialises a class object with maxSize 5

while True:#Repeats until the user quits
        choice = (input("What would you like to do? \n 1. Add an item \n 2. Remove an item \n 3. Check if the queue is full \n 4. Check if the queue is empty\n 5. Print the queue \n 6. Quit")) #Asks the user what they would like to do
        if choice in ["1","2","3","4","5","6"]: #Validates the user input against the possible options
            if choice == "1": 
                chosenItem = input("Please enter the item you want to add to the queue: ")#Takes the user input and passes it as a parameter into the procedure interface
                myQueue1.enQueue(chosenItem)
            elif choice == "2":
                myQueue1.deQueue() #Dequeues the item
            elif choice == "3":
                myQueue1.isFull()#Checks if queue is full
            elif choice == "4":
                myQueue1.isEmpty() #Checks if queue is empty
            elif choice == "5":
                myQueue1.printQueue()
            elif choice == "6": #If the user wants to quit
                break #Break the infinite loop to quit the program




