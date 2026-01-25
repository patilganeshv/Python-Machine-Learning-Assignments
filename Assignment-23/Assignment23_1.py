class BookStore:
    no_of_book = 0

    def __init__(self, name, author):
        BookStore.no_of_book = BookStore.no_of_book + 1
        self.name = name
        self.author = author

    def display(self):
        print(f"{self.name} by {self.author}. No of Books: {BookStore.no_of_book}")
    

obj1 = BookStore("Linux System Programming", "Robert Love")
obj1.display()

obj2 = BookStore("C Programming", "Dennis Ritchie")
obj2.display()