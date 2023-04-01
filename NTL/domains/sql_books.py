import sqlite3

class Database:
    def __init__(self):
        self.dbConnection = sqlite3.connect("bookstore.db")
        self.dbCursor = self.dbConnection.cursor()
        self.dbCursor.execute("CREATE TABLE IF NOT EXISTS books (id PRIMARYKEY text, title text, genre text, author text, target text, publisher text, price int, quantity int)")

    def Insert(self, id, title, genre, author, target, publisher, price, quantity):
        self.dbCursor.execute("INSERT INTO books VALUES (?, ?, ?, ?, ?, ?, ?, ?)", (id, title, genre, author, target, publisher, price, quantity))
        self.dbConnection.commit()

    def Update(self, title, genre, author, target, publisher, price, quantity, id):
        self.dbCursor.execute("UPDATE books SET title = ?, genre = ?, author = ?, target = ?, publisher = ?, price = ?, quantity = ? WHERE id = ?", (title, genre, author, target, publisher, price, quantity, id))
        self.dbConnection.commit()
    
    def Validate(self, id, title, mode):
        if (mode==1):
            self.dbCursor.execute("SELECT * FROM books WHERE id = ? or title = ?", (id, title))
        else:
            self.dbCursor.execute("SELECT * FROM books WHERE id != ? and title = ?", (id, title))
        searchResults = self.dbCursor.fetchall()
        if (len(searchResults)==0):
            return False
        else:
            return True

    def Search(self, id):
        self.dbCursor.execute("SELECT * FROM books WHERE id = ?", (id, ))
        searchResults = self.dbCursor.fetchall()
        return searchResults

    def Delete(self, id):
        self.dbCursor.execute("DELETE FROM books WHERE id = ?", (id, ))
        self.dbConnection.commit()

    def Storage(self):
        self.dbCursor.execute("SELECT * FROM books")
        records = self.dbCursor.fetchall()
        return records

    def __close__(self):
        self.dbCursor.close()
        self.dbConnection.close()