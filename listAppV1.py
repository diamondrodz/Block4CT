"""
Program goals:
3. Pull the values stored at specific indexes
4. Covert input to INTs
5. Put all action in a while loop
6. Add an exit option 

"""
myList = []

def mainProgram():
    #build our while loop
    while True:
        print("Hello, there! Let's work with lists!")
        print("Please choose from the following options. Type the number of the choice")
        choice = input("1. Add to list, 2. Return a value in a list, or 3.   ")
        if chocie == "1":
            addToList()
        elif choice == "2":
            indexValues()
        elif choice == "3":
            break

def addToList():
    print("Adding to a list! Great choice!")
    newItem = input("Type an integer here!   ")
    myList.append(int(newItem))
    #we need to think about errors!


def indexValues():
    print("At what indec position do you want to search?")
    indexPos = input("Type an index position here:   ")
    print(myList[int(indexPos)])
    
    


if _name_ == "_main_":
    mainProgram()
