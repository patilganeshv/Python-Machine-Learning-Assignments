# Write a program which accepts one number and prints cube of that number.
def calculate_cube(no):
    return no ** 3

def main():
    number = int(input("Enter the Number to calculate the cube: "))
    cubed_number = calculate_cube(number)
    print("Cube of", number, "is", cubed_number)

if __name__ == "__main__":
    main()