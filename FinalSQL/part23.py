import mysql.connector

my_db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="bob1234",
    database="menagerie"
    )

my_cursor = my_db.cursor()

my_cursor.execute("SELECT owner, COUNT(*) FROM pet GROUP BY owner")

for tb in my_cursor:
    print(tb)


