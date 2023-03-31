import sqlite3
import dbfunc

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