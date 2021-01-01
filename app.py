from utils import database

USER_CHOICE = """
Enter:
- 'a' to add a new book
- 'l' to list all books
- 'r' to mark a book as read
- 'd' to delete a book 
- 'q' to quit

Your choice: """


def prompt_add_book():
    title = input("Enter the title of the book: ")
    author = input("Enter the author of the book: ")
    database.add_book(title, author)


def show_books():
    for book in database.get_all_books():
        read = 'YES' if book['read'] == 1 else 'NO'
        print(f"{book['title']} by {book['author']} - Read: {read}")


def mark_as_read():
    title = input('What is the title of the book you have read: ')
    database.mark_book_read(title)


def prompt_delete_book():
    title = input('what is the title of the book you want to delete: ')
    database.delete_book(title)


user_options = {
    'a': prompt_add_book,
    'l': show_books,
    'r': mark_as_read,
    'd': prompt_delete_book
}


def menu():
    database.create_book_table()
    user_input = input(USER_CHOICE)
    while user_input != 'q':
        if user_input in user_options:
            selected_function = user_options[user_input]
            selected_function()

        else:
            print('unknown command, please try again')

        user_input = input(USER_CHOICE)


menu()
