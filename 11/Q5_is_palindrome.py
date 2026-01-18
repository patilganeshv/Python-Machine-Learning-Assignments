def check_palindrome(num):
    rev = 0
    while (num != 0):
        digit = num % 10
        rev = rev * 10 + digit
        num = num // 10
    return rev

def main():
    number = int(input("Enter the number: "))
    rev_number = check_palindrome(number)
    if rev_number == number:
        print(f"{number} is palindrome")
    else:
        print(f"{number} is not palindrome")


if __name__ == "__main__":
    main()