"""
Design a python application that creates two sepatrate threds named Even and Odd.
1.The Even thread should display the first 10 even numbers.
2.The Odd thread should display the first 10 odd numbers.
3.Both threads should execute independently using threading module.
4.Ensure proper thread creation and execution.
"""
import threading

def first_10_even_no():
    count = 0
    even = 2

    while count < 10:
        print(even, end=" ")
        even += 2
        count += 1
    print()

def first_10_odd_no():
    count = 0
    odd = 1

    while count < 10:
        print(odd, end=" ")
        odd += 2
        count += 1
    print()

def main():
    t1 = threading.Thread(target=first_10_even_no)
    t2 = threading.Thread(target=first_10_odd_no)

    t1.start()
    t2.start()

    t1.join()
    t2.join()


if __name__ == "__main__":
    main()