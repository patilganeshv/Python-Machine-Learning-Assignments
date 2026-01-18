# Write a lambda function using reduce() which accepts a list of numbers and returns the addition of all elements.
from functools import reduce

add = lambda no1, no2 : no1+no2

def main():
    data = [11, 10, 15, 20, 22, 27, 30]
    print("Actual Data is: ", data)

    reduce_data = reduce(add, data)
    print("Data after addition of each numbers: ", reduce_data)

if __name__ == "__main__":
    main()