from connection import create_connection

mydb = create_connection()

c = mydb.cursor()

sql = "INSERT INTO users (name,address) VALUES (%s,%s)"
value = ("rifqi","kerkof")
c.execute(sql,value)
mydb.commit()
print("data berhasil tersimpan")
c.close()
mydb.close()






