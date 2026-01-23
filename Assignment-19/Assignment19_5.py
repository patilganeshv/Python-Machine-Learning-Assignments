"""
Write a program which contains filter(), map() and reduce() in it. Python application 
which contains one list of numbers. List contains the numbers which are accepted from user.
Filter should filter out all prime numbers. Map function will multiply each number by 2.
Reduce will return maximum number from that numbers.

Input List = [2, 70, 11, 10, 17, 23, 31, 77]
List after filter = [2, 11, 17, 23, 31]
List after map = [4, 22, 34, 46, 62]
Output of reduce = 62
"""
from functools import reduce

def is_prime(no):
    flag = False
    for i in range(2, no):
        if (no % i) == 0:
            flag = True
            break
    
    if flag:
        return False
    else:
        return True

def multiply(no):
    return no * 2

def maximum(no1, no2):
    if no1 > no2:
        return no1
    else:
        return no2

def main():
    data = []
    no_of_list_ele = int(input("Enter the Number of Elements in List: "))
    
    for i in range(no_of_list_ele):
        element = int(input(f"Enter the Value for {i} Element: "))
        data.append(element)
    
    f_data = list(filter(is_prime, data))    
    print(f_data)

    map_data = list(map(multiply, f_data))
    print(map_data)

    reduce_data = reduce(maximum, map_data)
    print(reduce_data)

if __name__ == "__main__":
    main()