"""
Write a Python program to implement a class named Numbers with the following specifications:
.The class should contain one instance variable:
    .Value
.Define a constructor (__init__) that accepts a number from the user and initializes Value.
.Implement the following instance methods:
    .ChkPrime() - returns True if the number is prime, otherwise returns False
    .ChkPerfect() - returns True if the number is perfect, otherwise returns False
    .Factors() - displays all factors of the number
    .SumFactors() - returns the sum of all factors
        (You may use this method as a helper in ChkPerfect() if required)
Create multiple objects and call all methods.
"""
class Numbers:
    def __init__(self):
        self.value = int(input("Enter the number: "))

    def check_prime(self):
        if self.value <= 1:
            return False

        for i in range(2, self.value):
            if self.value % i == 0:
                return False
        return True

    def factors(self):
        print(f"Factors of {self.value} are:")
        for i in range(1, self.value + 1):
            if self.value % i == 0:
                print(i, end=" ")
        print()

    def sum_factors(self):
        factors_sum = 0
        for i in range(1, self.value):
            if self.value % i == 0:
                factors_sum += i
        return factors_sum

    def check_perfect(self):
        return self.sum_factors() == self.value

obj1 = Numbers()
print("Is Prime:", obj1.check_prime())
obj1.factors()
print("Is Perfect:", obj1.check_perfect())

print("------------------")

obj2 = Numbers()
print("Is Prime:", obj2.check_prime())
obj2.factors()
print("Is Perfect:", obj2.check_perfect())
