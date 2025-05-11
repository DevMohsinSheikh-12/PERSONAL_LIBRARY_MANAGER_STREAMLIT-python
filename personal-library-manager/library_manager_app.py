# library_manager.py

import os
import json

# Load library from file if exists
def load_library(filename="library.txt"):
    if os.path.exists(filename):
        with open(filename, "r") as f:
            return json.load(f)
    return []

# Save library to file
def save_library(library, filename="library.txt"):
    with open(filename, "w") as f:
        json.dump(library, f)

# Add a book
def add_book(library):
    title = input("Enter the book title: ").strip()
    author = input("Enter the author: ").strip()
    year = int(input("Enter the publication year: "))
    genre = input("Enter the genre: ").strip()
    read_input = input("Have you read this book? (yes/no): ").strip().lower()
    read = True if read_input == "yes" else False

    book = {
        "title": title,
        "author": author,
        "year": year,
        "genre": genre,
        "read": read
    }
    library.append(book)
    print("📚 Book added successfully!\n")

# Remove a book
def remove_book(library):
    title = input("Enter the title of the book to remove: ").strip()
    for book in library:
        if book["title"].lower() == title.lower():
            library.remove(book)
            print("🗑️ Book removed successfully!\n")
            return
    print("⚠️ Book not found.\n")

# Search for a book
def search_book(library):
    print("Search by:\n1. Title\n2. Author")
    choice = input("Enter your choice (1/2): ").strip()

    if choice == "1":
        keyword = input("Enter the title: ").strip().lower()
        results = [book for book in library if keyword in book["title"].lower()]
    elif choice == "2":
        keyword = input("Enter the author: ").strip().lower()
        results = [book for book in library if keyword in book["author"].lower()]
    else:
        print("⚠️ Invalid choice.\n")
        return

    if results:
        print("\nMatching Books:")
        for idx, book in enumerate(results, start=1):
            read_status = "Read" if book["read"] else "Unread"
            print(f"{idx}. {book['title']} by {book['author']} ({book['year']}) - {book['genre']} - {read_status}")
    else:
        print("🔍 No matching books found.")
    print()

# Display all books
def display_books(library):
    if not library:
        print("📂 Your library is empty!\n")
        return

    print("\nYour Library:")
    for idx, book in enumerate(library, start=1):
        read_status = "Read" if book["read"] else "Unread"
        print(f"{idx}. {book['title']} by {book['author']} ({book['year']}) - {book['genre']} - {read_status}")
    print()

# Display statistics
def display_statistics(library):
    total_books = len(library)
    if total_books == 0:
        print("📂 No books in your library.\n")
        return

    read_books = len([book for book in library if book["read"]])
    percentage_read = (read_books / total_books) * 100

    print(f"\n📊 Total books: {total_books}")
    print(f"📖 Percentage read: {percentage_read:.1f}%\n")

# Main menu
def main():
    library = load_library()

    while True:
        print("\nWelcome to your Personal Library Manager!")
        print("1. Add a book")
        print("2. Remove a book")
        print("3. Search for a book")
        print("4. Display all books")
        print("5. Display statistics")
        print("6. Exit")
        choice = input("Enter your choice: ").strip()

        if choice == "1":
            add_book(library)
        elif choice == "2":
            remove_book(library)
        elif choice == "3":
            search_book(library)
        elif choice == "4":
            display_books(library)
        elif choice == "5":
            display_statistics(library)
        elif choice == "6":
            save_library(library)
            print("\n💾 Library saved to file. Goodbye! 👋")
            break
        else:
            print("⚠️ Invalid choice. Please try again.\n")

if __name__ == "__main__":
    main()
