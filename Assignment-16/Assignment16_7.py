# Write a program which contains one function that accept one number from user and returns true if number is divisible by 5 otherwise return false.
def is_divisible_by_5(no):
    if (no % 5) == 0:
        return True
    else:
        return False

def main():
    number = int(input("Enter the Number: "))
    ret = is_divisible_by_5(number)
    print(ret)
    
if __name__ == "__main__":
    main()