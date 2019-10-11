# Xander Kehoe
abr = (input("Insert State Abbreviation: ").upper())  # Get input and capitalize all letters
print("")  # Space
infile = open("Colleges.txt", 'r')  # Open file for reading
for line in infile:  # Iterate through each line
    data = line.split(",")
    if data[1] == abr:  # Find if line corresponds to user input
        print(data[0], ",", data[2])  # Print out corresponding college with year
