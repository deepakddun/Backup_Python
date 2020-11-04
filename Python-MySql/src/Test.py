import mysql.connector as db

mydb = db.connect(host="localhost", user="root", password="123456")

mycursor = mydb.cursor()

mycursor.execute("CREATE DATABASE IF NOT EXISTS mydatabase")

mycursor.execute("USE mydatabase")

mycursor.execute(
    "CREATE TABLE IF NOT EXISTS customers1 (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), address VARCHAR(255))")





sql = "INSERT INTO customers1 (name, address) VALUES (%s, %s)"
val = [
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

mycursor.executemany(sql, val)

mydb.commit()

mycursor = mydb.cursor()

mycursor.execute("SELECT name, address FROM customers1")

myresult = mycursor.fetchall()

for x in myresult:
  print(x.name)

