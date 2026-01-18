# Write a program which accepts one number and print its factors.
def print_factors(num):
    for i in range(1, num+1):
        if (num % i) == 0:
            print(i, end=" ")

def main():
    number = int(input("Enter the Number: "))
    print_factors(number)

if __name__ == "__main__":
    main()