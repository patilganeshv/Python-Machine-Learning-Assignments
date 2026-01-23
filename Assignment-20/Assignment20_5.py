"""
Design a python application that creates two threads named Thread1 and Thread2.
1.Thread1 should display numbers from 1 to 50.
2.Thread2 should display numbers from 50 to 1 in reverse order.
3.Ensure that:
    . Thread2 starts execution only after Thread1 has completed.
4.Use appropriate thread synchronization.
"""
import threading

def one_to_fifty():
    for i in range(1, 51):
        print(i, end=" ")
    print()
    
def fifty_to_one():
    for i in range(50, 0, -1):
        print(i, end=" ")

def main():

    t1 = threading.Thread(target=one_to_fifty)
    t2 = threading.Thread(target=fifty_to_one)

    t1.start()
    t1.join()
    
    t2.start()
    t2.join()

if __name__ == "__main__":
    main()