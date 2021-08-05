"""
Homework #4 : Lists
Create a global variable called myUniqueList. It should be an empty list to start.

Next, create a function that allows you to add things to that list. 
Anything that's passed to this function should get added to myUniqueList, 
unless its value already exists in myUniqueList. 
If the value doesn't exist already, it should be added and the function should return True. 
If the value does exist, it should not be added, and the function should return False;

Finally, add some code below your function that tests it out. 
It should add a few different elements, showcasing the different scenarios, and then finally it should print the value of myUniqueList to show that it worked.

Extra Credit:
Add another function that pushes all the rejected inputs into a separate global array called myLeftovers. 
If someone tries to add a value to myUniqueList but it's rejected (for non-uniqueness), 
it should get added to myLeftovers instead.
submitted by: Raju Moni Borah
"""
# global variable
myUniqueList = []
myLeftovers = []

# function that allows you to add things to myUniqueList


def addItem(item):
    # checking if item is not there in list if true then insert value to myUniqueList otherwise call the myUniqueList function
    if item not in myUniqueList:
        myUniqueList.append(item)
        return True
    else:
        leftOverItems(item)
    return False

# function that allows you to add things to myLeftovers that are rejected from the myUniqueList


def leftOverItems(item):
    myLeftovers.append(item)


# adding items
addItem(1)
addItem(12)
addItem(11)
addItem(12)
addItem(1)
addItem("hello")
addItem("hello")
addItem("hello")

# priting myUniqueList
print("myUniqueList : ", myUniqueList)
# priting myLeftovers
print("myLeftovers : ", myLeftovers)
