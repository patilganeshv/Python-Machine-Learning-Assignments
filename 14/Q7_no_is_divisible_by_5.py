check_divisible = lambda no: (True if (no % 5 == 0) else False)

def main():
    val = int(input("Enter the Number: "))
    ret = check_divisible(val)
    print(ret)

if __name__ == "__main__":
    main()