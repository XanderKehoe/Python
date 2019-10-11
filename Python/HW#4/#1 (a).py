#  Xander Kehoe Assignment #4 Problem #1 (a)
import pickle
from nation import Nation
country = {}  # Initializing Dictionary
infile = open("UN.txt", 'r')  # Opening UN.txt for reading
for line in infile:
    data = line.split(",")  # Split string into tuple by commas
    name = data[0]
    c = Nation(data[0], data[1], float(data[2]), float(data[3]))  # make individual Nation object
    country[name] = c  # add new Nation object to dictionary

with open('nationDict.dat', 'wb') as output:  # export to pickled binary file
    pickle.dump(country, output, pickle.HIGHEST_PROTOCOL)
