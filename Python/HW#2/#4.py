# Xander Kehoe Assignment #2 Problem #4

def IsValid(i):
    try:  # Attempting conversion to check for error
        i = int(i)
    except:
        return 0
    if i > 1:  # Checking to see if value is positive
        return 1
    else:
        return 0


def GetInput():
    global i  # obtaining variable from outside of instance
    i = input("Insert Number: ")
    if IsValid(i) == 1:  # (1 == true) in this case
        i = int(i)  # Converting i to int type
        print("Value is valid, proceeding...")
    else:
        print("Invalid input, try again.")
        GetInput()


def FindPrimeFactors(i):
    primeFactors = []
    for j in range(2, i+1):
        if (i % j) == 0:
            primeFactors.append(j)
    return primeFactors


def FindLowestAndHighest(array):
    sorted(array)
    return [array[0], array[len(array)-2]]


i = None  # Initializing
GetInput()
primeFactors = FindPrimeFactors(i)
print(FindLowestAndHighest(primeFactors))



