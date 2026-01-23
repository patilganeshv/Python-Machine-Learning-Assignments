# Write a lambda funtion using filter() which accepts a list of numbers and returns the product of all elements.

from functools import reduce

product_element = lambda a, b: a * b

def main():
    data = [11, 21, 51]
    print("Actual Data is:", data)

    reduce_data = reduce(product_element, data)
    print("Product of all elements in List is:", reduce_data)

if __name__ == "__main__":
    main()
