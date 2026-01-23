# Write a program which accepts one number and prints binary equivalent.
def calculate_binary_equivalent(num):
    binary_equivalent = ""
    while (num != 0):
        rem = num % 2
        binary_equivalent = str(rem) + binary_equivalent
        num = num // 2
    
    return binary_equivalent

def main():
    number = int(input("Enter the Number: "))
    bin_equivalent = calculate_binary_equivalent(number)
    print(f"Binary Equivalent of {number} is: {bin_equivalent}")

if __name__ == "__main__":
    main()