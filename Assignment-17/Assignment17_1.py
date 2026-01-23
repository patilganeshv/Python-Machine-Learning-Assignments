"""
Create one module named as Arithmetic which contains 4 functions as Add(), Sub(),
Mult() & Div(). all functions accepts two parameters as number and perform the opetion.
Write on python program which call all the functions from Arithmetic module by accepting 
the parameters from user.
"""

import Arithmetic

result = 0
result = Arithmetic.Add(10, 20)
print("Addition is: ", result)

result = Arithmetic.Sub(10, 20)
print("Subration is: ", result)

result = Arithmetic.Mult(10, 20)
print("Multiple is: ", result)

result = Arithmetic.Div(10, 20)
print("Division is: ", result)