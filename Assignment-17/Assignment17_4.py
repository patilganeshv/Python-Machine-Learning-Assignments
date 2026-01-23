# Write a program which accept one number from user and return addition of its factors.
# input: 12     Output: 16   (1+2+3+4+6)

def factor_sum(no):
    fact_sum = 0
    for i in range(1, no):
        if (no % i) == 0:
            fact_sum = fact_sum + i
    return fact_sum

def main():
    number = int(input("Enter the number: "))
    ret = factor_sum(number)
    print("Addition of factors is: ", ret)

if __name__ == "__main__":
    main()