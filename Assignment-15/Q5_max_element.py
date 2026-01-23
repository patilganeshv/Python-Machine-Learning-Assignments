# Write a lambda function using reduce() which accepts a list of numbers and returns the maximum elements.
from functools import reduce

max_element = lambda a, b: a if a > b else b

def main():
    data = [11, 10, 155, 20, 22, 27, 30]
    print("Actual Data is:", data)

    reduce_data = reduce(max_element, data)
    print("Maximum element in List is:", reduce_data)

if __name__ == "__main__":
    main()
