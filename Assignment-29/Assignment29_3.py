"""
Copy file contents into a New File (Command Line)
Write a program which accepts an existing file name thorugh command line arguments, 
create a new file named demo.txt and copies all contents from the given file into demo.txt

Input (Command Line): abc.txt
Output: Create demo.txt and copy contents of abc.txt into demo.txt
"""
import sys
import os

def copy_content(source_file):
    try:
        # Open source file in read mode
        src_obj = open(source_file, "r")
        data = src_obj.read()

        # Create demo.txt and write content
        dest_obj = open("demo.txt", 'w')
        dest_obj.write(data)

        print(f"{source_file} File content copied successfully into demo.txt")
        src_obj.close()

    except Exception as e:
        print("An error occurred:", e)

def is_exists(file_name):
    if not os.path.exists(file_name):
        print(f"{file_name} does not exists")
        return False
    else:
        return True
    
def main():
    if len(sys.argv) != 2:
        print("Invalid Input")
        print("Usage: python script.py existing_filename")
        sys.exit(1)
    
    source_file = sys.argv[1]

    ret = is_exists(source_file)
    
    if ret:
        copy_content(source_file)

if __name__ == "__main__":
    main()

