"""
Display File Contents
Write a program which accepts a file name from the user, open that file,
and display the entire contents on the console.

Input: demo.txt
Output: Display contents of demo.txt on console.
"""

def display_file_content(file_name):
    try:
        fobj = open(file_name, "r")
        print("File gets successfully opened")

        data = fobj.read()
        print("Data from file is: ", data)
        
        fobj.close()

    except FileNotFoundError:
        print("Unable to open file as there no such file")

def main():
    file_name = input("Enter the File Name: ")
    display_file_content(file_name)

if __name__ == "__main__":
    main()