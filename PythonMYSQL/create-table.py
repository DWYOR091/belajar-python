# import connection as conn
from connection import create_connection

mydb = create_connection()

mycursor = mydb.cursor()

# mycursor.execute("CREATE TABLE Users (name VARCHAR(255), address VARCHAR(255))")
# mycursor.execute("ALTER TABLE users ADD COLUMN id INT AUTO_INCREMENT PRIMARY KEY")
mycursor.execute("SHOW TABLES")
for table in mycursor:
    print(table)
    
