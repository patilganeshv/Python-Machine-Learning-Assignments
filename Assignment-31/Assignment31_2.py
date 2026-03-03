"""
Design automation script which accept directory name and two file extensions from user.
Rename all files with first file extension with second file extention. 

Usage: DirectoryRename.py Demo .txt .doc
Demo is name of directory and .txt is the extension that we want to search and rename with .doc.
After execution this script each .txt file gets renamed as .doc.
"""

import sys
import os

def extension_rename(dir_name, old_ext, new_ext):
    count = 0
    for foldername, subfolders, filenames in os.walk(dir_name):
        for file in filenames:
            if file.endswith(old_ext):
                old_file = os.path.join(foldername, file)
                
                new_name = file.replace(old_ext, new_ext)
                new_file = os.path.join(foldername, new_name)

                os.rename(old_file, new_file)
                print(f"Renamed: {old_file} -> {new_file}")
                count += 1

    if count == 0:
        print("No files found with given extension.")
    else:
        print(f"\nTotal files renamed: {count}")

def is_directory(dir_name):
    if not os.path.isdir(dir_name):
        print(f"Directory '{dir_name}' does not exist")
        return False
    else:
        return True

def main():
    if len(sys.argv) != 4:
        print("Invalid Input")
        print("Usage: python script.py directoryname oldextension newextension")
        sys.exit(1)
    
    dir_name = sys.argv[1]
    old_ext = sys.argv[2]
    new_ext = sys.argv[3]

    ret = is_directory(dir_name)
    if ret:
        extension_rename(dir_name, old_ext, new_ext)

if __name__ == "__main__":
    main()
