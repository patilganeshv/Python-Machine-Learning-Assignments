# Write a program which contains one function named as ChkNum() which accepts one parameter as numbre. If number is even then it should disply "Even number" otherwise display "Odd number" on console.
def ChkNum(no):
    if (no % 2) == 0:
        return "Even number"
    else:
        return "Odd number"

def main():
    number = int(input("Enter the Number: "))
    ret = ChkNum(number)
    print(ret)
    
if __name__ == "__main__":
    main()