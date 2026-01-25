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