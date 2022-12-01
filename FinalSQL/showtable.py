# SQL Final Code
import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="bob1234",
    database="menagerie"
    )

my_cursor = mydb.cursor()

my_cursor.execute("SHOW TABLES")

for tb in my_cursor:
    print(tb)
