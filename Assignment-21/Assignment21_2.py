"""
Design a Python application that creates two threads.
1.Thread 1 should calculate and display the maximum element from an list.
2.Thread 2 should calculate and display the minimum element from the same list.
3.The list should be accepted from the user.
"""
import threading

def max_element(List):
    max_no = List[0]
    for i in range(len(List)):
        for j in range(i, len(List)):
            if List[i] < List[j]:
                max_no = List[j]
    print("Maximum Element: ", max_no)

def min_element(List):
    min_no = List[0]
    for i in range(len(List)):
        for j in range(i, len(List)):
            if List[i] > List[j]:
                min_no = List[j]
    print("Minimum Element: ", min_no)
    
def main():
    data = list()
    no_of_element = int(input("Enter the number of element: "))

    for i in range(no_of_element):
        element = int(input(f"Enter the value of {i} element: "))
        data.append(element)

    t1 = threading.Thread(target=max_element, args=(data, ))
    t2 = threading.Thread(target=min_element, args=(data, ))

    t1.start()
    t2.start()

    t1.join()
    t2.join()

if __name__ == "__main__":
    main()