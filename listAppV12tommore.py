"""
Program goals:
3. Pull the values stored at specific indexes
4. Covert input to INTs
5. Put all action in a while loop
6. Add an exit option 

"""
import random
myList = []


def mainProgram():
    #build our while loop
    while True:
        print("Hello, there! Let's work with lists!")
        print("Please choose from the following options. Type the number of the choice")
        choice = input("""1. Add to list,
2. Return a value in a list,
3. Add a bunch of numbers!
4. Random Search
5. Print List
5. Quit  """)
        if chocie == "1":
            addToList()
        elif choice == "2":
            indexValues()
        elif choice == "3":
            addABunch()
        elif choice == "4":
            randomSearch()
        elif choice == "5":
            print(myList)
        elif:
            break

def addToList():
    print("Adding to a list! Great choice!")
    newItem = input("Type an integer here!   ")
    myList.append(int(newItem))
    #we need to think about errors!

def addABunch():
    print("We are going to add a bunch of numbers to your list!")
    numToAdd = input ("How many new integers would you like to add?  ")
    numRange = input ("And how high would you like these numbers to go?   ")
    for x in range(0, int(numToAdd)):
        myList.append(random.randint)0, int(numRange))
    print("Your list is complete!")


def randomSearch():
    print("LOL hiii!!!")
    myList[random.randint(0, len(myList)-1)])

def linearSearch():
    print("We're going to go through this list one item at a time!")
    



def indexValues():
    print("At what index position do you want to search?")
    indexPos = input("Type an index position here:   ")
    print(myList[int(indexPos)])
    
    


if __name__ == "__main__":
    mainProgram()
