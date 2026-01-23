# Write a program which accepts one number and checks whether it is peferct number or not.
def check_perfect(num):
    sum_of_div = 0
    for i in range(1, num):
        if (num % i) == 0:
            sum_of_div = sum_of_div + i
    return sum_of_div

def main():
    number = int(input("Enter the Number: "))
    is_perfect = check_perfect(number)
    if is_perfect == number:
        print(f"{number} is perfect number")
    else:
        print(f"{number} is not perfect number")

if __name__ == "__main__":
    main()