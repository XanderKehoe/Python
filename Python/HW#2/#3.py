# Xander Kehoe Assignment #2 Problem #3

import math


def IsValid(h, v):
        try:  # Attempting conversion to check for error
            h = int(h)
            v = int(v)
        except:
            return 0
        if (h > 0) & (v > 0):  # Checking to see if values are positive
            return 1
        else:
            return 0


def GetInput():
    global h  # obtaining variable from outside of instance
    global v  # obtaining variable from outside of instance
    h = input("Insert Initial Height (feet): ")
    v = input("Insert Initial Velocity (ft/s): ")
    if IsValid(h, v) == 1:  # (1 == true) in this case
        v = int(v)  # Converting v to int type
        h = int(h)  # Converting h to int type
        print("Values are valid, proceeding...")
    else:
        print("Invalid input, try again.")
        GetInput()


def GetMaxHeight(h, v):
    maxHeightTime = v/32  # Time till max height
    maxHeight = h + (v*maxHeightTime) - (16*(maxHeightTime**2))
    print("Maximum Height is: ", round(maxHeight, 2), "ft.")


def GetAirTime(h, v):
    t = 0.1
    height = h + (v*t) - (16*(t**2))
    while height > 0:
        height = h + (v*t) - (16*(t**2))
        t += 1
    # or for a more accurate time, solving algebraically
    newT = round(math.sqrt((h+(v*t))/16), 2)  # Set height = 0, and move everything but "t" to the other side the Eq.

    print("Time till ball hits the ground is approximately: ", t, "s")
    print("A more accurate time is: ", newT, "s")


# Initializing Variables
h = None  # h is initial height not current height.
v = None

GetInput()
print("")  # Space

GetMaxHeight(h, v)
print("")  # Space
GetAirTime(h, v)
