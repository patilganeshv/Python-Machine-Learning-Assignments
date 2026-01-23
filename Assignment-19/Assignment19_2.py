# Write a program which contains one lambda function which accepts two parameter and return it's multiplication.
# Input: 4  3                Output: 12
# Input: 6  3                Output: 18

mult_of_two = lambda no1, no2: no1 * no2

def main():
    number_1 = int(input("Enter the  First Number: "))
    number_2 = int(input("Enter the Second Number: "))
    result = mult_of_two(number_1, number_2)
    print(f"{number_1} * {number_2} = {result}")

if __name__ == "__main__":
    main()