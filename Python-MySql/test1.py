import mysql.connector as db

print("Initial DB Setup")
mydb = db.connect(host="localhost", user="root", password="123456")
mycursor = mydb.cursor()
print(mydb.connection_id)

mycursor.execute("SHOW DATABASES")

for x in mycursor:
  print(x)