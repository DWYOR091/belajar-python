from connection import create_connection

mydb= create_connection()
c = mydb.cursor()

sql="SELECT * FROM users WHERE id = %s"
c.execute(sql,(1,))
result = c.fetchall()
print(result)
