class myQueue():
    def __init__(self,maxSize):#Constructor class method
        self.size = 0 #Initialises the variables to 0 and the maxSize as the input to the constructor method
        self.maxSize = maxSize
        self.currentQueue=[] #Initialises the list current queue
        for x in range(maxSize): #Goes through the list and adds an empty space to avoid errors in circular queue
            self.currentQueue.append('')
        self.startingPointer = 0
        self.rearPointer = -1 #Rear pointer set to -1 so first item in queue is 0

    def enQueue(self,itemToQueue):#Procedure to add item to queue
        if self.size != self.maxSize:#Checks that the size isn't the max size
            current = self.rearPointer +1 #Takes the mod of current pointer position +1 by maxSize to calculate the circular queue pointers next position
            newItemPointer = current % self.maxSize
            self.rearPointer = newItemPointer #Sets the rear pointer to this new index position
            self.currentQueue[newItemPointer] = itemToQueue #Sets the item in that position to the new item the user wants to queue
            print("The new queue is: ", self.currentQueue) #Prints the new queue out to the user
            self.size +=1 #Adds one to the current size
        else: #Else, the queue is at its maximum size
            print("Queue reached max size! Try removing an item...")#Displays a relevant error message to the user
            
    def deQueue(self):#Procedure to remove item from the queue
        if self.size !=0: #Checks that the list isn't empty
            current = self.startingPointer #Uses the same method as above to calculate new index pointer position
            newItemPointer = current % self.maxSize
            self.startingPointer = newItemPointer
            print("The item you have removed from the queue is: ", self.currentQueue[current]) #Prints the item removed from the queue
            self.size -=1 #Minuses one from the size
            
    def isFull(self): #Procedure to check if the queue is full
        if self.size == self.maxSize: #Checks if the size is at its maximum
            print("Queue is full!") #Size is maxsize so queue is full
        else: #Else, queue is not full
            print("Queue is not full!")
            
    def isEmpty(self): #Procedure to check if the queue is empty
        if self.size == 0: #Checks if there is nothing in the queue
            print("Queue is empty!")#Prints the relevant message to the user
        else:
            print("Queue is not empty!")#Else, queue is not empty!

myQueue1 = myQueue(5)#Initialises a class object with maxSize 5

while True:#Repeats until the user quits
        choice = (input("What would you like to do? \n 1. Add an item \n 2. Remove an item \n 3. Check if the queue is full \n 4. Check if the queue is empty\nAny other key = quit \n")) #Asks the user what they would like to do
        if choice in ["1","2","3","4"]:#Validates the user input against the possible options
            if choice == "1":
                chosenItem = input("Please enter the item you want to add to the queue: ")#Takes the user input and passes it as a parameter into the procedure interface
                myQueue1.enQueue(chosenItem)
            elif choice == "2":
                myQueue1.deQueue()#Dequeues the item
            elif choice == "3":
                myQueue1.isFull()#Checks if queue is full
            elif choice == "4":
                myQueue1.isEmpty()#Checks if queue is empty
        else:
            break




