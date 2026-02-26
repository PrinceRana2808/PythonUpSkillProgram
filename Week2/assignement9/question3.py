#Create a class Book with a class method from_string() that creates a Book instance from a string.
# And print both attributes of the class

class Book:
    
    def __init__(self, title, author):
        self.title = title
        self.author = author

    # Class method to create object from string
    @classmethod
    def from_string(cls, book_str):
        title, author = book_str.split(",")
        return cls(title.strip(), author.strip())


book1 = Book.from_string("Atomic Habits, James Clear")
print("Title:", book1.title)
print("Author:", book1.author)