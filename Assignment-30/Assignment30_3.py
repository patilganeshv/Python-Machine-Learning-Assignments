"""
# Display file Line by Line
Write a program which accepts a file name from the user and display the 
contents of the file line by line on the screen.

Input: demo.txt
Output: Display each line of demo.txt one by one.
"""

import sys
import os

def display_content_line_by_line(file_name):
    try:
        obj = open(file_name, "r")
        for line in obj:
            print(line, end="")

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
        display_content_line_by_line(file_name)
        
if __name__ == "__main__":
    main()