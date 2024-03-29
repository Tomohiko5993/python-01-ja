class Book:
    def __init__(self, title, status):
        self.title = title
        self.status = status  # "read" or "unread"

class BookShelf:
    def __init__(self):
        self.books = []

    def add_book(self, title, status):
        if not title:
            print("Title cannot be empty.")
            return
        book = Book(title, status)
        self.books.append(book)
        print("Book added successfully.")

    def edit_book(self, old_title, new_title, new_status):
        if not old_title or not new_title:
            print("Title cannot be empty.")
            return False
        for book in self.books:
            if book.title == old_title:
                book.title = new_title
                book.status = new_status
                print("Book edited successfully.")
                return True
        print("Book not found.")
        return False

    def search_book(self, title):
        if not title:
            print("Title cannot be empty.")
            return None
        for book in self.books:
            if book.title == title:
                return book
        print("Book not found.")
        return None

    def delete_book(self, title):
        if not title:
            print("Title cannot be empty.")
            return False
        for book in self.books:
            if book.title == title:
                self.books.remove(book)
                print("Book deleted successfully.")
                return True
        print("Book not found.")
        return False

    def display_statistics(self):
        total_books = len(self.books)
        read_books = sum(1 for book in self.books if book.status == "read")
        unread_books = total_books - read_books
        print("Total books:", total_books)
        print("Read books:", read_books)
        print("Unread books:", unread_books)

def display_menu():
    print("\nBookshelf Menu:")
    print("1. Add Book")
    print("2. Edit Book")
    print("3. Search Book")
    print("4. Delete Book")
    print("5. Display Statistics")
    print("6. Exit")

# ブックシェルフのインスタンスを作成
bookshelf = BookShelf()

while True:
    display_menu()
    choice = input("Please select from 1 to 6: ")

    if choice == "1":
        title = input("Enter book title: ")
        status = input("Enter book status (read/unread): ").lower()
        if status not in ["read", "unread"]:
            print("Invalid status. Please enter 'read' or 'unread'.")
            continue
        bookshelf.add_book(title, status)

    elif choice == "2":
        old_title = input("Enter the title of the book to edit: ")
        new_title = input("Enter new title: ")
        new_status = input("Enter new status (read/unread): ").lower()
        if new_status not in ["read", "unread"]:
            print("Invalid status. Please enter 'read' or 'unread'.")
            continue
        bookshelf.edit_book(old_title, new_title, new_status)

    elif choice == "3":
        title = input("Enter book title to search: ")
        book = bookshelf.search_book(title)
        if book:
            print("Found:", book.title)

    elif choice == "4":
        title = input("Enter book title to delete: ")
        bookshelf.delete_book(title)

    elif choice == "5":
        bookshelf.display_statistics()

    elif choice == "6":
        print("Exiting...")
        break

    else:
        print("Invalid choice. Please enter a number between 1 and 6.")