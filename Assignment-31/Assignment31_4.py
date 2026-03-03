"""
Design automation script which accept two directory names and one file extension.Copy all files with the 
specified extension from first directory into second directory.
Second directory should be created at run time.

Usage: DirectoryCopyExt.py Demo Temp .exe
Demo is name of directory which is existing and contains files in it. we have to create new directory
as Temp and copy all files with extension .exe from Demo to Temp.
"""
import sys
import os
import shutil

def directory_copy_ext(src_dir, dest_dir, extension):
    if not os.path.exists(dest_dir):
        os.mkdir(dest_dir)
        print(f"Destination directory '{dest_dir}' created successfully.")
    else:
        print(f"Destination directory '{dest_dir}' already exists.")

    count = 0
    for file in os.listdir(src_dir):
        src_path = os.path.join(src_dir, file)
        
        # Copy only files with given extension
        if os.path.isfile(src_path) and file.endswith(extension):
            dest_path = os.path.join(dest_dir, file)
            shutil.copy(src_path, dest_path)
            print(f"Copied: {src_path} -> {dest_path}")
            count += 1

    if count == 0:
        print("No files found with given extension.")
    else:
        print(f"\nTotal files copied: {count}")

def is_directory(dir_name):
    if not os.path.isdir(dir_name):
        print("Source directory does not exist")
        return False
    else:
        return True

def main():
    if len(sys.argv) != 4:
        print("Invalid Input")
        print("Usage: python script.py source_directory destination_directory extension")
        sys.exit(1)
    
    src_dir = sys.argv[1]
    dest_dir = sys.argv[2]
    extension = sys.argv[3]

    ret = is_directory(src_dir)
    if ret:
        directory_copy_ext(src_dir, dest_dir, extension)

if __name__ == "__main__":
    main()