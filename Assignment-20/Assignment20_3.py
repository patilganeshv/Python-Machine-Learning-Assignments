"""
Design a python application that creates two threads named EvenList and OddList.
1.Both thread should accept a list of integers as input.
2.The EvenList thread should:
    .Extract all even elements from the list.
    .Calculate and display thier sum.
3.The OddList thread should:
    .Extract all odd elements from the list.
    .Calculate and display thier sum.
4.Threads should run concurrently.
"""
import threading
import time

def EvenList(List):
    sum = 0
    for i in range(len(List)):
        if (List[i] % 2) == 0:
            sum = sum + List[i]

    print("Sum of all even numbers:", sum)

def OddList(List):
    sum = 0
    for i in range(len(List)):
        if (List[i] % 2) != 0:
            sum = sum + List[i]
    
    print("Sum of all odd numbers is:", sum)

def main():
    start_time = time.time()
    
    data = [2, 3, 4, 5, 6, 7, 8, 9, 10]

    t1 = threading.Thread(target=EvenList, args=(data, ))
    t2 = threading.Thread(target=OddList, args=(data, ))
    
    t1.start()
    t2.start()

    t1.join()
    t2.join()
    
    end_time = time.time()
    
    print(f"Todal time required: {end_time-start_time}")

if __name__ == "__main__":
    main()