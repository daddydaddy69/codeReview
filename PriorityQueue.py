class priorityQueue():
    def __init__(self,maxSize):#Constructor class method
        self.size = 0 #Initialises the variables to 0 and the maxSize as the input to the constructor method
        self.maxSize = maxSize
        self.currentQueue = []

    def enQueue(self,itemToQueue): #Procedure to queue an item
        if self.size !=self.maxSize: #Checks that there is still space in the queue
            self.currentQueue.append(itemToQueue) #Appends the item to the end of the list
            self.size +=1 #Adds one to the size
            self.sortList() #Calls the sorting function to sort the priority
        else: #Not space in the queue, prints appropriate message
            print("Queue at maximum capacity! Try removing an item.")

    def sortList(self): #Procedure to sort the list based on priority
        sorted = False  # We haven't started sorting yet
        while sorted == False:
            sorted = True  # Assume the list is now sorted
            for element in range(0, self.size-1): #Loops through the list size, -1 to cope with getting the next value below
                asciiVal1 = ord(self.currentQueue[element][-1].upper()) #Gets the ascii values of the last letter
                asciiVal2 = ord(self.currentQueue[element + 1][-1].upper())
                if asciiVal1 > asciiVal2:
                    sorted = False  # We found two elements in the wrong order
                    temp = self.currentQueue[element] #Swap the two items using a temp variable
                    self.currentQueue[element] = self.currentQueue[element+1]
                    self.currentQueue[element+1] = temp

    def displayQueue(self): #Procedure to display the current queue
        print("The queue is: ",self.currentQueue)

    def isFull(self): #Procedure to check if the queue is full
        if self.size == self.maxSize: #Checks if the size has reached the max
            print("Queue is full!") #Prints appropriate message
        else: #Otherwise, queue is not full
            print("Queue is not full!")

    def isEmpty(self): #Procedure to check if the queue is empty
        if self.size == 0: #If the size is at 0, the queue is empty, prints appropriate message
            print("Queue is empty!")
        else: #Otherwise, queue not empty
            print("Queue is not empty!")

    def deQueue(self,delItem): #Procedure to dequeue an item (item name provided to function)
        try: #Uses a try catch loop in case the item doesn't exist
            self.currentQueue.remove(delItem) #Tries to remove the item, if successful then:
            self.size -=1 #Minuses one from the size
            self.sortList()#Sorts the list again based on new priorities
        except: #Couldn't find the item, prints appropriate message
            print("Couldn't find item")

myQueue = priorityQueue(5)
while True:#Repeats until the user quits
        choice = (input("What would you like to do? \n 1. Add an item \n 2. Remove an item \n 3. Check if the queue is full \n 4. Check if the queue is empty\n 5. Display the Queue \n Any other key to quit...\n")) #Asks the user what they would like to do
        if choice in ["1","2","3","4","5"]: #Validates the user input against the possible options
            if choice == "1":
                chosenItem = input("Please enter the item you want to add to the queue: ")#Takes the user input and passes it as a parameter into the procedure interface
                myQueue.enQueue(chosenItem) #Enqueues a named element and sorts the list
            elif choice == "2":
                dequeueItem = input("Please enter the name of the item you want to de-queue: ")
                myQueue.deQueue(dequeueItem) #Dequeues a named element and sorts the list
            elif choice == "3":
                myQueue.isFull() # Checks if queue is full
            elif choice == "4":
                myQueue.isEmpty() #Checks if queue is empty
            elif choice == "5":
                myQueue.displayQueue()
         else:
             break #Break the infinite loop to quit the program

