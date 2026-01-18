# Write a program which accepts one number and prints reverse of that number
def print_reverse_number(num):
    rev = 0
    while (num != 0):
        digit = num % 10
        rev = rev * 10 + digit
        num = num // 10
    return rev

def main():
    number = int(input("Enter the number: "))
    print("Original Number:", number)
    rev_number = print_reverse_number(number)
    print("Reverse Number:", rev_number)

if __name__ == "__main__":
    main()