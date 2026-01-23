# Write a program which accept one number from user and return it's factorial.
# input: 5          output: 120

def factorial(no):
    fact = 1
    while (no!=0):
        fact = fact * no
        no = no - 1
    return fact

def main():
    number = int(input("Enter the Number:"))
    ret = factorial(number)
    print(f"factorial of {number} is: {ret}")

if __name__ == "__main__":
    main()