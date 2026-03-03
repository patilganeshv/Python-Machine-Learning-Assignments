"""
Design automation script which accept directory name and file extension from user.
and Display all files with that extension.

Usage: DirectoryFileSearch.py Demo .txt
Demo is name of directory and .txt is the extension that we want to search.
"""
import sys
import os

def directory_file_search(dir_name, extension):
    fobj = open("log.txt", "w")
    found = False
    for foldername, subfolders, filenames in os.walk(dir_name):
        for file in filenames:
            if file.endswith(extension):
                # print(os.path.join(foldername, file))
                fobj.write(os.path.join(foldername, file))
                fobj.write("\n")
                found = True

    if not found:
        print("No files found with given extension.")

def is_directory(dir_name):
    if not os.path.isdir(dir_name):
        print(f"Directory '{dir_name}' does not exist")
        return False
    else:
        return True

def main():
    if len(sys.argv) != 3:
        print("Invalid Input")
        print("Usage: python script.py directoryname extension")
        sys.exit(1)
    
    dir_name = sys.argv[1]
    extension = sys.argv[2]

    ret = is_directory(dir_name)
    if ret:
        directory_file_search(dir_name, extension)

if __name__ == "__main__":
    main()