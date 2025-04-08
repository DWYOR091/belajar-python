import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    # database="", #bisa buat db ketika buat connection
)

mycursor = mydb.cursor()

# mycursor.execute("CREATE DATABASE dbpython")
mycursor.execute("SHOW DATABASES")

for x in mycursor:
    print(x)


