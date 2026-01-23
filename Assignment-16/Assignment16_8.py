# Write a program which number from user and print that number of "*" on screen.
def print_star(no):
    for i in range(no):
        print("*", end=" ")

def main():
    number = int(input("Enter the Number: "))
    print_star(number)

if __name__ == "__main__":
    main()