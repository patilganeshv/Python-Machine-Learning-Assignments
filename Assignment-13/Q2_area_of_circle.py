# Write a program which accepts radium of circle and prints area of circle.
PI = 3.142

def calculate_area_of_circle(r):
    return PI * r * r

def main():
    radius = float(input("Enter the radius of circle: "))
    area_of_circle = calculate_area_of_circle(radius)
    print("Area of Circle is: ", area_of_circle)

if __name__ == "__main__":
    main()