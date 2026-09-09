# Magic methods = Dunder methods (double underscore) __init__, __str__, __eq__
#                 They are automatically called by many of Python's built-in operations.
#                 They allow developers to define or customize the behavior of objects

class Book:

    def __init__(self, title, author, num_pages):
        self.title = title
        self.author = author
        self.num_pages = num_pages

    def __str__(self):
        return f"'{self.title}' by {self.author}"

    def __eq__(self, other):
        return self.title == other.title and self.author == other.author

    def __lt__(self, other):
        return self.num_pages < other.num_pages

    def __gt__(self, other):
        return self.num_pages > other.num_pages

    def __add__(self,other):
        return f"{self.num_pages + other.num_pages} pages"

    def __contains__(self, keyword):
        return keyword in self.title or keyword in self.author

    def __getitem__(self, key):
        if key == "title":
            return self.title
        if key == "author":
            return self.author
        else:
            return f"key '{key}' was not found"

book1 = Book("ASTROPHYSICS for PEOPLE in a HURRY", "Neil DeGrasse Tyson", 211)
book2 = Book("In Search of Schrödinger's Cat", "John Gribbin", 252)
book3 = Book("Chess Book for Beginners", "A.Gopalaratnam", 385)
book4 = Book("In Search of Schrödinger's Cat", "John Gribbin", 272)

print(book1)  # __str__
print(book2 == book4)  # __eq__
print(book2 > book4)  # __lt__
print(book2 < book4)  # __gt__
print(book2 + book4)  # __add__
print("Cat" in book2)  # __contains__
print(book1['title'])  # __getitem__
print(book1['author'])  # __getitem__
print(book1['audio'])  # __getitem__