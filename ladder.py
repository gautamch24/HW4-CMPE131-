
def climbFunction(n):
    n= int(input("Please enter a number of steps"))
    if (n == 0):
        return 1
    elif(n < 0):
        return 0
    else:
        return climbFunction(n-2) + climbFunction(n-1)

