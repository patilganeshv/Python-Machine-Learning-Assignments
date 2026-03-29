import os

def main():
    directory_name = input("Enter the name of directory: ")
    print("Contents of the directory are:")

    for folder_name, sub_folder_name, file_name in os.walk(directory_name):
        print("Folder Name:", folder_name)
        
        for sub_f in sub_folder_name: 
            print("Sub Folder Name:", sub_f)
        
        for f_name in file_name:
            print("File Name:", f_name)
            
if __name__ == "__main__":
    main()