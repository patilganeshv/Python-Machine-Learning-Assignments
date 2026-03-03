"""
# Copy File Contents into Another File
Write a program which accept two file names from the user.
 . First file is an existing file
 . Second file is new file

 copy all contents from the first file into second file.
 INPUT: abc.txt demo.txt
"""
import sys
import os

def copy_content(src_file, dest_file):
    try:
        src_obj = open(src_file, "r")
        content = src_obj.read()

        dest_obj = open(dest_file, "w")
        dest_obj.write(content)

        print(f"Contents of {src_file} copied successfully into {dest_file}")
        src_obj.close()

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
        print("Usage: python script.py sourcefile destinationfile")
        sys.exit(1)
    
    src_file_name = sys.argv[1]
    dest_file_name = sys.argv[2]

    ret = is_exists(src_file_name)
    
    if ret:
        copy_content(src_file_name, dest_file_name)
        
if __name__ == "__main__":
    main()