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