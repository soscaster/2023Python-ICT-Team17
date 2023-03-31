import sqlite3
import dbfunc

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