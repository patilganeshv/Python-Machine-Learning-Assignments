# Write a lambda function which accepts two number and returns maximum number.
max_number = lambda no_1, no_2: (no_1 if no_1 > no_2 else no_2)

def main():
    no1 = int(input("Enter the First Number: "))
    no2 = int(input("Enter the Second Number: "))
    max_no = max_number(no1, no2)
    print(max_no)

if __name__ == "__main__":
    main()