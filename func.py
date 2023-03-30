import sqlite3

# Create database connection [DONE]
def create_connection():
    sql_conn = sqlite3.connect("bookstore.db")
    cur = sql_conn.cursor()
    # Drop tables if they exist
    cur.execute("DROP TABLE IF EXISTS store")
    cur.execute("DROP TABLE IF EXISTS staff")
    cur.execute("DROP TABLE IF EXISTS customer")
    cur.execute("CREATE TABLE IF NOT EXISTS store (store_id TEXT PRIMARY KEY, store_name TEXT, store_address TEXT, store_phone TEXT, store_email TEXT)")
    cur.execute("CREATE TABLE IF NOT EXISTS staff (st_ID TEXT PRIMARY KEY, st_name TEXT, st_dob TEXT, st_address TEXT, st_phone TEXT, st_email TEXT)")
    cur.execute("CREATE TABLE IF NOT EXISTS customer (cus_ID TEXT PRIMARY KEY, cus_name TEXT, cus_dob TEXT, cus_address TEXT, cus_phone TEXT, cus_email TEXT)")
    sql_conn.commit()
    sql_conn.close()

def add_store_default():
    sql_conn = sqlite3.connect("bookstore.db")
    cur = sql_conn.cursor()
    cur.execute("INSERT INTO store VALUES ('HN-001', 'ICT Bookstore', 'A21 - 17B Hoang Quoc Viet', '1900-1508', 'ict-bookstore@quangminh.name.vn')")
    sql_conn.commit()
    sql_conn.close()

# Get store information from database [DONE]
def get_store_info():
    sql_conn = sqlite3.connect("bookstore.db")
    cur = sql_conn.cursor()
    cur.execute("SELECT * FROM store")
    store_info = cur.fetchall()
    sql_conn.close()
    return store_info[0]

# Modify store information [DONE]
def modify_store(store_id, store_name, store_address, store_phone, store_email):
    sql_conn = sqlite3.connect("bookstore.db", timeout=3)
    cur = sql_conn.cursor()
    # Drop all store information and add new one
    cur.execute("DELETE FROM store")
    cur.execute("INSERT INTO store VALUES (?, ?, ?, ?, ?)", (store_id, store_name, store_address, store_phone, store_email))
    sql_conn.commit()

    # Verify if store is saved or not
    cur.execute("SELECT * FROM store WHERE store_id = ?", (store_id,))
    store = cur.fetchall()
    if store:
        print("Store modified successfully!")
        sql_conn.close()
    else:
        print("Store not modified!")
        sql_conn.close()

# Check if staff ID exists [DONE]
def check_staff(st_ID, st_phone, st_email):
    sql_conn = sqlite3.connect("bookstore.db")
    cur = sql_conn.cursor()
    cur.execute("SELECT * FROM staff WHERE st_ID = ? OR st_phone = ? OR st_email = ?", (st_ID, st_phone, st_email))
    staff = cur.fetchall()
    # If staff exists, return True
    if staff:
        print("Staff already exists!")
        sql_conn.close()
        return True
    else:
        print("Staff does not exist yet!")
        sql_conn.close()
        return False
    

# Add new staff [DONE]
def add_staff(st_ID, st_name, st_dob, st_address, st_phone, st_email):
    sql_conn = sqlite3.connect("bookstore.db")
    cur = sql_conn.cursor()
    # Add new staff
    cur.execute("INSERT INTO staff VALUES (?, ?, ?, ?, ?, ?)", (st_ID, st_name, st_dob, st_address, st_phone, st_email))
    sql_conn.commit()
    cur.execute("SELECT * FROM staff WHERE st_ID = ?", (st_ID,))
    staff = cur.fetchall()
    if staff:
        print("Staff added successfully!")
        sql_conn.close()
        return True
    else:
        print("Staff not added!")
        sql_conn.close()
        return False
    
# Get staff list from database to create a dropdown list [DONE]
def get_staff_list():
    sql_conn = sqlite3.connect("bookstore.db")
    cur = sql_conn.cursor()
    cur.execute("SELECT * FROM staff")
    staff_info = cur.fetchall()
    sql_conn.close()
    return staff_info

def get_staff_info(st_ID):
    sql_conn = sqlite3.connect("bookstore.db")
    cur = sql_conn.cursor()
    cur.execute("SELECT * FROM staff WHERE st_ID = ?", (st_ID,))
    staff_info = cur.fetchall()
    sql_conn.close()
    return staff_info[0]

# Modify staff information
def modify_staff(st_ID, st_name, st_dob, st_address, st_phone, st_email):
    sql_conn = sqlite3.connect("bookstore.db")
    st_ID = str(st_ID)
    st_name = str(st_name)
    st_dob = str(st_dob)
    st_address = str(st_address)
    st_phone = str(st_phone)
    st_email = str(st_email)
    cur = sql_conn.cursor()
    cur.execute("UPDATE staff SET st_name = ?, st_dob = ?, st_address = ?, st_phone = ?, st_email = ? WHERE st_ID = ?", (st_name, st_dob, st_address, st_phone, st_email, st_ID))
    sql_conn.commit()

    # Verify if staff is saved or not
    cur.execute("SELECT * FROM staff WHERE st_ID = ?", (st_ID,))
    staff = cur.fetchall()
    if staff:
        print("Staff modified successfully!")
        sql_conn.close()
        return True
    else:
        print("Staff not modified!")
        sql_conn.close()
        return False
    
# Delete staff
def delete_staff(st_ID):
    sql_conn = sqlite3.connect("bookstore.db")
    cur = sql_conn.cursor()
    # Set st_ID as string
    st_ID = str(st_ID)
    cur.execute("DELETE FROM staff WHERE st_ID = ?", (st_ID,))
    sql_conn.commit()

    # Verify if staff is deleted or not
    cur.execute("SELECT * FROM staff WHERE st_ID = ?", (st_ID,))
    staff = cur.fetchall()
    if staff:
        print("Staff not deleted!")
        sql_conn.close()
        return False
    else:
        print("Staff deleted successfully!")
        sql_conn.close()
        return True

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
