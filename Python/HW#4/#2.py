#  Xander Kehoe Assignment #4 Problem #2
import pickle
print("To Professor Kandah (or whoever is grading this), I added additional some features out of boredom, "
      "hope you don't mind.")
print("Additional features include: Ability to create multiple accounts, accounts are saved to file for "
      "logging in later (even after program termination).")


class SavingsAccount:
    def __init__(self, name, balance):  # Initializer
        self.name = name
        self.balance = balance

    # getters
    def getName(self):
        return self.name

    def getBalance(self):
        return self.balance

    # Deposit/Withdrawal methods
    def makeDeposit(self, amount):
        self.balance += amount
        print("New balance is: $", self.balance)

    def makeWithdrawal(self, amount):
        if self.balance - amount > -1:  # Check to see if withdrawal will bring balance to less than 0
            self.balance -= amount
            print("New balance is: $", self.balance)
        else:
            print("Insufficient Balance (Current Balance is: $" + str(self.balance) + ")")


accounts = []
skip = 0  # Initializing bypass variable for if no accounts exist
try:
    infile = open("accounts.dat", 'rb')  # open accounts.dat for reading
    accounts = pickle.load(infile)  # load binary pickled file
except:  # if file is non-existent
    print("No accounts loaded")
    skip = 1

i = 0  # Initializer for inner loop variable
j = 0  # Initializer for outter loop variable

while j != 3:
    j = int(input("Press 1 to create an account, Press 2 to log in, Press 3 to exit: "))
    if j == 1:
        userName = input("Create Account - Insert Your Name: ")  # User Input
        if skip == 0:  # if accounts were loaded
            found = 0  # Initializer for check to see if an account was found that already existed
            for x in range(len(accounts)):
                if userName == accounts[x].getName():
                    print("Account for '" + accounts[x].getName() + "' Already Exist")
                    found = 1
            if found == 0:  # If no already existing account is found
                accounts.append(SavingsAccount(userName, 0))  # create new SavingsAccount object
                with open('accounts.dat', 'wb') as output:  # export to pickled binary file
                    pickle.dump(accounts, output, pickle.HIGHEST_PROTOCOL)
                print("Account Created for " + userName + ". Please Log in to continue.")
        else:  # Skip iterating through accounts since no accounts exist
            accounts.append(SavingsAccount(userName, 0))  # create new SavingsAccount object
            with open('accounts.dat', 'wb') as output:  # export to pickled binary file
                pickle.dump(accounts, output, pickle.HIGHEST_PROTOCOL)
            print("Account Created for " + userName + ". Please Log in to continue.")
            skip = 0
    if j == 2:
        userName = input("Log in - Insert Username: ")
        found = 0
        for x in range(len(accounts)):
            if userName == accounts[x].getName():
                found = 1
                while i != 3:
                    displayStr = ("Welcome " + accounts[x].getName() + ". Press 1 to Deposit, Press 2 to Withdraw, "
                                                                       "Press 3 to log out: ")
                    i = int(input(displayStr))
                    if i == 1:
                        amount = int(input("Insert Amount: $"))
                        accounts[x].makeDeposit(amount)
                    if i == 2:
                        amount = int(input("Insert Amount: $"))
                        accounts[x].makeWithdrawal(amount)
        i = 0
        if found == 0:
            print("Username not found.")

with open('accounts.dat', 'wb') as output:  # export to pickled binary file
    pickle.dump(accounts, output, pickle.HIGHEST_PROTOCOL)
print("Goodbye")
