def addition(num1, num2):
    return num1+num2

def subtraction(num1, num2):
    return num1-num2

def multiplication(num1, num2):
    return num1*num2

def division(num1, num2):
    return num1/num2

def main():
    no1 = int(input("Enter the first number: "))
    no2 = int(input("Enter the second number: "))

    add = addition(no1, no2)
    print(f"{no1} + {no2} = {add}")

    sub = subtraction(no1, no2)
    print(f"{no1} - {no2} = {sub}")
    
    mult = multiplication(no1, no2)
    print(f"{no1} * {no2} = {mult}")
    
    div = division(no1, no2)
    print(f"{no1} / {no2} = {div}")

if __name__ == "__main__":
    main()