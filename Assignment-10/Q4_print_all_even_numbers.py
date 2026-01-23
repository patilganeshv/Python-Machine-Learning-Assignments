# Write a program which accepts one number and prints all even numbers till that number.
def print_all_even_number(num):
    for i in range(2, num+1):
        if (i%2) == 0:
            print(i, end=" ")

def main():
    number = int(input("Enter the number: "))
    print_all_even_number(number)

if __name__ == "__main__":
    main()