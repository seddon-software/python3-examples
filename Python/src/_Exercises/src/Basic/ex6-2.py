# Create a class that represents a bank account.  
# Add methods to allow a customer to deposit() and withdraw() money 
# and provide a method getBalance().  
# Write a test program to check out your class.

class BankAccount:
    def __init__(self, accountName):
        self.accountName = accountName
        self.balance = 0.0
        self.overdraft = 0.0
    
    def deposit(self, amount):
        self.balance += amount
        
    def withdraw(self, amount):
        newBalance = self.balance - amount
        if newBalance < self.overdraft: raise Overdrawn()
        self.balance -= amount
    
    def setOverdraft(self, amount):
        self.overdraft = amount
        
    def getBalance(self):
        return self.balance

class Overdrawn(Exception): pass

try:
    johnsAccount = BankAccount("johns")
    johnsAccount.deposit(350.00)
    johnsAccount.deposit(250.00)
    johnsAccount.deposit(500.00)
    johnsAccount.withdraw(100.00)
    print johnsAccount.getBalance()
    johnsAccount.withdraw(2000.00)
except Overdrawn:
    print "account would be overdrawn"



