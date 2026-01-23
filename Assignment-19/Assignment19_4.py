"""
Write a program which contains filter(), map() and reduce() in it. Python application 
which contains one list of numbers. List contains  the numbers which are accepted from user.
Filter should filter our all such numbers which are even.
Map function will calculate it's square. Reduce will return addition of all that numbers.

Input List = [5, 2, 3, 4, 3, 4, 1, 2, 8, 10]
List after filter = [2, 4, 4, 2, 8, 10]
List after map = [4, 16, 16, 4, 64, 100]
Output of reduce = 204
"""
from functools import reduce

even_filter = lambda no: no % 2 == 0

square_map = lambda no: no * no

addition_reduce = lambda no1, no2: no1 + no2

def main():
    data = []
    no_of_list_ele = int(input("Enter the Number of Elements in List: "))
    
    for i in range(no_of_list_ele):
        element = int(input(f"Enter the Value for {i} Element: "))
        data.append(element)
    
    f_data = list(filter(even_filter, data))    
    print(f_data)

    map_data = list(map(square_map, f_data))
    print(map_data)

    reduce_data = reduce(addition_reduce, map_data)
    print(reduce_data)

if __name__ == "__main__":
    main()