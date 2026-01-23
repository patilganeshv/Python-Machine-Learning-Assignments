# Write a program which accept one number and display below pattern.
# input: 5

def print_pattern(no):
    while (no != 0):
        print("*  " * no)
        no = no - 1

def main():
    no = int(input("Enter the Number: "))
    print_pattern(no)

if __name__ == "__main__":
    main()