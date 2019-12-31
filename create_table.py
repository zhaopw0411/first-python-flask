import sqlite3

# connect to a file data.db
connection = sqlite3.connect('data.db')

# cursor will run a query and store the result
cursor = connection.cursor()


create_table = """CREATE TABLE if not exists users 
            (id INTEGER PRIMARY KEY, 
            username text, 
            password text)"""


cursor.execute(create_table)


create_table = """CREATE TABLE if not exists items 
            (id INTEGER PRIMARY KEY, 
             name text,
             price real)"""

cursor.execute(create_table)

#cursor.execute("""insert into items values ('test', 10.99)""")

connection.commit()
connection.close()