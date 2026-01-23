"""
Design a python application that creates two threads named EvenFactor and OddFactor.
1.Both thread should accept one integer number as a parameter.
2.The EvenFactor thread should:
    .Identify all even factors of the given number.
    .Calculate and display the sum of even factors.
3.The OddFactor thread should:
    .Identify all odd factors of the given number.
    .Calculate and display the sum of odd factors.
4.After both threads complete execution, the main thread should display the message
    "Exit from main".
"""
import threading

def EvenFactor(no):
    sum_of_even_factors = 0
    for i in range(1, no):
        if (no % i) == 0 and (i % 2) == 0:
            sum_of_even_factors += i
    
    print("Sum of all even factors is: ", sum_of_even_factors)

def OddFactor(no):
    sum_of_odd_factors = 0
    for i in range(1, no):
        if (no % i) == 0 and (i % 2) != 0:
            sum_of_odd_factors += i
    
    print("Sum of all odd factors is: ", sum_of_odd_factors)

def main():
    t1 = threading.Thread(target=EvenFactor, args=(12, ))
    t2 = threading.Thread(target=OddFactor, args=(12, ))

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print("Exit from main")


if __name__ == "__main__":
    main()