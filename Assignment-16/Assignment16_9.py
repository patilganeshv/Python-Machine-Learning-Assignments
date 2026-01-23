# Write a program which display first 10 even numbers in screen.
def first_10_even_no():
    count = 0
    even = 2

    while count < 10:
        print(even, end=" ")
        even += 2
        count += 1


def main():
    first_10_even_no()

if __name__ == "__main__":
    main()