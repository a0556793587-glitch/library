def print_menu():
    print("""================================
       LIBRARY MANAGEMENT
================================

1. Display all books
2. Search book by name
3. Add new book
4. Borrow a book
5. Return a book
6. Display available books
7. Display books by author
0. Exit

Choose an option:""")

def get_input():
    choose_number = None
    while True:
        try:
            choose_number = int(input("enter your anser!"))
            if choose_number >= 0 and choose_number < 8:
                return choose_number
            else: 
                print("Incorrect option Try again")
        except ValueError:
            print("You must choose only from the possible options, so you will choose between 0 and 10.")
    

    