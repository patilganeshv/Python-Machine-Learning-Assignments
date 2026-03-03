"""
# Count Lines in a File
Write a program which accepts a file name from the user and counts how many
lines are present in the file.

Input: demo.txt
Output: Total number of lines in demo.txt
"""

import sys
import os

def count_no_of_lines(file_name):
    line_count = 0
    try:
        obj = open(file_name, "r")
        for line in obj:
            line_count += 1

        print(f"Total number of lines in {file_name} is: {line_count}")
        obj.close()

    except Exception as e:
        print("An error occurred:", e)
        sys.exit(1)

def is_exists(file_name):
    if not os.path.exists(file_name):
        print(f"{file_name} does not exists")
        return False
    else:
        return True
    
def main():
    if len(sys.argv) != 2:
        print("Invalid Input")
        print("Usage: python script.py filename")
        sys.exit(1)
    
    file_name = sys.argv[1]

    ret = is_exists(file_name)
    
    if ret:
        count_no_of_lines(file_name)
        
if __name__ == "__main__":
    main()