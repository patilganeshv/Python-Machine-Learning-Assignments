"""
# Search a Word in File
Write a Program which accepts a file name and a word from the user and
Checks whether that word is present in the file or not.

Input: 
demo.txt Marvellous

Expected Output: 
Display whether the word Marvellous is found in demo.txt or not.
"""

import sys
import os

def search_word(file_name, word):
    found = False
    try:
        f_obj = open(file_name, "r")
        for line in f_obj:
            words = line.split()
            
            if word in words:
                found = True
                break

        if found:
            print(f'"{word}" is found in {file_name}')
        else:
            print(f'"{word}" is NOT found in {file_name}')
            
        f_obj.close()

    except Exception as e:
        print("An error occurred:", e)
        sys.exit(1)

def is_exists(file_name):
    if not os.path.exists(file_name):
        print("Source file does not exists")
        return False
    else:
        return True
    
def main():
    if len(sys.argv) != 3:
        print("Invalid Input")
        print("Usage: python script.py filename word")
        sys.exit(1)
    
    file_name = sys.argv[1]
    word = sys.argv[2]

    ret = is_exists(file_name)
    
    if ret:
        search_word(file_name, word)
        
if __name__ == "__main__":
    main()