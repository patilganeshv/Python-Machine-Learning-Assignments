# Write a program which accepts one number and prints that many numbers in reverse order.
def print_that_many_numbers_rev_ord(num):
    while (num != 0):
        print(num, end=" ")
        num = num - 1

def main():
    number = int(input("Enter the number: "))
    print_that_many_numbers_rev_ord(number)

if __name__ == "__main__":
    main()