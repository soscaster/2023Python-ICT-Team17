import sqlite3
import dbfunc

def check_book_table():
    sql_conn = sqlite3.connect("bookstore.db")
    cur = sql_conn.cursor()
    cur.execute("SELECT * FROM book")
    book = cur.fetchall()
    if book:
        sql_conn.close()
        return True
    else:
        sql_conn.close()
        return False

# Check if book exists
def check_book(ID, title):
    sql_conn = sqlite3.connect("bookstore.db")
    cur = sql_conn.cursor()
    cur.execute("SELECT * FROM book WHERE book_ID = ? OR book_title = ?", (ID, title))
    book = cur.fetchall()
    if book:
        print("Book already exists!")
        sql_conn.close()
        return True
    else:
        print("This book is new.")
        sql_conn.close()
        return False
    

def add_book(id, title, genre, author, target, publisher, price, quantity):
    sql_conn = sqlite3.connect("bookstore.db")
    cur = sql_conn.cursor()
    cur.execute("INSERT INTO book VALUES (?, ?, ?, ?, ?, ?, ?, ?)", (id, title, genre, author, target, publisher, price, quantity))
    sql_conn.commit()
    cur.execute("SELECT * FROM book WHERE book_ID = ?", (id,))
    customer = cur.fetchall()
    if customer:
        print("Book added!")
        sql_conn.close()
        return True
    else:
        print("Book not added!")
        sql_conn.close()
        return False
    
    
def mod_book(title, genre, author, target, publisher, price, quantity):
    sql_conn = sqlite3.connect("bookstore.db")
    cur = sql_conn.cursor()
    cur.execute("UPDATE book SET book_title = ?, book_genre = ?, book_author = ?, book_target = ?, book_publisher = ?, book_price = ?, book_quantity = ?", (title, genre, author, target, publisher, price, quantity))
    sql_conn.commit()
    sql_conn.close()
    
    
def get_book_list():
    sql_conn = sqlite3.connect("bookstore.db")
    cur = sql_conn.cursor()
    cur.execute("SELECT * FROM book")
    book_list = cur.fetchall()
    sql_conn.close()
    return book_list

def get_book_info(id):
    sql_conn = sqlite3.connect("bookstore.db")
    cur = sql_conn.cursor()
    cur.execute("SELECT * FROM book WHERE book_id = ?", (id,))
    book = cur.fetchall()
    sql_conn.close()
    return book[0]
        