# SQL Final Code
import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="bob1234",
    database="menagerie"
    )

my_cursor = mydb.cursor()

my_cursor.execute("CREATE TABLE pet(name VARCHAR(20),owner VARCHAR(20),"
                  "species VARCHAR(20),sex CHAR(1),birth DATE,death DATE)")


