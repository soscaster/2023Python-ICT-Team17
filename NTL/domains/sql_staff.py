import sqlite3

class Database:
    def __init__(self):
        self.dbConnection = sqlite3.connect("bookstore.db")
        self.dbCursor = self.dbConnection.cursor()
        self.dbCursor.execute("CREATE TABLE IF NOT EXISTS staff (id PRIMARYKEY text, password text, name text, dob text, address text, phone text, email text)")

    def Insert(self, id, pwd, name, dob, address, phone, email):
        self.dbCursor.execute("INSERT INTO staff VALUES (?, ?, ?, ?, ?, ?, ?)", (id, pwd, name, dob, address, phone, email))
        self.dbConnection.commit()

    def Update(self, pwd, name, dob, address, phone, email, salary, id):
        self.dbCursor.execute("UPDATE staff SET password = ?, name=?, dob = ?, address = ?, phone = ?, email = ?, salary = ? WHERE id = ?", (pwd, name, dob, address, phone, email, salary, id))
        self.dbConnection.commit()

    def Validate(self, id, phone, email ,mode):
        if (mode == 1):
            self.dbCursor.execute("SELECT * FROM staff WHERE id = ? OR phone = ? OR email = ?", (id, phone, email))
        else:
            self.dbCursor.execute("SELECT * FROM staff WHERE id != ? AND (phone = ? OR email = ?)", (id, phone, email))
        searchResults = self.dbCursor.fetchall()
        if (len(searchResults)==0):
            return False
        else:
            return True

    def Search(self, id):
        self.dbCursor.execute("SELECT * FROM staff WHERE id = ?", (id, ))
        searchResults = self.dbCursor.fetchall()
        return searchResults
    
    def Searchall(self, id, name, dob, address, phone, email):
        self.dbCursor.execute("SELECT * FROM staff WHERE id like '%%%s%%' AND name like '%%%s%%' AND dob like '%%%s%%' AND address like '%%%s%%' AND phone like '%%%s%%' AND email like '%%%s%%'" % (id, name, dob, address, phone, email))
        searchResults = self.dbCursor.fetchall()
        return searchResults

    def Delete(self, id):
        self.dbCursor.execute("DELETE FROM staff WHERE id = ?", (id, ))
        self.dbConnection.commit()

    def Storage(self):
        self.dbCursor.execute("SELECT * FROM staff")
        records = self.dbCursor.fetchall()
        return records

    def __close__(self):
        self.dbCursor.close()
        self.dbConnection.close()