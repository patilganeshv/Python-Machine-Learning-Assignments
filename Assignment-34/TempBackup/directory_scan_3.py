import os

def directory_scanner(directory_name = "Marvellous"):
    ret = os.path.exists(directory_name)

    if not ret:
        print("There is no such directory")
        return
    
    print("Contents of the directory are:")
    for folder_name, sub_folder_name, file_name in os.walk(directory_name):
        print("Folder Name:", folder_name)
        
        for sub_f in sub_folder_name: 
            print("Sub Folder Name:", sub_f)
        
        for f_name in file_name:
            print("File Name:", f_name)

def main():
    directory_name = input("Enter the name of directory: ")
    directory_scanner(directory_name)

if __name__ == "__main__":
    main()