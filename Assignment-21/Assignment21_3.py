"""
Design a Python application where multiple threads update a shared variable.
1.Use a Lock to avoid race conditions.
2.Each thread should increment the shared counter multiple times.
3.Display the final value of the counter after all threads complete execution.
"""
import threading

lock = threading.Lock()

counter = 0

def increment():
    global counter
    for _ in range(100000):
        with lock:
            counter += 1

def main():
    t1 = threading.Thread(target=increment)
    t2 = threading.Thread(target=increment)
    t3 = threading.Thread(target=increment)
    t4 = threading.Thread(target=increment)
    t5 = threading.Thread(target=increment)
    t6 = threading.Thread(target=increment)

    t1.start()
    t2.start()
    t3.start()
    t4.start()
    t5.start()
    t6.start()

    t1.join()
    t2.join()
    t3.join()
    t4.join()
    t5.join()
    t6.join()

    print(counter)
 
if __name__ == "__main__":
    main()