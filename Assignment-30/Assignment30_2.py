"""
# Count Words in a File
Write a program which accepts a file name from the user and counts the
 total number of words in that file.

Input: demo.txt
Output: Total number of words in demo.txt
"""
import sys
import os

def count_no_of_words(file_name):
    word_count = 0
    try:
        obj = open(file_name, "r")
        for line in obj:
            words = line.split()
            word_count += len(words)

        print(f"Total number of words in {file_name} is: {word_count}")
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
        count_no_of_words(file_name)
        
if __name__ == "__main__":
    main()