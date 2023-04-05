import sqlite3

class Session:
    def __init__(self):
        self.dbConnection = sqlite3.connect("bookstore.db")
        self.dbCursor = self.dbConnection.cursor()
        self.dbCursor.execute("CREATE TABLE IF NOT EXISTS session (id AUTO_INCREMENT int, usr_id text, usr_name text, PRIMARY KEY (id))")

    def Insert(self, usr_id, usr_name):
        # Count number of records
        self.dbCursor.execute("SELECT COUNT(*) FROM session")
        count = int(self.dbCursor.fetchone()[0]) + 1
        self.dbCursor.execute("INSERT INTO session VALUES (?, ?, ?)", (count, usr_id, usr_name))
        self.dbConnection.commit()

    def __close__(self):
        self.dbCursor.close()
        self.dbConnection.close()