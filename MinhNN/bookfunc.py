import sqlite3
from sqlite3 import Error

    
# Add book - Modify book - Delete book - View book - Search book by ID, name, author, year - View all sales report - View sales report by date - View sales report by book - View sales report by staff - View sales report by category
# Book detail: book_ID, book_title, book_genre, book_author, book_year, book_rated, 

# Call .commit() every modification to the database
# Call .close() every time finish modifying the data

# def check_db():
#     if os.path.exists('bookstore.db'):
#         with open("bookstore.db", 'x')

def create_book_db():
    sql_conn = sqlite3.connect("bookstore.db")
    cur = sql_conn.cursor()
    cur.execute("DROP TABLE IF NOT EXISTS book")
    cur.execute("CREATE TABKE IF NOT EXISTS books (book_ID TEXT PRIMARY KEY, book_title TEXT, book_genre TEXT, book_author TEXT, book_year TEXT, book_price TEXT, book_quantity VARCHAR(10))") 
    # 7 (book_ID, book_title, book_gerne, book_author, book_year, book_price, book_quantity(varchar(10))

    sql_conn.commit()
    sql_conn.close()

def add_book(book_ID, book_title, book_gerne, book_author, book_year, book_price, book_quantity):
    # book_ID should be set, and increase when new book is added, starting from 1 (optional)
    sql_conn = sqlite3.connect("bookstore.db")
    cur = sql_conn.cursor()

    cur.execute("INSERT INTO books VALUES(?, ?, ?, ?, ?, ? ,?)",(book_ID, book_title, book_gerne, book_author, book_year, book_price, book_quantity))
    sql_conn.commit()
    book = cur.fetchall()
    cur.execute("SELECT * FROM book WHERE book_ID = ?",(book_ID,))
    if book:
        print("Book added successfully!")
        sql_conn.close()
        return True
    else:
        print("Book not added!")
        sql_conn.close()
        return True
    
# def add_book():
#     sql_conn = sqlite3.connect("bookstore.db")
#     cur = sql_conn.cursor()
#     cur.execute("")
def modify_book(book_ID, book_title, book_gerne, book_author, book_year, book_price, book_quantity):
    sql_conn = sqlite3.connect("bookstore.db")
    cur = sql_conn.cursor()
    cur.execute("UPDATE book SET book_ID = ?, book_title = ?, book_gerne = ?, book_author = ?, book_year = ?, book_price = ?, book_quantity = ?",(book_ID, book_title, book_gerne, book_author, book_year, book_price, book_quantity))
    sql_conn.commit()

    cur.execute("SELECT * FROM book WHERE book_ID = ?")
    book = cur.fetchall()
    cur.execute("SELECT * FROM book WHERE book_ID = ?",(book_ID,))
    if book:
        print("Book moddified successfully!")
        sql_conn.close()
        return True
    else:
        print("Book not modified!")
        sql_conn.close()
        return True

    
def delete_book(book_ID):
    sql_conn = sqlite3.connect("bookstore.db")
    cur = sql_conn.cursor()
    cur.execute("DELETE FROM book WHERE book_ID = ?",(book_ID,))
    sql_conn.commit()
    sql_conn.close()

def view_book():
    sql_conn = sqlite3.connect("bookstore.db")
    cur = sql_conn.cursor()
    cur.execute("SELECT * FROM book")
    sql_conn.commit()
    sql_conn.close()
    
def search_book_by_ID(book_ID):
    sql_conn = sqlite3.connect("bookstore.db")
    cur = sql_conn.cursor()
    cur.execute("SELECT * FROM book WHERE book_ID = ?",(book_ID,))
    sql_conn.commit()
    sql_conn.close()

def search_book_by_title(book_title):
    sql_conn = sqlite3.connect("bookstore.db")
    cur = sql_conn.cursor()
    cur.execute("SELECT * FROM book WHERE book_title = ?",(book_title))
    sql_conn.commit()
    sql_conn.close()

def search_book_by_author(book_author):
    sql_conn = sqlite3.connect("bookstore.db")
    cur = sql_conn.cursor()
    cur.execute("SELECT * FROM book WHERE book_author = ?",(book_author,))
    sql_conn.commit()
    sql_conn.close()
    
def search_book_by_year(book_year): 
    sql_conn = sqlite3.connect("bookstore.db")
    cur = sql_conn.cursor()
    cur.execute("SELECT * FROM book WHERE book_year = ?",(book_year))
    sql_conn.commit()
    sql_conn.close()

#Check book table
