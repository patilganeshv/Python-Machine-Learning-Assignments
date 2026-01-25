"""
Write a Python program to implement a class named BankAccount with the following requirements:
.The class should contain two instance variables:
    .Name (Account holder name)
    .Amount (Account balance)
.The class should contain one class variable:
    .ROI (Rate of Interest), initialized to 10.5
.Define a constructor (__init__) that accepts Name and initial Amount.
.Implement the following instance methods:
    .Display() - displays account holder name and current balance
    .Deposit() - accepts an amount from the user and adds it to balance
    .Withdraw() - accepts an amount from the user and subtracts it from balance
            (Ensure withdrawal is allowed only if sufficient balance exists)
    .CalculateInterest() - calculates and returns interest using formula:
            Interest = (Amount * ROI) / 100
Create multiple objects and demonstrate all methods.
"""
class BankAccount:
    ROI = 10.5

    def __init__(self, name, amount):
        self.name = name
        self.amount = amount

    def display(self):
        print("Account holder name:", self.name)
        print("Current balance:", self.amount)

    def deposit(self):
        deposit_amt = int(input("Enter the amount that you want to deposit in your A/C: "))
        self.amount = self.amount + deposit_amt
        print("Amount deposited successfully")

    def withdraw(self):
        withdraw_amt = int(input("Enter the amount that you want to withdraw from your A/C: "))
        
        if self.amount >= withdraw_amt:
            self.amount = self.amount - withdraw_amt
            print("Amount withraw successfully.")
        else:
            print("Insufficient balance. withdrawal not allowed")
    
    def calculate_interest(self):
        interest = (self.amount * BankAccount.ROI) / 100
        return interest    
    
obj1 = BankAccount("Ganesh", 1000)

obj1.display()
obj1.deposit()
obj1.display()
obj1.withdraw()
obj1.display()
print("Rate of Interest is:", obj1.calculate_interest())
obj1.display()