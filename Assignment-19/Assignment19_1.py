# Write a program which contains one lambda function which accepts one parameter and return power of two.
# Input: 4                  output: 16
# Input: 6                  Output: 64

power_of_two = lambda no: (2 ** no)

def main():
    number = int(input("Enter the Number: "))
    result = power_of_two(number)
    print(result)

if __name__ == "__main__":
    main()