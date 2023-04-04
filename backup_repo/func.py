import sqlite3

# Create database connection [DONE]
def create_connection():
    sql_conn = sqlite3.connect("bookstore.db")
    cur = sql_conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS book (book_id TEXT PRIMARY KEY, book_name TEXT, book_author TEXT, book_publisher TEXT, book_price REAL, book_quantity INTEGER)")
    cur.execute("CREATE TABLE IF NOT EXISTS store (store_id TEXT PRIMARY KEY, store_name TEXT, store_address TEXT, store_phone TEXT, store_email TEXT)")
    cur.execute("CREATE TABLE IF NOT EXISTS staff (st_ID TEXT PRIMARY KEY, st_pwd TEXT, st_name TEXT, st_dob TEXT, st_address TEXT, st_phone TEXT, st_email TEXT)")
    cur.execute("CREATE TABLE IF NOT EXISTS customer (cu_ID TEXT PRIMARY KEY, cu_name TEXT, cu_dob TEXT, cu_address TEXT, cu_phone TEXT, cu_email TEXT)")
    sql_conn.commit()
    sql_conn.close()

# If store is not created, create one [DONE]
def create_store_if_not_exist():
    sql_conn = sqlite3.connect("bookstore.db")
    cur = sql_conn.cursor()
    cur.execute("SELECT * FROM store")
    store = cur.fetchall()
    if not store:
        print("New database created. Creating store information...")
        cur.execute("INSERT INTO store VALUES (?, ?, ?, ?, ?)", ("", "", "", "", ""))
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
        return True
    else:
        print("Store not modified!")
        sql_conn.close()
        return False

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
def add_staff(st_ID, st_pwd, st_name, st_dob, st_address, st_phone, st_email):
    sql_conn = sqlite3.connect("bookstore.db")
    cur = sql_conn.cursor()
    # Add new staff
    cur.execute("INSERT INTO staff VALUES (?, ?, ?, ?, ?, ?, ?)", (st_ID, st_pwd, st_name, st_dob, st_address, st_phone, st_email))
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
    
def check_staff_table():
    sql_conn = sqlite3.connect("bookstore.db")
    cur = sql_conn.cursor()
    cur.execute("SELECT * FROM staff")
    staff = cur.fetchall()
    if staff:
        sql_conn.close()
        return True
    else:
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
def modify_staff(st_ID, st_pwd, st_name, st_dob, st_address, st_phone, st_email):
    sql_conn = sqlite3.connect("bookstore.db")
    st_ID = str(st_ID)
    st_name = str(st_name)
    st_dob = str(st_dob)
    st_address = str(st_address)
    st_phone = str(st_phone)
    st_email = str(st_email)
    cur = sql_conn.cursor()
    # Modify staff
    cur.execute("UPDATE staff SET st_name = ?, st_pwd = ?, st_dob = ?, st_address = ?, st_phone = ?, st_email = ? WHERE st_ID = ?", (st_name, st_pwd, st_dob, st_address, st_phone, st_email, st_ID))
    sql_conn.commit()
    print("Staff modified successfully!")
    
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

def check_cus_table():
    sql_conn = sqlite3.connect("bookstore.db")
    cur = sql_conn.cursor()
    cur.execute("SELECT * FROM customer")
    staff = cur.fetchall()
    if staff:
        sql_conn.close()
        return True
    else:
        sql_conn.close()
        return False

# CUSTOMER

# Check if customer ID exists [DONE]
def check_cu(cu_ID, cu_phone, cu_email):
    sql_conn = sqlite3.connect("bookstore.db")
    cur = sql_conn.cursor()
    cur.execute("SELECT * FROM customer WHERE cu_ID = ? OR cu_phone = ? OR cu_email = ?", (cu_ID, cu_phone, cu_email))
    customer = cur.fetchall()
    # If customer exists, return True
    if customer:
        print("customer already exists!")
        sql_conn.close()
        return True
    else:
        print("customer does not exist yet!")
        sql_conn.close()
        return False
    

# Add new customer [DONE]
def add_customer(cu_ID, cu_name, cu_dob, cu_address, cu_phone, cu_email):
    sql_conn = sqlite3.connect("bookstore.db")
    cur = sql_conn.cursor()
    # Add new customer
    cur.execute("INSERT INTO customer VALUES (?, ?, ?, ?, ?, ?)", (cu_ID, cu_name, cu_dob, cu_address, cu_phone, cu_email))
    sql_conn.commit()
    cur.execute("SELECT * FROM customer WHERE cu_ID = ?", (cu_ID,))
    customer = cur.fetchall()
    if customer:
        print("customer added successfully!")
        sql_conn.close()
        return True
    else:
        print("customer not added!")
        sql_conn.close()
        return False
    
def check_customer_table():
    sql_conn = sqlite3.connect("bookstore.db")
    cur = sql_conn.cursor()
    cur.execute("SELECT * FROM customer")
    customer = cur.fetchall()
    if customer:
        sql_conn.close()
        return True
    else:
        sql_conn.close()
        return False
    
# Get customer list from database to create a dropdown list [DONE]
def get_customer_list():
    sql_conn = sqlite3.connect("bookstore.db")
    cur = sql_conn.cursor()
    cur.execute("SELECT * FROM customer")
    customer_info = cur.fetchall()
    sql_conn.close()
    return customer_info

def get_customer_info(cu_ID):
    sql_conn = sqlite3.connect("bookstore.db")
    cur = sql_conn.cursor()
    cur.execute("SELECT * FROM customer WHERE cu_ID = ?", (cu_ID,))
    customer_info = cur.fetchall()
    sql_conn.close()
    return customer_info[0]

# Modify customer information
def modify_customer(cu_ID, cu_name, cu_dob, cu_address, cu_phone, cu_email):
    sql_conn = sqlite3.connect("bookstore.db")
    cu_ID = str(cu_ID)
    cu_name = str(cu_name)
    cu_dob = str(cu_dob)
    cu_address = str(cu_address)
    cu_phone = str(cu_phone)
    cu_email = str(cu_email)
    cur = sql_conn.cursor()
    # Modify customer
    cur.execute("UPDATE customer SET cu_name = ?, cu_dob = ?, cu_address = ?, cu_phone = ?, cu_email = ? WHERE cu_ID = ?", (cu_name, cu_dob, cu_address, cu_phone, cu_email, cu_ID))
    sql_conn.commit()
    print("customer modified successfully!")
    
# Delete customer
def delete_customer(cu_ID):
    sql_conn = sqlite3.connect("bookstore.db")
    cur = sql_conn.cursor()
    # Set cu_ID as string
    cu_ID = str(cu_ID)
    cur.execute("DELETE FROM customer WHERE cu_ID = ?", (cu_ID,))
    sql_conn.commit()

    # Verify if customer is deleted or not
    cur.execute("SELECT * FROM customer WHERE cu_ID = ?", (cu_ID,))
    customer = cur.fetchall()
    if customer:
        print("customer not deleted!")
        sql_conn.close()
        return False
    else:
        print("customer deleted successfully!")
        sql_conn.close()
        return True

# Path: main.py
