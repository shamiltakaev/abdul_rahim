import sqlite3

conn = sqlite3.connect('characters_file_db.sqlite')
cursor = conn.cursor()
cursor.execute('''CREATE TABLE users (id INTEGER PRIMARY KEY, Name TEXT, Surname TEXT, Species TEXT, From_place TEXT, Motion INT)''')

conn.close()
