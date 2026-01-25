"""
Write a Python program to implement a class named Arithmetic with the following characteristics:
.The class should contain two instance variables: Value1 and Value2.
.Define a constructor (__init__) that initializes all instance variables to 0.
.Implement the following instance methods:
    .Accept() - Accepts values for Value1 and Value2 from the user.
    .Addition() - Returns the addition of Value1 and Value2.
    .Subtraction() - Returns the subtraction of Value1 and Value2.
    .Multiplication() - Returns the multiplication of Value1 and Value2.
    .Division() - Returns the division of Value1 and Value2
                (handle division by zero properly).
Create multiple objects of the Arithmetic class and invoke all the instance methods.
"""

class Arithmatic:
    value = 0

    def __init__(self):
        self.value_1 = 0
        self.value_2 = 0
    
    def accept(self):
        self.value_1 = int(input("Enter the first value: "))
        self.value_2 = int(input("Enter the second value: "))

    def addition(self):
        return self.value_1 + self.value_2
    
    def subtraction(self):
        return self.value_1 - self.value_2
    
    def multiplication(self):
        return self.value_1 * self.value_2
    
    def division(self):
        try:
            return self.value_1 // self.value_2
        except ZeroDivisionError as zobj:
            return zobj
        
    # def division(self):
    #     if self.Value2 == 0:
    #         return "Division by zero is not allowed"
    #     return self.Value1 / self.Value2
    
    
obj1 = Arithmatic()
obj2 = Arithmatic()

obj1.accept()
print(f"Addition of {obj1.value_1} and {obj1.value_2} is:", obj1.addition())
print(f"Subtraction of {obj1.value_1} and {obj1.value_2} is:", obj1.subtraction())
print(f"Multiplication of {obj1.value_1} and {obj1.value_2} is:", obj1.multiplication())
print(f"Division of {obj1.value_1} and {obj1.value_2} is:", obj1.division())

obj2.accept()
print(f"Addition of {obj2.value_1} and {obj2.value_2} is:", obj2.addition())
print(f"Subtraction of {obj2.value_1} and {obj2.value_2} is:", obj2.subtraction())
print(f"Multiplication of {obj2.value_1} and {obj2.value_2} is:", obj2.multiplication())
print(f"Division of {obj2.value_1} and {obj2.value_2} is:", obj2.division())