min_number = lambda no_1, no_2: (no_1 if no_1 < no_2 else no_2)

def main():
    no1 = int(input("Enter the First Number: "))
    no2 = int(input("Enter the Second Number: "))
    min_no = min_number(no1, no2)
    print(min_no)

if __name__ == "__main__":
    main()