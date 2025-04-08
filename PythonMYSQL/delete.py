from connection import create_connection

mydb = create_connection()
c = mydb.cursor()
sql = "DELETE FROM users WHERE id = %s"
c.execute(sql,(1,))
mydb.commit()
print(c.rowcount, "record deleted")
