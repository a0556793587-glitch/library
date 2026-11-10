from menu import get_input,print_menu
from data import books
from working import *

def main():
    user_chooce = None
    while user_chooce != 0:
        print_menu()
        user_chooce = get_input()
        if user_chooce == 1:
            Display_all_books(books)
        elif user_chooce == 2:
            user_chooce = input("what the nane of the book?")
            Search_book_by_name(books,user_chooce)
        elif user_chooce == 3:
            name = input("whet the name?")
            author = input("whet the author?")
            year = input("whet the year?")
            add_book(books, name, author, year)
        elif user_chooce == 4:
            id_book = None
            try:
                id_book = int(input("enter id of the book!"))
                Borrow_a_book(books,id_book)
            except ValueError:
                print(" id must be number !!!!!!!")    
        elif user_chooce == 5:
            id_book = None
            try:
                id_book = int(input("enter id of the book!"))
                Return_a_book(books, book_id)
            except ValueError:
                print(" id must be number !!!!!!!")  
        elif user_chooce == 6:
            Display_available_books(books)
        elif user_chooce == 7:
            author = input("what the name of the author")
            Display_books_by_author(books, author)


if __name__ == "__main__":
    main()
