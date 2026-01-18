addition = lambda no_1, no_2: no_1 + no_2

def main():
    no1 = int(input("Enter the First Number: "))
    no2 = int(input("Enter the Second Number: "))
    add = addition(no1, no2)
    print(add)

if __name__ == "__main__":
    main()