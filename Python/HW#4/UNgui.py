from tkinter import *
import pickle
from nation import Nation
infile = open("UNDict.dat", 'rb')
lstUN = pickle.load(infile)

print(lstUN["Canada"]["popl"])
strListUN = sorted(list(lstUN))


def setValues(self):
    global lstUN
    selectedN = lstboxUN.get(lstboxUN.curselection())
    continent = lstUN[selectedN]["cont"]
    population = lstUN[selectedN]["popl"]
    area = lstUN[selectedN]["area"]
    conContinent.set(continent)
    conPop.set("{:,}".format(int((1000000*population))))
    conArea.set("{0:,.2f}".format(area))


window = Tk()
window.title("Members of U.N.")


# Labels
Label(window, text="Continent:").grid(row=0, column=9, padx=1, pady=1, sticky=E)
Label(window, text="Population:").grid(row=1, column=9, padx=1, pady=1, sticky=E)
Label(window, text="Area(sq. miles):").grid(row=2, column=9, padx=1, pady=1, sticky=E)

conContinent = StringVar()
entContinent = Entry(window, textvariable=conContinent, state="readonly", width=20).grid(row=0, column=10, columnspan=2, padx=1, pady=1,
                                                                                   sticky=W)
conPop = StringVar()
entPop = Entry(window, textvariable=conPop, state="readonly", width=20).grid(row=1, column=10, columnspan=2, padx=1, pady=1,
                                                                                   sticky=W)
conArea = StringVar()
entArea = Entry(window, textvariable=conArea, state="readonly", width=20).grid(row=2, column=10, columnspan=2, padx=1, pady=1,
                                                                                   sticky=W)
yscroll = Scrollbar(window, orient=VERTICAL)
yscroll.grid(row=0, column=1, rowspan=10, pady=(0,5), sticky=NS)

# List boxes
conUN = StringVar()
lstboxUN = Listbox(window, width=35, height=10, listvariable=conUN, yscrollcommand=yscroll.set)
lstboxUN.grid(row=0, rowspan=6, column=0, columnspan=1, padx=(0, 3), pady=(0, 3), sticky=NSEW)
lstboxUN.bind("<<ListboxSelect>>", setValues)

yscroll["command"] = lstboxUN.yview
# Put corresponding items into list box
conUN.set(tuple(strListUN))

window.mainloop()  # Start GUI
