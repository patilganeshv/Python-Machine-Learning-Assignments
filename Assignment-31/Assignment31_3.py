"""
Design automation script which accept two directory names.Copy all files from first directory 
into second directoy. Second directory should be created at runtime. 

Usage: DirectoryCopy.py Demo Temp
Demo is name of directory which is existing and contains files in it. we have to create new directory
as Temp and copy all files from Demo to Temp.
"""
import sys
import os
import shutil

def directory_copy(src_dir, dest_dir):
    if not os.path.exists(dest_dir):
        os.mkdir(dest_dir)
        print(f"Destination directory '{dest_dir}' created successfully.")
    else:
        print(f"Destination directory '{dest_dir}' already exists.")

    count = 0
    for file in os.listdir(src_dir):
        src_path = os.path.join(src_dir, file)
        dest_path = os.path.join(dest_dir, file)

        # Copy only files (ignore subdirectories)
        if os.path.isfile(src_path):
            shutil.copy(src_path, dest_path)
            print(f"Copied: {src_path} -> {dest_path}")
            count += 1

    print(f"\nTotal files copied: {count}")

def is_directory(dir_name):
    if not os.path.isdir(dir_name):
        print("Source directory does not exist")
        return False
    else:
        return True

def main():
    if len(sys.argv) != 3:
        print("Invalid Input")
        print("Usage: python script.py source_directory destination_directory")
        sys.exit(1)
    
    src_dir = sys.argv[1]
    dest_dir = sys.argv[2]

    ret = is_directory(src_dir)
    if ret:
        directory_copy(src_dir, dest_dir)

if __name__ == "__main__":
    main()