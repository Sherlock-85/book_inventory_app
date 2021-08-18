import sqlite3

def connect():
    connection = sqlite3.connect("books.db")
    cur = connection.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS book (id INTEGER PRIMARY KEY, title text, author text, year integer,"
                " isbn integer)")
    connection.commit()
    connection.close()

def insert(title, author, year, isbn):
    connection = sqlite3.connect("books.db")
    cur = connection.cursor()
    cur.execute("INSERT INTO book VALUES(NULL,?,?,?,?)", (title, author, year, isbn))
    connection.commit()
    connection.close()

def view():
    connection = sqlite3.connect("books.db")
    cur = connection.cursor()
    cur.execute("SELECT * FROM book")
    rows = cur.fetchall()
    connection.close()
    return rows

def search(title="", author="", year="", isbn=""):
    connection = sqlite3.connect("books.db")
    cur = connection.cursor()
    cur.execute("SELECT * FROM book WHERE title=? OR author=? OR year=? OR isbn=?", (title, author, year, isbn))
    rows = cur.fetchall()
    connection.close()
    return rows

def delete(id):
    connection = sqlite3.connect("books.db")
    cur = connection.cursor()
    cur.execute("DELETE FROM book WHERE id=?", (id,))
    connection.commit()
    connection.close()

def update(id, title, author, year, isbn):
    connection = sqlite3.connect("books.db")
    cur = connection.cursor()
    cur.execute("UPDATE book SET title=?, author=?, year=?, isbn=? WHERE id=?", (title, author, year, isbn, id))
    connection.commit()
    connection.close()


connect()
# insert("Mars", "Gustav Holst", 1945, 973417025)
# delete(2)
# update(8, "Jupiter", "James Nathaniel", 1917, 997662414, )
# print(view())
# print(search(author="Frank Dreadful"))