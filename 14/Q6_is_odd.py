is_odd = lambda no: (True if no%2 != 0 else False)
def main():
    number = int(input("Enter the Number: "))
    check_odd = is_odd(number)
    print(check_odd)

if __name__ == "__main__":
    main()