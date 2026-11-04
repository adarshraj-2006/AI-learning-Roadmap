class Book:
    def __init__(self, title, author, price, availability=True):
        self.title = title
        self.author = author
        self.price = price
        self.availability = availability

    def borrow_book(self):
        if self.availability:
            self.availability = False
            print(f"{self.title}borrowed.")
        else:
            print(f"{self.title}not available.")

    def return_book(self):
        self.availability = True
        print(f"{self.title} has been returned.")

    def display(self):
        print(f"Title       : {self.title}")
        print(f"Author      : {self.author}")
        print(f"Price       : {self.price}")
        print(f"Available   : {self.availability}")

books = [
    Book("Python Basics", "Rishav Raj", 500, True),
    Book("Data Structures", "Adarsh Raj", 700, False),
    Book("Machine Learning", "Sahil Raj", 1200, True),
    Book("AI Fundamentals", "Surya Pratap", 900, True),
    Book("Web Development", "Aditya Raj", 800, False)
]

books[0].borrow_book()
books[1].return_book()
for book in books:
    book.display()
available_books = [book for book in books if book.availability]

for book in available_books:
    print(book.title, "-", book.price)

avg_price = sum(book.price for book in available_books) / len(available_books)
print(avg_price)