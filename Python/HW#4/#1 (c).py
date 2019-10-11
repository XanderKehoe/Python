#  Xander Kehoe Assignment #4 Problem #1 (c)
import pickle
ui = input("Insert Continent: ")  # User input
infile = open("nationDict.dat", 'rb')  # Open nationDict.dat for reading
country = pickle.load(infile)  # load pickled binary file back into dictionary
newCountry = {}  # initializing dictionary of just countries belonging to user input's continent
topFive = []  # initializing tuple for top 5 countries

for key in country:  # iterate through all the countries
    if ui == country[key].getContinent():  # if country's continent matches user input
        newCountry[country[key].getName()] = country[key].popDensity()  # insert country into newCountry dictionary with
                                                                        # corresponding population density as item

for x in range(5):  # for 0.4
    inverse = [(value, key) for key, value in newCountry.items()]  # switch keys and items
    topFive.append(max(inverse)[1])  # add highest value to topFive tuple
    newCountry.__delitem__(max(inverse)[1])  # delete highest value

print(topFive)
