library=["Game of thrones","spyderman","harrypotter","Avengers"]
def add_book():
    book=input("Enter the book name - ")
    library.append(book)
    print("Book is added successfully")

def remove_book():
    book=input("Enter the book name to remove - ")
    if book in library:
        library.remove(book)
        print("Book removed successfully")
1
def search_book():
    book=input("Enter the book name to search - ")
    if book in library:
        print("Book is available")
    else:
        print("Book isnt Available")

def show_books():
    if len(library)==0:
        print("There ar no books")
    else:
        print("-- ALL BOOKS --")
        for b in library:
            print(b)

def menu():
    while True:
        print("====== LIBRARY MENU ======")
        print("1. Add Book")
        print("2. Remove Book")
        print("3. Search Book")
        print("4. Show All Books")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_book()
        elif choice == "2":
            remove_book()
        elif choice == "3":
            search_book()
        elif choice == "4":
            show_books()
        elif choice == "5":
            print("Thank you for visiting!...")
            break
        else:
            print("Invalid choice! Try again.\n")

menu()
    
    


