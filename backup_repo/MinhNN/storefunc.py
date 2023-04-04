import sqlite3
import dbfunc

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