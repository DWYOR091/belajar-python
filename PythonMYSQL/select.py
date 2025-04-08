from connection import create_connection

mydb = create_connection()

c = mydb.cursor()
c.execute("SELECT * FROM users")
# for user in c:
#     print(user)
    
myresult=c.fetchone()
print(myresult)