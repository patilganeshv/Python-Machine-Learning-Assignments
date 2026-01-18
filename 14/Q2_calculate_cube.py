# Write a lambda function which accepts one number and returns cube of that number.
calculate_cube = lambda no: no ** no

def main():
    number = int(input("Enter the Number to calculate the cube: "))
    cubed_number = calculate_cube(number)
    print("Cube of", number, "is", cubed_number)

if __name__ == "__main__":
    main()