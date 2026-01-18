multiplication = lambda no_1, no_2: no_1 * no_2

def main():
    no1 = int(input("Enter the First Number: "))
    no2 = int(input("Enter the Second Number: "))
    mult = multiplication(no1, no2)
    print(mult)

if __name__ == "__main__":
    main()