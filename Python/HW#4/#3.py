#  Xander Kehoe Assignment #4 Problem #3
from tkinter import *


def calculatePayment():  # calculate command for button
    i = float(conRate.get())/100  # Converting to decimal format
    n = int(conYears.get())
    A = float(conAmount.get())

    payment = ((i/12)/(1-(1+(i/12))**(-(12*n)))) * A
    conPayment.set("$"+str(round(payment, 2)))


window = Tk()
window.title("Car Loan")

# Labels
Label(window, text="Amount of loan: ").grid(row=0, column=0, padx=5, pady=5, sticky=W)
Label(window, text="Interest rate (as %): ").grid(row=1, column=0, padx=5, pady=5, sticky=W)
Label(window, text="Number of years: ").grid(row=2, column=0, padx=5, pady=5, sticky=W)
Label(window, text="Monthly Payment: ").grid(row=4, column=0, padx=5, pady=5, sticky=W)

# Text boxes
conAmount = StringVar()
entAmount = Entry(window, textvariable=conAmount).grid(row=0, column=1, padx=5, pady=5, sticky=W)

conRate = StringVar()
entRate = Entry(window, textvariable=conRate).grid(row=1, column=1, padx=5, pady=5, sticky=W)

conYears = StringVar()
entYears = Entry(window, textvariable=conYears).grid(row=2, column=1, padx=5, pady=5, sticky=W)

conPayment = StringVar()
entPayment = Entry(window, textvariable=conPayment, state="readonly").grid(row=4, column=1, padx=5, pady=5, sticky=W)

# Button
btnCalculate = Button(window, text="Calculate Monthly Payment", command=calculatePayment).grid(row=3,
                                                                    column=0, columnspan=2, padx=25, pady=5, sticky=EW)
window.mainloop()  # Start GUI
