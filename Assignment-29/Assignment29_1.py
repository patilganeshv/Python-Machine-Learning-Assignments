"""
-> Check File Exists in Current Directory
Write a program which accepts a file name from the user and checks whether that file
exists in the current directory or not.

Input: demo.txt
Output: Display whether demo.txt exists or not.
"""
import os

def is_exists(file_name):
    if os.path.exists(file_name):
        return True

def main():
    file_name = input("Enter the File Name: ")
    ret = is_exists(file_name)
    
    if ret:
        print(f"{file_name} is exists")
    else:
        print(f"{file_name} is not exists")

if __name__ == "__main__":
    main()