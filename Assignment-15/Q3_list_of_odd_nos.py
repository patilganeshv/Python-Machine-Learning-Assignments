# Write a lambda function using filter() which accepts a list of numbers and returns a list of odd numbers.
is_odd = lambda no: (no % 2 != 0)

def main():
    data = [10, 23, 12, 8, 9, 13, 24, 15, 27, 44]
    print("Actual data is:", data)

    filter_data = list(filter(is_odd, data))
    print("Data after filter is: ", filter_data)

if __name__ == "__main__":
    main()