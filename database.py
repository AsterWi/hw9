# 14th of December 2024
# SQlite database
# Task: Create database with date-time and temperature. Find temperature info and insert data.

import sqlite3

connection = sqlite3.connect('database.db')
cur = connection.cursor()

# cur.execute("""
#     CREATE TABLE amongus (
#         id INTEGER PRIMARY KEY AUTOINCREMENT,
#         dt TEXT,
#         temp INTEGER
#     );
# """)

# cur.execute("INSERT INTO amongus (dt, temp) VALUES ('12.14.2024 1PM', -3);")
# cur.execute("INSERT INTO amongus (dt, temp) VALUES ('12.15.2024 1AM', -17);")
# cur.execute("INSERT INTO amongus (dt, temp) VALUES ('12.16.2024 1AM', -15);")

cur.execute("SELECT * FROM amongus;")
amongus = cur.fetchall()

for among in amongus:
    print(among)

connection.commit()
connection.close()

