def print_that_many_numbers(num):
    for i in range(1, num+1):
        print(i, end=" ")

def main():
    number = int(input("Enter the number: "))
    print_that_many_numbers(number)

if __name__ == "__main__":
    main()