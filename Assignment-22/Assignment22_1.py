"""
Write a python program to implement a class named Demo with following specifications:
    1.The class should contain two instance variable: no1, no2.
    2.The class should contain one class variable named value.
    3.Define a constructor (__init__) that accepts two parameters and initializes the instance variable
    4.Implement two instance methods:
        .Fun() - Display the values of instance variable no1 and no2.
        .Gun() - Display the value of instance variable no1 and no2.
Create two objects of the Demo class as follows:
obj1 = Demo(11, 21)
obj2 = Demo(51, 101)
call the instance methods in the given sequence:
obj1.fun()
obj2.fun()

obj2.fun()
obj2.gun()
"""
class Demo:
    value = 0

    def __init__(self, no1, no2):
        self.value_1 = no1
        self.value_2 = no2
    
    def fun(self):
        print("Instance variable no1: ", self.value_1)
        print("Instance variable no2: ", self.value_2)

    def gun(self):
        print("Instance variable no1: ", self.value_1)
        print("Instance variable no2: ", self.value_2)

obj1 = Demo(11, 21)
obj2 = Demo(51, 101)

obj1.fun()
obj2.fun()

obj1.gun()
obj2.gun()