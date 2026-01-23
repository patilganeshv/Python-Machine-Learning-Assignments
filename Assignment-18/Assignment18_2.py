"""
Write a program which accept N numbers from user and store it into List. Returns maximum number from that list
Input: Number of element: 7
Input Elements: 13 5 45 7 4 56 34
Output: 56
"""

def max_element(l):
    max_no = l[0]
    for i in range(len(l)):
        for j in range(i, len(l)):
            if l[i] > l[j]:
                max_no = l[i]

    return max_no

def main():
    no_of_elements = int(input("Enter the Number of Element: "))
    l1 = []

    for i in range(no_of_elements):
        val = int(input(f"Enter the {i} element value: "))
        l1.append(val)

    result = max_element(l1)
    print("Input Elements: ", l1)
    print("Maximum Element from List is: ", result)

if __name__ == "__main__":
    main()

