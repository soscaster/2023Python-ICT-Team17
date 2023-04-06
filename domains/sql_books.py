import sqlite3

class Database:
    def __init__(self):
        self.dbConnection = sqlite3.connect("bookstore.db")
        self.dbCursor = self.dbConnection.cursor()
        self.dbCursor.execute("CREATE TABLE IF NOT EXISTS books (id text, title text, genre text, author text, target text, publisher text, price int, quantity int, PRIMARY KEY (id))")

    def Insert(self, id, title, genre, author, target, publisher, price, quantity):
        self.dbCursor.execute("INSERT INTO books VALUES (?, ?, ?, ?, ?, ?, ?, ?)", (id, title, genre, author, target, publisher, price, quantity))
        self.dbConnection.commit()

    def Update(self, title, genre, author, target, publisher, price, quantity, id):
        self.dbCursor.execute("UPDATE books SET title = ?, genre = ?, author = ?, target = ?, publisher = ?, price = ?, quantity = ? WHERE id = ?", (title, genre, author, target, publisher, price, quantity, id))
        self.dbConnection.commit()
    
    def Validate(self, id, title, author, mode):
        if (mode==1):
            self.dbCursor.execute("SELECT * FROM books WHERE id = ? or (title = ? and author = ?)", (id, title, author))
        else:
            self.dbCursor.execute("SELECT * FROM books WHERE id != ? and title = ? and author = ?", (id, title, author))
        searchResults = self.dbCursor.fetchall()
        if (len(searchResults)==0):
            return False
        else:
            return True

    def Search(self, id):
        self.dbCursor.execute("SELECT * FROM books WHERE id = ?", (id, ))
        searchResults = self.dbCursor.fetchall()
        return searchResults

    def Searchall(self, id, title, genre, author, target, publisher, price1, price2, quantity1, quantity2):
        self.dbCursor.execute("SELECT * FROM books WHERE id like '%%%s%%' AND title like '%%%s%%' AND genre like '%%%s%%' AND author like '%%%s%%' AND target like '%%%s%%' AND publisher like '%%%s%%' AND price >= ? AND price <= ? AND quantity >= ? AND quantity <= ?" % (id, title, genre, author, target, publisher), (price1, price2, quantity1, quantity2))
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