# Write a program which accept one number from user and check whether number is prime or not.
# Input: 5       Output: It is prime NUmber

def is_prime(no):
    flag = False
    for i in range(2, no):
        if (no % i) == 0:
            flag = True
            break
    
    if flag:
        return "It is not prime number"
    else:
        return "It is prime number"

def main():
    number = int(input("Enter the Number:"))
    ret = is_prime(number)
    print(ret)

if __name__ == "__main__":
    main()