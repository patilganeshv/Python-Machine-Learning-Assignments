# Write a lambda function using map() which accepts a list of numbers and returns a list of squares of each number.
square = lambda no : (no * no)

def main():
    data = [11,10,15,20,22,27,30]
    print("Actual Data is: ", data)

    map_data = list(map(square, data))
    print("Data after after calculate of each number is: ", map_data)

if __name__ == "__main__":
    main()