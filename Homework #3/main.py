"""
Homework #3 : If Statement
Create a function that accepts 3 parameters and checks for equality between any two of them.

Function will return True if 2 or more of the parameters are equal, 
and false if none of them are equal to any of the others.
submitted by: Raju Moni Borah
"""
# function that accepts 3 parameters and checks for equality between any two of them. 
def equalifyChecker(a,b,c):
    """
    Accepts 3 interger inputs 
    """
    # converting a string to integer if any 
    a = int(a)
    b = int(b)
    c = int(c)
    if a == b or a == c or a == b:
        return True
    return False

# calling the function with 2 equal values
print(equalifyChecker("1",1,2))
# calling the function with no equal values
print(equalifyChecker("8",1,2))