import mysql.connector

my_db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="bob1234",
    database="menagerie"
    )

my_sql = "INSERT INTO pet (name, owner, species, sex, birth, death) \
      VALUES (%s, %s, %s, %s, %s, %s)"

pet = [
    "('Fluffy','Harold', 'cat', 'f','1993-02-04'),\
    ('Claws','Gwen', 'cat', 'm','1994-03-17'),\
    ('Buffy','Harold', 'dog', 'f','1989-05-13',),\
    ('Fang','Benny', 'dog', 'm','1990-08-27'),\
    ('Bowser','Diane', 'dog', 'm','1979-08-31','1995-07-29'),\
    ('Chripy','Gwen', 'bird', 'f','1998-09-11'),\
    ('Whistler','Gwen', 'bird', 'NULL','1997-12-09'),\
    ('Slim','Benny', 'snake', 'm','1996-04-29'),\
    ('Puffball','Diane', 'hamster', 'f','1999-03-30')"
    ]

cursor = my_db.cursor(my_sql, pet)

