class Library:
    def __init__(self):
        self.books = {}

    def add_book(self, book_id, book_name, author):
        self.books[book_id] = {
            "name": book_name,
            "author": author,
            "issued": False
        }
        print("Book added successfully!\n")

    def view_books(self):
        if not self.books:
            print("No books available in the library.\n")
            return

        print("\nAvailable Books:")
        print("ID | Book Name | Author | Status")
        for book_id, details in self.books.items():
            status = "Issued" if details["issued"] else "Available"
            print(f"{book_id} | {details['name']} | {details['author']} | {status}")
        print()

    def issue_book(self, book_id):
        if book_id in self.books:
            if not self.books[book_id]["issued"]:
                self.books[book_id]["issued"] = True
                print("Book issued successfully!\n")
            else:
                print("Book already issued.\n")
        else:
            print("Book ID not found.\n")

    def return_book(self, book_id):
        if book_id in self.books:
            if self.books[book_id]["issued"]:
                self.books[book_id]["issued"] = False
                print("Book returned successfully!\n")
            else:
                print("Book was not issued.\n")
        else:
            print("Book ID not found.\n")


# Main Program
library = Library()

while True:
    print("===== Library Management System =====")
    print("1. Add Book")
    print("2. View Books")
    print("3. Issue Book")
    print("4. Return Book")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        book_id = input("Enter Book ID: ")
        book_name = input("Enter Book Name: ")
        author = input("Enter Author Name: ")
        library.add_book(book_id, book_name, author)

    elif choice == "2":
        library.view_books()

    elif choice == "3":
        book_id = input("Enter Book ID to issue: ")
        library.issue_book(book_id)

    elif choice == "4":
        book_id = input("Enter Book ID to return: ")
        library.return_book(book_id)

    elif choice == "5":
        print("Thank you for using Library Management System.")
        break

    else:
        print("Invalid choice. Please try again.\n")
