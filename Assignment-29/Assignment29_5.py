"""
Frequency of a string in file
Write a program which accepts a file name and one string from the user and returns the
frequency (count of occurences) of that string in the file.

Input (Command Line): demo.txt  Marvellous 
Expected Output: Count how many time "Marvellous" appears in demo.txt
"""

import sys
import os

def count_of_occurences(file_name, search_string):
    count = 0
    try:
        obj = open(file_name, "r")
        for line in obj:
            count += line.count(search_string)

        print(f'"{search_string}" appears {count} time(s) in {file_name} file')
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
    if len(sys.argv) != 3:
        print("Invalid Input")
        print("Usage: python script.py filename string")
        sys.exit(1)
    
    file_name = sys.argv[1]
    search_string  = sys.argv[2]

    ret = is_exists(file_name)
    
    if ret:
        count_of_occurences(file_name, search_string)
        
if __name__ == "__main__":
    main()