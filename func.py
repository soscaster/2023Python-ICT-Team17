import sqlite3

# Create database connection
def create_connection():
    sql_conn = sqlite3.connect("bookstore.db")
    cur = sql_conn.cursor()
    # Drop tables if they exist
    cur.execute("DROP TABLE IF EXISTS store")
    cur.execute("DROP TABLE IF EXISTS staff")
    cur.execute("DROP TABLE IF EXISTS customer")
    cur.execute("CREATE TABLE IF NOT EXISTS store (store_id INTEGER PRIMARY KEY, store_name TEXT, store_address TEXT, store_phone TEXT, store_email TEXT)")
    cur.execute("CREATE TABLE IF NOT EXISTS staff (st_ID INTEGER PRIMARY KEY, st_name TEXT, st_dob TEXT, st_address TEXT, st_phone TEXT, st_email TEXT)")
    cur.execute("CREATE TABLE IF NOT EXISTS customer (cus_ID INTEGER PRIMARY KEY, cus_name TEXT, cus_dob TEXT, cus_address TEXT, cus_phone TEXT, cus_email TEXT)")
    sql_conn.commit()
    sql_conn.close()

# Modify store information
def modify_store(store_id, store_name, store_address, store_phone, store_email):
    sql_conn = sqlite3.connect("bookstore.db")
    cur = sql_conn.cursor()
    cur.execute("UPDATE store SET store_name = ?, store_address = ?, store_phone = ?, store_email = ? WHERE store_id = ?", (store_name, store_address, store_phone, store_email, store_id))
    sql_conn.commit()
    sql_conn.close()

# Add new staff
def add_staff(st_ID, st_name, st_dob, st_address, st_phone, st_email):
    sql_conn = sqlite3.connect("bookstore.db")
    cur = sql_conn.cursor()
    cur.execute("INSERT INTO staff VALUES (?, ?, ?, ?, ?, ?)", (st_ID, st_name, st_dob, st_address, st_phone, st_email))
    sql_conn.commit()

    # Verify if staff is saved or not
    cur.execute("SELECT * FROM staff WHERE st_ID = ?", (st_ID,))
    staff = cur.fetchall()
    if staff:
        print("Staff added successfully!")
    else:
        print("Staff not added!")
    sql_conn.close()

# Get staff list from database
def get_staff_list():
    sql_conn = sqlite3.connect("bookstore.db")
    cur = sql_conn.cursor()
    cur.execute("SELECT * FROM staff")
    staff_list = cur.fetchall()
    sql_conn.close()
    return staff_list

# Modify staff information
def modify_staff(st_ID, st_name, st_dob, st_address, st_phone, st_email):
    sql_conn = sqlite3.connect("bookstore.db")
    cur = sql_conn.cursor()
    cur.execute("UPDATE staff SET st_name = ?, st_dob = ?, st_address = ?, st_phone = ?, st_email = ? WHERE st_ID = ?", (st_name, st_dob, st_address, st_phone, st_email, st_ID))
    sql_conn.commit()

    # Verify if staff is saved or not
    cur.execute("SELECT * FROM staff WHERE st_ID = ?", (st_ID,))
    staff = cur.fetchall()
    if staff:
        print("Staff modified successfully!")
    else:
        print("Staff not modified!")
    sql_conn.close()

# Delete staff
def delete_staff(st_ID):
    sql_conn = sqlite3.connect("bookstore.db")
    cur = sql_conn.cursor()
    cur.execute("DELETE FROM staff WHERE st_ID = ?", (st_ID,))
    sql_conn.commit()
    sql_conn.close()

# Add new customer
def add_customer(cus_ID, cus_name, cus_dob, cus_address, cus_phone, cus_email):
    sql_conn = sqlite3.connect("bookstore.db")
    cur = sql_conn.cursor()
    cur.execute("INSERT INTO customer VALUES (?, ?, ?, ?, ?, ?)", (cus_ID, cus_name, cus_dob, cus_address, cus_phone, cus_email))
    sql_conn.commit()
    sql_conn.close()

# Modify customer information
def modify_customer(cus_ID, cus_name, cus_dob, cus_address, cus_phone, cus_email):
    sql_conn = sqlite3.connect("bookstore.db")
    cur = sql_conn.cursor()
    cur.execute("UPDATE customer SET cus_name = ?, cus_dob = ?, cus_address = ?, cus_phone = ?, cus_email = ? WHERE cus_ID = ?", (cus_name, cus_dob, cus_address, cus_phone, cus_email, cus_ID))
    sql_conn.commit()
    sql_conn.close()

# Delete customer
def delete_customer(cus_ID):
    sql_conn = sqlite3.connect("bookstore.db")
    cur = sql_conn.cursor()
    cur.execute("DELETE FROM customer WHERE cus_ID = ?", (cus_ID,))
    sql_conn.commit()
    sql_conn.close()

# Path: main.py
