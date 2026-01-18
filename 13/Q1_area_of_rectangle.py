def calculate_area_of_rectangle(length, width):
    return length * width

def main():
    length_value = float(input("Enter the length: "))
    width_value = float(input("Enter the width: "))
    ret = calculate_area_of_rectangle(length_value, width_value)
    print(ret)

if __name__ == "__main__":
    main()