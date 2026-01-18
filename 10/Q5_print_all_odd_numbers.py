def print_all_odd_number(num):
    for i in range(num+1):
        if (i%2) != 0:
            print(i, end=" ")

def main():
    number = int(input("Enter the number: "))
    print_all_odd_number(number)

if __name__ == "__main__":
    main()