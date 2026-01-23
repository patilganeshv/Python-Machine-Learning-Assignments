# Write a program which accepts one number and prints sum of digits.
def sum_of_digits(num):
    digit_sum = 0
    while (num != 0):
        digit_sum = digit_sum + num % 10
        num = num // 10
    return digit_sum

def main():
    number = int(input("Enter the number: "))
    ret_digit_sum = sum_of_digits(number)
    print("Sum of digits is:", ret_digit_sum)

if __name__ == "__main__":
    main()