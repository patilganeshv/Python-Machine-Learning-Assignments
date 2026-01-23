# Write a lambda funtion using filter() which accepts a list of numbers and returns a list of numbers divisible by both 3 and 5.
is_divisible = lambda no: (no % 3 == 0 and no % 5 == 0)

def main():
    data = [10, 15, 12, 8, 30, 13, 24, 27, 40, 50]
    print("Actual data is:", data)

    filter_data = list(filter(is_divisible, data))
    print("List of numbers which is divisible by 3 and 5: ", filter_data)

if __name__ == "__main__":
    main()