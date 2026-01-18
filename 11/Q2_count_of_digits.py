def count_of_digits(num):
    cnt = 0
    while (num != 0):
        cnt = cnt + 1
        num = num // 10
    return cnt

def main():
    number = int(input("Enter the number: "))
    ret = count_of_digits(number)
    print("Count of digits is:", ret)

if __name__ == "__main__":
    main()