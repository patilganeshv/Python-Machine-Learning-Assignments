# Write a lambda funtion using filter() which accepts a list of strings and returns a list of strings having length greater than 5
str_len_gt_five = lambda string: (len(string) > 5)

def main():
    data = ["jay", "patil", "ram", "ganesh", "pune", "maharashtra"]
    print("Actual data is:", data)

    filter_data = list(filter(str_len_gt_five, data))
    print("List of strings having length greater then 5:", filter_data)

if __name__ == "__main__":
    main()