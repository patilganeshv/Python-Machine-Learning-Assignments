"""
Design a python application that creates three threads named Small, Capital and Digits.
1.All threads should accept a string as input.
2.The Small thread should count and display the number of lowercase characters.
3.The Capital thread should count and display the number of upercase characters.
4.The Digits thread should count and display the number of numeric digits.
5.Each thread must also display:
    . Thread ID
    . Thread Name
"""
import threading

def Small(input_str):
    print("Small() Thread ID: ", threading.get_ident())
    print("Small() Thread Name: ", threading.current_thread().name)
    lowercase_cnt = 0
    for ch in input_str:
        if ch >= 'a' and ch <= 'z':
            lowercase_cnt += 1
    
    print("Lowercase Character in Input String is: ", lowercase_cnt)


def Capital(input_str):
    print("Capital() Thread ID: ", threading.get_ident())
    print("Capital() Thread Name: ", threading.current_thread().name)
    uppercase_cnt = 0
    for ch in input_str:
        if ch >= 'A' and ch <= 'Z':
            uppercase_cnt += 1
    
    print("Uppercase Character in Input String is: ", uppercase_cnt)

def Digits(input_str):
    print("Digits() Thread ID: ", threading.get_ident())
    print("Digits() Thread Name: ", threading.current_thread().name)
    numeric_digits_cnt = 0
    for ch in input_str:
        if ch >= '0' and ch <= '9':
            numeric_digits_cnt += 1

    print("Numeric Digits in Input String is: ", numeric_digits_cnt)

def main():
    data = input("Enter the String: ")

    t1 = threading.Thread(target=Small, args=(data, ))
    t2 = threading.Thread(target=Capital, args=(data, ))
    t3 = threading.Thread(target=Digits, args=(data, ))

    t1.start()
    t2.start()
    t3.start()

    t1.join()
    t2.join()
    t3.join()
    
if __name__ == "__main__":
    main()