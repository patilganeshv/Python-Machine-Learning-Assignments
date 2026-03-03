"""
Design automation script which accept directory name and delete all duplicate 
files from that directory. Write names of duplicate files from that directory 
into log file named as Log.txt.
Log.txt file should be created into current directory.

Usage : DirectoryDuplicateRemoval.py Demo

Demo is name of directory
"""
import os
import sys
import module
import time

duplicate = {}

def find_duplicate(dir_name, fobj):
    found = False
    for folder_name, _, file_name in os.walk(dir_name):
        for f_name in file_name: 
            f_name = os.path.join(folder_name, f_name)
            checksum = module.calculate_checksum(f_name)

            if checksum in duplicate:
                fobj.write(f"Duplicate file: {f_name} \n")
                duplicate[checksum].append(f_name)
                found = True
            else:
                duplicate[checksum] = [f_name]
    
    if not found:
        fobj.write("There is no any duplicate files \n\n")

    return duplicate


def delete_duplicate(dir_name, fobj):
    my_dict = find_duplicate(dir_name, fobj)
    
    result = list(filter(lambda x: len(x) > 1, my_dict.values()))
    count = 0
    cnt = 0 

    for value in result:
        for sub_value in value:
            count = count + 1
            if count > 1:
                # print("Deleted File: ", sub_value)
                os.remove(sub_value)
                cnt = cnt + 1
        count = 0

    fobj.write(f"Total deleted files: {cnt} \n")

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
    fobj.write("------ Find Duplicate Files From Directory -------\n")
    fobj.write(border+"\n\n")

    exists = module.is_exists(dir_name)
    if not exists:
        fobj.write(f"Directory '{dir_name}' does not exist")
        return
    
    directory = module.is_directory(dir_name) 
    if not directory:
        fobj.write(f"'{dir_name}' is not a directory")
        return
    
    delete_duplicate(dir_name, fobj)
    fobj.write(border+"\n")
    fobj.write("This log file is created at: "+time_stamp+"\n")
    fobj.write(border+"\n")

if __name__ == "__main__":
    main()