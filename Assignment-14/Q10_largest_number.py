# Write a lambda function which accepts three numbers and returns largest number.
largest_number = lambda no_1, no_2, no_3: (no_1 if no_1 > no_2 and no_1 > no_3 else no_2 if no_2 > no_3 else no_3)

def main():
    no1 = int(input("Enter the First Number: "))
    no2 = int(input("Enter the Second Number: "))
    no3 = int(input("Enter the Third Number: "))
    largest_no = largest_number(no1, no2, no3)
    print(largest_no)

if __name__ == "__main__":
    main()