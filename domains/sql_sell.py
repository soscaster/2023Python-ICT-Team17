import sqlite3
import datetime

class Sell:
    def __init__(self):
        self.dbConnection = sqlite3.connect("bookstore.db")
        self.dbCursor = self.dbConnection.cursor()
        self.dbCursor.execute("CREATE TABLE IF NOT EXISTS sell (id text, book_id text, book_title text, price int, quantity int, cus_id text, cus_name text, staff_id text, staff_name text, time TIMESTAMP, PRIMARY KEY (id))")

    def Insert(self, book_id, book_title, price, quantity, cus_id, cus_name, staff_id, staff_name):
        # Count number of records
        self.dbCursor.execute("SELECT COUNT(*) FROM sell")
        count = int(self.dbCursor.fetchone()[0]) + 1
        count_txt = str(count)
        time = str(datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S"))
        self.dbCursor.execute("INSERT INTO sell VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", (count_txt, book_id, book_title, price, quantity, cus_id, cus_name, staff_id, staff_name, time))
        self.dbConnection.commit()
    
    def Storage(self):
        self.dbCursor.execute("SELECT * FROM sell")
        return self.dbCursor.fetchall()

    def __close__(self):
        self.dbCursor.close()
        self.dbConnection.close()