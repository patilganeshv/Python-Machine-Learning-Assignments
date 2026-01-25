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