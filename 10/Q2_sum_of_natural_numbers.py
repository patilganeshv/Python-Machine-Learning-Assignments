def sum_of_first_n_natural_numbers(num):
    sum = 0
    while (num != 0):
        sum = sum + num
        num = num - 1
    return sum

def main():
    number = int(input("Enter the number to print the sum of first N natural numbers: "))
    sum_of_num = sum_of_first_n_natural_numbers(number)
    print("Sum of first N natural numbers is:", sum_of_num)
    
if __name__ == "__main__":
    main()