import sqlite3
import datetime

class Session:
    def __init__(self):
        self.dbConnection = sqlite3.connect("bookstore.db")
        self.dbCursor = self.dbConnection.cursor()
        # Create table if not exists and set timezone to GMT +7
        self.dbCursor.execute("CREATE TABLE IF NOT EXISTS session (id int, usr_id text, usr_name text, time TIMESTAMP, PRIMARY KEY (id))")

    def Insert(self, usr_id, usr_name):
        # Count number of records
        self.dbCursor.execute("SELECT COUNT(*) FROM session")
        count = int(self.dbCursor.fetchone()[0]) + 1
        time = str(datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S"))
        self.dbCursor.execute("INSERT INTO session VALUES (?, ?, ?, ?)", (count, usr_id, usr_name, time))
        self.dbConnection.commit()

    def Print(self):
        # Print the last record
        self.dbCursor.execute("SELECT * FROM session ORDER BY id DESC LIMIT 1")
        return self.dbCursor.fetchone()

    def __close__(self):
        self.dbCursor.close()
        self.dbConnection.close()