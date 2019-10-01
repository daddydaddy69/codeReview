class myStack():
    def __init__(self,maxSize): #Constructor class method
        self.size = 0 #Initialises the variables to 0 and the maxSize as the input to the constructor method
        self.maxSize = maxSize
        self.currentStack = []
        self.stackPointer = 0
        for x in range(maxSize): #Goes through and initialises the list of Maxsize
            self.currentStack.append("")

    def push(self,itemToQueue): #Procedure to add item to stack
        if self.stackPointer != self.maxSize: #Checks that the rearpointer hasn't reached the max size
            self.currentStack[self.stackPointer] = (itemToQueue)  # Appends the item to the stack list
            self.stackPointer += 1  # Adds one to the current size
        else: #Else, the stack is at its maximum size
            print("Stack reached max size!")#Displays a relevant error message to the user

    def pop(self): #Procedure to remove item from the stack
        if self.stackPointer !=0: #Checks that the size isn't nothing
            self.stackPointer -=1 #Removes one from the stack pointer to point to the item below on the stack
            print("The item you have removed from the stack is: ", self.currentStack[self.stackPointer]) #Prints the item removed
        else:
            print("Couldn't remove item - Stack is empty!") #Empty Stack

    def isFull(self):#Procedure to check if the stack is full
        if self.stackPointer == self.maxSize: #Checks if the stack pointer is equal to the max size
            print("Stack is full!") #Pointer at maxsize so stack is full
        else: #Else, stack is not full
            print("Stack is not full!")

    def isEmpty(self): #Procedure to check if the stack is empty
        if self.stackPointer == 0: #Checks if the stack pointer is at the bottom of the stack
            print("Stack is empty!") #Prints the relevant message to the user
        else:
            print("Stack is not empty!")#Else, stack is not empty!

    def peek(self): #Procedure to check the item at the top of the stack
        if self.stackPointer == 0: #Checks that the stack is not empty
            print("Stack is empty!")
        else:
            print("The item on the top of the stack is: " + self.currentStack[self.stackPointer-1]) #Prints the item on the top of the stack

myStack = myStack(5) #Initialises a class object with maxSize 5

while True:#Repeats until the user quits
        choice = (input("What would you like to do? \n 1. Add an item \n 2. Remove an item \n 3. Check if the stack is full \n 4. Check if the stack is empty\n 5. Peek at the top item \n 6. Quit\n")) #Asks the user what they would like to do
        if choice in ["1","2","3","4","5","6"]: #Validates the user input against the possible options
            if choice == "1":
                chosenItem = input("Please enter the item you want to add to the stack: ")#Takes the user input and passes it as a parameter into the procedure interface
                myStack.push(chosenItem) #Pushes item onto stack
            elif choice == "2":
                myStack.pop() #Pops an item of the stack
            elif choice == "3":
                myStack.isFull()#Checks if stack is full
            elif choice == "4":
                myStack.isEmpty() #Checks if stack is empty
            elif choice == "5":
                myStack.peek()  #Looks at the item on the top of the stack
            elif choice == "6": #If the user wants to quit
                break #Break the infinite loop to quit the program




