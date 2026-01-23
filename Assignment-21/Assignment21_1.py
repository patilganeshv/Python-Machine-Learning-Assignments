"""
Design a Python application that creates two threads named Prime and NonPrime.
1.Both thread should accept a list of integers.
2.The Prime thread should display all prime numbers from the list.
3.The NonPrime thread should display all non-prime numbers from the list.
"""
import threading

def is_prime(no):
    flag = False
    for i in range(2, no):
        if (no % i) == 0:
            flag = True
            break
    
    if flag:
        return False
    else:
        return True
    

def Prime(List):
    print("All Prime Numbers:")
    for i in range(len(List)):
        if List[i] != 1:
            ret = is_prime(List[i])
            if ret:
                print(List[i], end=" ")
    print()

def NonPrime(List):
    print("All NonPrime Numbers:")
    for i in range(len(List)):
        if List[i] != 1:
            ret = is_prime(List[i])
            if not ret:
                print(List[i], end=" ")

def main():
    data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    t1 = threading.Thread(target=Prime, args=(data, ))
    t2 = threading.Thread(target=NonPrime, args=(data, ))

    t1.start()
    t2.start()

    t1.join()
    t2.join()

if __name__ == "__main__":
    main()