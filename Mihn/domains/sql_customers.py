import sqlite3

class Database:
    def __init__(self):
        self.dbConnection = sqlite3.connect("bookstore.db")
        self.dbCursor = self.dbConnection.cursor()
        self.dbCursor.execute("CREATE TABLE IF NOT EXISTS customers (id PRIMARYKEY text, name text, dob text, address text, phone text, email text)")

    def Insert(self, id, name, dob, address, phone, email):
        self.dbCursor.execute("INSERT INTO customers VALUES (?, ?, ?, ?, ?, ?)", (id, name, dob, address, phone, email))
        self.dbConnection.commit()

    def Update(self, name, dob, address, phone, email, id):
        self.dbCursor.execute("UPDATE customers SET name = ?, dob = ?, address = ?, phone = ?, email = ? WHERE id = ?", (name, dob, address, phone, email, id))
        self.dbConnection.commit()

    def Validate(self, id, phone, email ,mode):
        if (mode == 1):
            self.dbCursor.execute("SELECT * FROM customers WHERE id = ? OR phone = ? OR email = ?", (id, phone, email))
        else:
            self.dbCursor.execute("SELECT * FROM customers WHERE id != ? AND (phone = ? OR email = ?)", (id, phone, email))
        searchResults = self.dbCursor.fetchall()
        if (len(searchResults)==0):
            return False
        else:
            return True

    def Search(self, id):
        self.dbCursor.execute("SELECT * FROM customers WHERE id = ?", (id, ))
        searchResults = self.dbCursor.fetchall()
        return searchResults

    def Delete(self, id):
        self.dbCursor.execute("DELETE FROM customers WHERE id = ?", (id, ))
        self.dbConnection.commit()

    def select_all(self):
        self.dbCursor.execute("SELECT * FROM customers")
        records = self.dbCursor.fetchall()
        return records
    
    def __close__(self):
        self.dbCursor.close()
        self.dbConnection.close()
