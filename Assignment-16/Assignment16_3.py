# Write a program which contains one function named as Add() which accepts two numbers from user and return addition of that two numbers.
def Add(no_1, no_2):
    return no_1 + no_2

def main():
    number_1 = int(input("Enter the First Number: "))
    number_2 = int(input("Enter the Second Number: "))
    ret = Add(number_1, number_2)
    print(f"Addition of {number_1} + {number_2} = {ret}")
    
if __name__ == "__main__":
    main()