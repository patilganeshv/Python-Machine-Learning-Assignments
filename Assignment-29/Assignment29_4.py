"""
Compare Two Files (Command Line)
Write a program which accepts two file names thorugh command line arguments and 
compare the contents of both files.
    .If both files contain the same contents, display success
    .otherwise display Failure

Input (Command Line): demo.txt  hello.txt 
Expected Output: Success / Failure
"""

import sys
import os

def compare_content(file1, file2):
    try:
        file1_obj = open(file1, "r")
        file1_content = file1_obj.read()

        file2_obj = open(file2, "r")
        file2_content = file2_obj.read()
       
        if file1_content == file2_content:
            print("Success")
        else:
            print("Failure")
        
        file1_obj.close()
        file2_obj.close()

    except Exception as e:
        print("An error occurred:", e)

def is_exists(file_name):
    if not os.path.exists(file_name):
        print(f"{file_name} does not exists")
        return False
    else:
        return True
    
def main():
    if len(sys.argv) != 3:
        print("Invalid Input")
        print("Usage: python script.py filename1 filename2")
        sys.exit(1)
    
    file1 = sys.argv[1]
    file2 = sys.argv[2]

    ret1 = is_exists(file1)
    ret2 = is_exists(file2)
    
    if ret1 and ret2:
        compare_content(file1, file2)
        
if __name__ == "__main__":
    main()

