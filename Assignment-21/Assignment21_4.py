"""
Design a Python application that two threads.
1.Thread 1 should compute the sum of elements from a list.
2.Thread 2 should compute the product of elements from the same list.
3.Return the result to the main thread and display them.
"""
import threading

sum_result = 0 
product_result = 1

def sum_of_all_ele(List):
    global sum_result
    for i in range(len(List)):
        sum_result += List[i]

def product_of_all_ele(List):
    global product_result
    for i in range(len(List)):
        product_result *= List[i]

def main():
    data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    t1 = threading.Thread(target=sum_of_all_ele, args=(data, ))
    t2 = threading.Thread(target=product_of_all_ele, args=(data, ))

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print("Sum of all elements is:", sum_result)
    print("Product of all elements is:", product_result)
    
if __name__ == "__main__":
    main()