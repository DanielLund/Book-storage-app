"""
this is for storing and retrieving books from a list
"""
import json


books_file = 'books.json'


def create_book_table():
    with open(books_file, 'w') as file:
        json.dump([], file)


def get_all_books():
    with open(books_file, 'r') as file:
        return json.load(file)


def add_book(title, author):
    books = get_all_books()
    books.append({
        'title': title,
        'author': author,
        'read': False
    })
    _save_all_books(books)


def _save_all_books(books):
    with open(books_file, 'w') as file:
        json.dump(books, file)


def mark_book_read(title):
    books = get_all_books()
    for book in books:
        if book['title'] == title:
            book['read'] = True
    _save_all_books(books)


def delete_book(name):
    books = get_all_books()
    books = [book for book in books if book['title'] != name]
    _save_all_books(books)
