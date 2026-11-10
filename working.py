from data import books

def Display_all_books(books):
    for item in books:
        print(item["name"])

def Search_book_by_name(books,user_chooce):
    for item in books:
        if item["name"][:len(user_chooce)].lower() == user_chooce.lower():
            print(item)
    

def add_book(books, name, author, year):
    new_book = {"id": get_next_book_id(books),"name": name, "author":author ,"year":year, "available": True}
    books.append(new_book)
    print("The addition was successful")

def Borrow_a_book(books,id_book):
    for item in books:
        if id_book == item["id"]:
            if item["available"] == True:
                item["available"] = False
                print("The loan was successful")
                return True
    print("not found")
    return False
def Return_a_book(books, book_id):
    for item in books:
        if book_id == item["id"]:
            if item["available"] == False:
                item["available"] = True
                print(" successful")
                
    return False

def Display_available_books(books):
    for item in books:
        if item["available"] == True:
            print(item)

def Display_books_by_author(books, author):
    for item in books:
        if item["author"].lower() == author.lower():
            print(item)
            return True
        else:
            print("not found")
            return False

def get_next_book_id(books):
    return books[-1]["id"] +1

