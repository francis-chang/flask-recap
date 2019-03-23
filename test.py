import sqlite3

connection = sqlite3.connect('data.db')

cursor = connection.cursor()

create_table = "CREATE TABLE users (id int, username text, password text)"
cursor.execute(create_table)


user = (1, 'jose', 'asdf')
insert_query = "INSERT INTO users VALUES (?, ?, ?)"
cursor.execute(insert_query, user)

users = [
    (12, 'joswete', 'as3df'),
    (2, 'joswee', 'asd5f'),
    (3, 'joshae', 'as6df'),
    (4, 'jogrese', 'a7sdf'),
    (5, 'hert', 'asd1f'),
]


cursor.executemany(insert_query, users)

select_query = "SELECT * FROM users"

for row in cursor.execute(select_query):
    print(row)

connection.commit()

connection.close()
