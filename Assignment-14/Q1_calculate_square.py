# Write a lambda function which accepts one number and returns squre of that number.
calculate_square = lambda no: no * no

def main():
    val = int(input("Enter the Number to calculate the square: "))
    ret = calculate_square(val)
    print("Square of", val, "is", ret)

if __name__ == "__main__":
    main()