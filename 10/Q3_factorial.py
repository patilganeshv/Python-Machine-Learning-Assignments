def calculate_factorial(num):
    fact = 1
    for i in range(1, num+1):
        fact = fact * i

    return fact

def main():
    number = int(input("Enter the number to calculate the factorial:"))
    ret = calculate_factorial(number)
    print(f"Factorial of {number} is {ret}")

if __name__ == "__main__":
    main()