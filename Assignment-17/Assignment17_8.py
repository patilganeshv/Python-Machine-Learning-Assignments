# Write a program which accept one number and display below pattern.
# input: 5

def print_pattern(no):
    for i in range(1, no+1):
        for j in range(1, i+1):
            print(j, end=" ")
        print()
        
def main():
    no = int(input("Enter the Number: "))
    print_pattern(no)

if __name__ == "__main__":
    main()