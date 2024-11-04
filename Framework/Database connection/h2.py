import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="sam726",
  database="parthividb"
)

mycursor=mydb.cursor()


mycursor = mydb.cursor()

sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
val = ("John", "Highway 21")
mycursor.execute(sql, val)

mycursor.execute("Insert into customers values ('Parthivi','K')")

mydb.commit()

print(mycursor.rowcount, "record inserted.")
