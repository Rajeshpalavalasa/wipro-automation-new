library = { 
"101": ("Atomic Habits", "James Clear"), 
"102": ("The Power of Now", "Eckhart Tolle"), 
"103": ("Think and Grow Rich", "Napoleon Hill"), 
"104": ("How to Win Friends and Influence People", "Dale Carnegie"), 
"105": ("The 7 Habits of Highly E ective People", "Stephen R. Covey"), 
"106": ("You Are a Badass", "Jen Sincero"), 
"107": ("Rich Dad Poor Dad", "Robert T. Kiyosaki"), 
"108": ("The Subtle Art of Not Giving a F*ck", "Mark Manson"), 
"109": ("Deep Work", "Cal Newport"), 
"110": ("Mindset", "Carol S. Dweck") 
} 
def add_book(): 
    print("\nAdd New Book") 
    book_id = input("Book ID: ") 
    book_name = input("Book Name: ") 
    author_name = input("Author Name: ") 
    library[book_id] = (book_name, author_name) 
    print("Book added successfully") 
def remove_book(): 
    print("\nRemove Book") 
    book_id = input("Enter Book ID to remove: ") 
    if book_id in library: 
        del library[book_id] 
        print("Book removed successfully ") 
    else: 
        print("Book not found") 
def search_book(): 
    print("\nSearch Book") 
    book_id = input("Enter Book ID to search: ") 
    if book_id in library: 
        book_name, author_name = library[book_id] 
        print("Book Found ") 
        print("Book Name:", book_name) 
        print("Author:", author_name) 
    else: 
        print("Book not found ") 
def show_books(): 
    print("\nAll Books in Library") 
    if not library: 
        print("Library is empty ") 
    else: 
        for book_id, details in library.items(): 
            book_name, author_name = details 
            print("ID:", book_id, "| Name:", book_name, "| Author:", author_name) 
def update_book(): 
    print("\nUpdate Book Details") 
    book_id = input("Enter Book ID to update: ") 
    if book_id in library: 
        book_name = input("Enter new Book Name: ") 
        author_name = input("Enter new Author Name: ") 
        library[book_id] = (book_name, author_name) 
        print("Book details updated successfully") 
    else: 
        print("Book not found") 
while True: 
    print("\n--- Library Menu ---") 
    print("1. Add new book") 
    print("2. Remove book") 
    print("3. Search for a book") 
    print("4. Show all books") 
    print("5. Update book details") 
    print("6. Exit") 
    choice = input("Choose an option (1-6): ") 
    if choice == "1": 
        add_book() 
    elif choice == "2": 
        remove_book() 
    elif choice == "3": 
        search_book() 
    elif choice == "4": 
        show_books() 
    elif choice == "5": 
        update_book() 
    elif choice == "6": 
        print("Thank you for using the Library System ") 
        break 
    else: 
        print("Invalid choice  Please try again.")