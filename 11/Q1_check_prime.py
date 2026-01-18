# Write a program which accepts one number and checks whether it is prime or not.
flag = False

def check_prime(num):
    global flag
    for i in range(2, num):
        if (num % i) == 0:
            flag = True
            break

def main():
    global flag
    number = int(input("Enter the number to check whether it is prime or not:"))
    check_prime(number)
    if flag:
        print(f"{number} is not prime")
    else:
        print(f"{number} is prime")

if __name__ == "__main__":
    main()