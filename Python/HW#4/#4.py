#  Xander Kehoe Assignment #4 Problem #4
from tkinter import *
r = 0  # initializing
n = 0  # initializing


def setRates(event):
    global r
    selectedR = lstRates.curselection()  # gets selected index in rates list box
    try:  # Removes annoying error message that doesn't effect program performance
        r = rates[selectedR[0]]
    except:
        zero = 0  # do nothing


def setPeriods(event):
    global n
    selectedP = lstPeriods.curselection()  # gets selected index in periods list box
    try:  # Removes annoying error message that doesn't effect program performance
        n = {
            0: 1,
            1: 2,
            2: 4,
            3: 12,
            4: 52,
        }[selectedP[0]]
    except:
        zero = 0  # do nothing


def calculate():
    global r
    global n
    amount = 10000*(1+(r/n))**(5*n)  # Raw final number
    strAmount = '{:0,.2f}'.format(amount)  # Format with commas and 2 decimal places
    conAmount.set("$"+strAmount)  # Put number (with $) into textbox


window = Tk()
window.title("Investment")

# Labels
Label(window, text="Invest $10,000").grid(row=0, column=1, padx=1, pady=1, sticky=EW)
Label(window, text="Interest \n rate:").grid(row=1, column=0, padx=1, pady=1, sticky=EW)
Label(window, text="Compound \n Periods:").grid(row=1, column=1, padx=1, pady=1, sticky=W)

# Tuples for list boxes
rates = [0.02, 0.025, 0.03, 0.035, 0.04]  # Actual decimal values for rates
strRates = ["2%", "2.5%", "3%", "3.5%", "4%"]  # String format for display of rates
periods = ["annually", "semi-annually", "quarterly", "monthly", "weekly"]

# List boxes
conRates = StringVar()
lstRates = Listbox(window, width=5, height=5, listvariable=conRates)
lstRates.grid(row=2, column=0, padx=1, pady=1, sticky=NS)
lstRates.bind("<<ListboxSelect>>", setRates)

conPeriods = StringVar()
lstPeriods = Listbox(window, width=10, height=5, listvariable=conPeriods)
lstPeriods.grid(row=2, column=1, padx=1, pady=1, sticky=NS+W)
lstPeriods.bind("<<ListboxSelect>>", setPeriods)

# Put corresponding items into list box
conRates.set(tuple(strRates))
conPeriods.set(tuple(periods))

# Button
btnCalculate = Button(window, text="Calculate \n amount \n After 5 \n Years", command=calculate).grid(row=2, column=2,
                                                                                            padx=1, pady=1, sticky=NS+W)
# Final label/read-only textbox
Label(window, text="Amount after 5 years:").grid(row=3, column=0, columnspan=2, padx=1, pady=1, sticky=E)
conAmount = StringVar()
entAmount = Entry(window, textvariable=conAmount, state="readonly", width=10).grid(row=3, column=2, padx=1, pady=1,
                                                                                   sticky=E)
window.mainloop()  # Start GUI
