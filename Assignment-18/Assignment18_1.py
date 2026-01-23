"""
Write a program which accept N numbers from user and store it into List. Returns addition of all elements from that List.
Input: Number of element: 6
Input Elements: 13 5 45 7 4 56
Output: 130
"""

def sum_elements(l):
    Sum = 0
    for i in range(len(l)):
        Sum = Sum + l[i]

    return Sum

def main():
    no_of_elements = int(input("Enter the Number of Element: "))
    l1 = []

    for i in range(no_of_elements):
        val = int(input(f"Enter the {i} element value: "))
        l1.append(val)

    result = sum_elements(l1)
    print("Addition of List Elements is: ", result)

if __name__ == "__main__":
    main()

