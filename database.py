"""
this is for storing and retrieving books from a list
"""
from .Database_Connection import DatabaseConnection


def create_book_table():
    with DatabaseConnection('data.db') as connection:
        cursor = connection.cursor()

        cursor.execute('CREATE TABLE IF NOT EXISTS books(title text, author text, read integer)')



def get_all_books():
    with DatabaseConnection('data.db') as connection:
        cursor = connection.cursor()

        cursor.execute('SELECT * FROM books')
        books = [{'title': row[0], 'author': row[1], 'read': row[2]} for row in cursor.fetchall()]


    return books


def add_book(title, author):
   with DatabaseConnection('data.db') as connection:
        cursor = connection.cursor()

        cursor.execute('INSERT INTO books VALUES(?, ?, 0)', (title, author))

    #using format string is bad because it allows for SQL injection attacks.


def mark_book_read(title):
    with DatabaseConnection('data.db') as connection:
        cursor = connection.cursor()

        cursor.execute('UPDATE books SET read=1 WHERE title=?', (title,))


def delete_book(title):
    with DatabaseConnection('data.db') as connection:
        cursor = connection.cursor()

        cursor.execute('DELETE FROM books WHERE title=?', (title,))
