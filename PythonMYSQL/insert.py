from connection import create_connection

mydb = create_connection()

c = mydb.cursor()

sql = "INSERT INTO users (name,address) VALUES (%s,%s)"
# value = ("rifqi","kerkof")
# c.execute(sql,value)
value = [
  ('Peter', 'Lowstreet 4'),
  ('Amy', 'Apple st 652'),
  ('Hannah', 'Mountain 21'),
  ('Michael', 'Valley 345'),
  ('Sandy', 'Ocean blvd 2'),
  ('Betty', 'Green Grass 1'),
  ('Richard', 'Sky st 331'),
  ('Susan', 'One way 98'),
  ('Vicky', 'Yellow Garden 2'),
  ('Ben', 'Park Lane 38'),
  ('William', 'Central st 954'),
  ('Chuck', 'Main Road 989'),
  ('Viola', 'Sideway 1633')
]
#execute many
c.executemany(sql,value)
mydb.commit()
print("data berhasil tersimpan")
print("1 record inserted, ID:", c.lastrowid)
c.close()
mydb.close()







