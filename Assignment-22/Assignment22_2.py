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