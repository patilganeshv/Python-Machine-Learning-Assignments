"""
Design automation script which accept directory name
and display checksum of all files.

Usage : DirectoryChecksum.py Demo
Demo is name of directory
"""
import os
import sys
import module
import time

def directory_watcher(dir_name, fobj):
    found = False
    for folder_name, _, file_name in os.walk(dir_name):
        for f_name in file_name: 
            f_name = os.path.join(folder_name, f_name)
            checksum = module.calculate_checksum(f_name)
            fobj.write(f"File Name: {f_name} --> Checksum: {checksum} \n")
            found = True
    
    if not found:
        fobj.write("No files found")

def main():
    border = "-" * 50
    time_stamp = time.ctime()

    if len(sys.argv) != 2:
        print("Invalid Input")
        print("Usage: python script.py directoryname")
        sys.exit(1)
    
    dir_name = sys.argv[1]
    
    fobj = open("Log.txt", "w")
    fobj.write(border+"\n")
    fobj.write("---------- Directory Checksum Script -------------\n")
    fobj.write(border+"\n")

    exists = module.is_exists(dir_name)
    if not exists:
        fobj.write(f"Directory '{dir_name}' does not exist")
        return
    
    directory = module.is_directory(dir_name) 
    if not directory:
        fobj.write(f"'{dir_name}' is not a directory")
        return
    
    directory_watcher(dir_name, fobj)
    fobj.write(border+"\n")
    fobj.write("This log file is created at: "+time_stamp+"\n")
    fobj.write(border+"\n")

if __name__ == "__main__":
    main()