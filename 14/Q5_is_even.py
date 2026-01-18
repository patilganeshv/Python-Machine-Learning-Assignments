# Write a lambda function which accepts one number and returns True if number is even otherwise False.
is_even = lambda no: (True if no%2 == 0 else False)
def main():
    number = int(input("Enter the Number: "))
    check_even = is_even(number)
    print(check_even)

if __name__ == "__main__":
    main()