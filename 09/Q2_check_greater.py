# Write a program which contains one function ChkGreater() that accepts two numbers and prints the greater number.
def ChkGreater(no1, no2):
    if no1 > no2:
        return no1
    else:
        return no2

def main():
    no_1 = int(input("Enter the First Number: "))
    no_2 = int(input("Enter the Second Number: "))
    greater_number = ChkGreater(no_1, no_2)
    print(greater_number, "is greater")

if __name__ == "__main__":
    main()