def multiplication_table(num):
    for i in range(1, 11):
        print(num*i, end=" ")

def main():
    number = int(input("Enter the Number to print the table: "))
    multiplication_table(number)

if __name__ == "__main__":
    main()