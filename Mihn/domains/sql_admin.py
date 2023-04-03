import sqlite3

class Database:
    def __init__(self):
        self.dbConnection = sqlite3.connect("bookstore.db")
        self.dbCursor = self.dbConnection.cursor()
        self.dbCursor.execute("CREATE TABLE IF NOT EXISTS admin (id PRIMARYKEY text, name text, dob text, phone text, email text)")

    def Insert(self, id, name, dob, phone, email):
        self.dbCursor.execute("INSERT INTO admin VALUES (?, ?, ?, ?, ?)", (id, name, dob, phone, email))
        self.dbConnection.commit()

    def Update(self, name, dob, phone, email, id):
        self.dbCursor.execute("UPDATE admin SET name = ?, dob = ?, phone = ?, email = ? WHERE id = ?", (name, dob, phone, email, id))
        self.dbConnection.commit()
    
    def Validate(self, id, phone, email ,mode):
        if (mode == 1):
            self.dbCursor.execute("SELECT * FROM admin WHERE id = ? OR phone = ? OR email = ?", (id, phone, email))
        else:
            self.dbCursor.execute("SELECT * FROM admin WHERE id != ? AND (phone = ? OR email = ?)", (id, phone, email))
        searchResults = self.dbCursor.fetchall()
        if (len(searchResults)==0):
            return False
        else:
            return True

    def Search(self, id):
        self.dbCursor.execute("SELECT * FROM admin WHERE id = ?", (id, ))
        searchResults = self.dbCursor.fetchall()
        return searchResults

    def Delete(self, id):
        self.dbCursor.execute("DELETE FROM admin WHERE id = ?", (id, ))
        self.dbConnection.commit()

    def select_all(self):
        self.dbCursor.execute("SELECT * FROM admin")
        records = self.dbCursor.fetchall()
        return records
    
    def __close__(self):
        self.dbCursor.close()
        self.dbConnection.close()
