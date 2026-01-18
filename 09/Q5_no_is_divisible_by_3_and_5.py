def check_divisible(no):
    if (no % 3) == 0 and (no % 5) == 0:
        return True

def main():
    val = int(input("Enter the Number: "))
    ret = check_divisible(val)
    if ret:
        print(val, "is divisible by 3 and 5")
    else:
        print(val, "is not divisible by 3 and 5")


if __name__ == "__main__":
    main()