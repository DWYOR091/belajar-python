import connection

try:
    mydb = connection.create_connection()
    c = mydb.cursor()
    sql = "UPDATE users SET name = %s WHERE id = %s"
    c.execute(sql,("Hehehe",3))
    mydb.commit()
    print(c.rowcount, "record updated")
except Exception as e:
    print("error:",e)
finally:
    c.close()
    mydb.close()
