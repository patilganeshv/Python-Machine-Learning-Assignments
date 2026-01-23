# Write a program which one number from user and check whether that number is positive or negative or zero.
def ChkNum(no):
    if no > 0:
        return "Positve number"
    elif no < 0:
        return "Negative number"
    else:
        return "Zero"

def main():
    number = int(input("Enter the Number: "))
    ret = ChkNum(number)
    print(ret)
    
if __name__ == "__main__":
    main()