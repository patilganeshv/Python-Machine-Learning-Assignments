# Write a program which accept name from user and display length of its name.
def len_of_name(name):
    return len(name)

def main():
    name = input("Enter the Name: ")
    ret = len_of_name(name)
    print(f"Length of {name} is: {ret}")

if __name__ == "__main__":
    main()