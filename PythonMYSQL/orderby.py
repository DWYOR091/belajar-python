from connection import create_connection

mydb= create_connection()
c = mydb.cursor()
c.execute("SELECT * FROM users ORDER BY name ASC")
result = c.fetchall()
for user in result:
    print(user)
    