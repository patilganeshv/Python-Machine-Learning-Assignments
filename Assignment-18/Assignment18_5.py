"""
Write a program which accept N numbers from user and store it into List. 
Returns addition of all prime numbers from that list. Main python file 
accepts N numbers from user and pass each number to ChkPrime() function which is
part of our user defined module named as MarvellousNum. Name of the function from python file should ListPrime().  
Input: Number of element: 11
Input Elements: 13 5 45 7 4 56 10 34 2 5 8
Output: (13 + 5 + 7 + 2 + 5) = 32
"""

import MarvellousNum

def ListPrime(l):
    sum_of_prime = 0
    for i in range(len(l)):
        is_prime = MarvellousNum.ChkPrime(l[i])
        if is_prime:
            sum_of_prime = sum_of_prime + l[i]
        
    return sum_of_prime


def main():
    no_of_elements = int(input("Enter the Number of Element: "))
    l1 = []

    for i in range(no_of_elements):
        val = int(input(f"Enter the {i} element value: "))
        l1.append(val)

    result = ListPrime(l1)
    print("Input Elements: ", l1)
    print("Addition of all prime numbers from list is: ", result)

if __name__ == "__main__":
    main()
