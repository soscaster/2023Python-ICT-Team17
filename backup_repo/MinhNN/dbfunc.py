import sqlite3

# Create database connection [DONE]
def create_connection():
    sql_conn = sqlite3.connect("bookstore.db")
    cur = sql_conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS book (book_id TEXT PRIMARY KEY, book_title TEXT, book_genre TEXT, book_author TEXT, book_target TEXT, book_publisher TEXT, book_price INTEGER, book_quantity INTEGER)")
    cur.execute("CREATE TABLE IF NOT EXISTS store (store_id TEXT PRIMARY KEY, store_name TEXT, store_address TEXT, store_phone TEXT, store_email TEXT)")
    cur.execute("CREATE TABLE IF NOT EXISTS staff (st_ID TEXT PRIMARY KEY, st_pwd TEXT, st_name TEXT, st_dob TEXT, st_address TEXT, st_phone TEXT, st_email TEXT)")
    cur.execute("CREATE TABLE IF NOT EXISTS customer (cu_ID TEXT PRIMARY KEY, cu_name TEXT, cu_dob TEXT, cu_address TEXT, cu_phone TEXT, cu_email TEXT)")
    sql_conn.commit()
    sql_conn.close()


# Path: main.py
