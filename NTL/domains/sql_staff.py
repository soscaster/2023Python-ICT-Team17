import sqlite3

class Database:
    def __init__(self):
        self.dbConnection = sqlite3.connect("bookstore.db")
        self.dbCursor = self.dbConnection.cursor()
        self.dbCursor.execute("CREATE TABLE IF NOT EXISTS staff (id PRIMARYKEY text, password text, name text, dob text, address text, phone text, email text, salary int)")

    def Insert(self, id, pwd, name, dob, address, phone, email, salary):
        self.dbCursor.execute("INSERT INTO staff VALUES (?, ?, ?, ?, ?, ?, ?, ?)", (id, pwd, name, dob, address, phone, email, salary))
        self.dbConnection.commit()

    def Update(self, pwd, name, dob, address, phone, email, salary, id):
        self.dbCursor.execute("UPDATE staff SET password = ?, name=?, dob = ?, address = ?, phone = ?, email = ?, salary = ? WHERE id = ?", (pwd, name, dob, address, phone, email, salary, id))
        self.dbConnection.commit()

    def Update_salary(self,salary,id):
        self.dbCursor.execute("UPDATE staff SET salary = ? WHERE id = ?", (salary, id))
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