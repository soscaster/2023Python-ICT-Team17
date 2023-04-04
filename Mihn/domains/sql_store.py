import sqlite3

class Database:
    def __init__(self):
        self.dbConnection = sqlite3.connect("bookstore.db")
        self.dbCursor = self.dbConnection.cursor()
        self.dbCursor.execute("CREATE TABLE IF NOT EXISTS store (id PRIMARYKEY text, name text, address text, phone text, email text)")

    def Insert(self, id, name, address, phone, email):
        self.dbCursor.execute("INSERT INTO store VALUES (?, ?, ?, ?, ?)", (id, name, address, phone, email))
        self.dbConnection.commit()

    def Update(self, name, address, phone, email, id):
        self.dbCursor.execute("UPDATE store SET name = ?, address = ?, phone = ?, email = ?, id = ?", (id, name, address, phone, email))
        self.dbConnection.commit()

    def Delete(self):
        self.dbCursor.execute("DELETE * FROM store")
        self.dbConnection.commit()

    def select_all(self):
        self.dbCursor.execute("SELECT * FROM store")
        records = self.dbCursor.fetchall()
        return records

    def __close__(self):
        self.dbCursor.close()
        self.dbConnection.close()