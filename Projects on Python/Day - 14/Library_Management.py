# Write a Library class with no_of_books and books as two instance variables. Write a program to create a library from this Library class and show how you can print all books, add a book and get the number of books using different methods. Show that your program doesnt persist the books after the program is stopped!

class Library:
    def __init__(self, books):
        self.books = books

    def print_books(self):
        print(self.books)

    def add_book(self, book):
        self.books.append(book)

    def get_no_of_books(self):
        return len(self.books)

    def get_books(self):
        return self.books

library = Library([])
print("1. Print all books\n2. Add a book\n3. Get number of books\n4. Get all books\n5. Exit")
while True:
    try:
        choice = int(input("Enter your choice: "))
    except ValueError:
        print("You must enter a number between 1 and 5")
        continue
    if choice < 1 or choice > 5:
        print("You must enter a number between 1 and 5")
        continue
    if choice == 1:
        if len(library.books) == 0:
            print("No books available")
        else:
            print("Available books are: ", end="")
            library.print_books()
    elif choice == 2:
        book = input("Enter the book name: ")
        library.add_book(book)
    elif choice == 3:
        print(library.get_no_of_books())
    elif choice == 4:
        print(library.get_books())
    elif choice == 5:
        break