"""
Write a program which contains filter(), map() and reduce() in it. Python application 
which contains one list of numbers. List contains  the numbers which are accepted from user.
Filter should filter our all such numbers which greater than or equal to 70 and less than or equal to 90.
Map function will increase each number by 10. Reduce will return product of all that numbers.

Input List = [4, 34, 36, 76, 68, 24, 89, 23, 86, 90, 45, 70]
List after filter = [76, 89, 86, 90, 70]
List after map = [86, 99, 96, 100, 80]
Output of reduce = 6538752000
"""
from functools import reduce

Filter = lambda no: no >= 70 and no <= 90

Map = lambda no: no + 10

Reduce = lambda no1, no2: no1 * no2

def main():
    data = []
    no_of_list_ele = int(input("Enter the Number of Elements in List: "))
    
    for i in range(no_of_list_ele):
        element = int(input(f"Enter the Value for {i} Element: "))
        data.append(element)
    
    f_data = list(filter(Filter, data))    
    print(f_data)

    map_data = list(map(Map, f_data))
    print(map_data)

    reduce_data = reduce(Reduce, map_data)
    print(reduce_data)

if __name__ == "__main__":
    main()