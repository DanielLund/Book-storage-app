"""
this is for storing and retrieving books from a list
"""
import sqlite3


def create_book_table():
    connection = sqlite3.connect('data.db')
    cursor = connection.cursor()

    cursor.execute('CREATE TABLE IF NOT EXISTS books(title text, author text, read integer)')

    connection.commit()
    connection.close()


def get_all_books():
    connection = sqlite3.connect('data.db')
    cursor = connection.cursor()

    cursor.execute('SELECT * FROM books')
    books = [{'title': row[0], 'author': row[1], 'read': row[2]} for row in cursor.fetchall()]

    connection.close()

    return books


def add_book(title, author):
    connection = sqlite3.connect('data.db')
    cursor = connection.cursor()

    cursor.execute('INSERT INTO books VALUES(?, ?, 0)', (title, author))

    #using format string is bad because it allows for SQL injection attacks using DROP TABLE command and others.

    connection.commit()
    connection.close()


def mark_book_read(title):
    connection = sqlite3.connect('data.db')
    cursor = connection.cursor()

    cursor.execute('UPDATE books SET read=1 WHERE title=?', (title,))

    connection.commit()
    connection.close()


def delete_book(title):
    connection = sqlite3.connect('data.db')
    cursor = connection.cursor()

    cursor.execute('DELETE FROM books WHERE title=?', (title,))

    connection.commit()
    connection.close()

