# Write a program which accepts marks and display grade
def display_grade(mark):
    if mark >= 75:
        return "Distinction"
    elif mark >= 60:
        return "First Class"
    elif mark >= 50:
        return "Second Class"
    elif mark < 50:
        return "Fail"

def main():
    mark = int(input("Enter the mark: "))
    grade = display_grade(mark)
    print(grade)

if __name__ == "__main__":
    main()