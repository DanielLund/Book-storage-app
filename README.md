# Book Storage/Library app
Updated my code to use SQLite3 instead so it doesn't just store the "database" in memory and doesn't get deleted when reran. Only changes were to the interface 'database.py' nothing changed on 'app.py' apart from a variable name change in the prompt_delete_book function.

Further updated my code to include context managers in a new file called Database_Connection so there's no need to repeat boilerplate code to start, commit and close SQLite connections.
