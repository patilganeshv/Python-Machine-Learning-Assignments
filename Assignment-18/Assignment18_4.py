"""
Write a program which accept N numbers from user and store it into List. 
Accept one another number from user and return frequency of that another number.
Input: Number of element: 7
Input Elements: 13 5 45 7 4 45 34
Element to Search: 45
Output: 2
"""

def frequency_of_element(l, search):
    cnt = 0
    for i in range(len(l)):
        if l[i] == search:
            cnt += 1

    return cnt

def main():
    no_of_elements = int(input("Enter the Number of Element: "))
    l1 = []

    for i in range(no_of_elements):
        val = int(input(f"Enter the {i} element value: "))
        l1.append(val)

    search = int(input("Enter the number that you want to search in List: "))
    result = frequency_of_element(l1, search)
    print("Input Elements: ", l1)
    print("Search Element: ", search)
    print(f"Frequency of {search} is: {result}")

if __name__ == "__main__":
    main()

