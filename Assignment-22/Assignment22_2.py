"""
Write a python program to implement a class named Circle with following requirements:
    1.The class should contain three instance variable: Radius, Area, and Circumference.
    2.The class should contain one class variable named PI  and initialized to 3.14.
    3.Define a constructor (__init__) that initializes the instance variable 0.0.
    4.Implement the following instance methods:
        .accept() - Display the radius of the circle from the user.
        .calculate_area() - calculate the area of the circle and stores it in the are variable.
        .calculate_circumference() - calculate the circumference of the circle and stores the
         circumference variable.
        .display() - display the value of radius, area and circumference.
"""
class Circle:
    PI = 3.14
    def __init__(self):
        self.radius = 0.0
        self.area = 0.0
        self.circumference = 0.0

    def accept(self):
        self.radius = float(input("Enter the radius of the circle: "))

    def calculate_area(self):
        self.area = Circle.PI * self.radius * self.radius

    def calculate_circumference(self):
        self.circumference = 2 * Circle.PI * self.radius

    def display(self):
        print("Value of Radius: ", self.radius)
        print("Value of Area: ", self.area)
        print("Value of Circumference: ", self.circumference)


obj1 = Circle()
obj2 = Circle()

obj1.accept()
obj1.calculate_area()
obj1.calculate_circumference()
obj1.display()

obj2.accept()
obj2.calculate_area()
obj2.calculate_circumference()
obj2.display()