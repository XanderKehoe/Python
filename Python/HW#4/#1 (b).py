#  Xander Kehoe Assignment #4 Problem #1 (b)
import pickle
ui = input("Insert U.N. Member: ")  # User input
infile = open("nationDict.dat", 'rb')  # open nationDict.dat for reading
country = pickle.load(infile)  # load binary pickled file

if ui in country:  # search for User input
    print("Information about ", ui, ":", country[ui])  # print out user input with corresponding data if it is found
else:  # User input is not found
    print("No such U.N. Member exist.")
