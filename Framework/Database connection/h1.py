import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="sam726",
  database="parthividb"
)

mycursor=mydb.cursor()

#mycursor.execute("CREATE TABLE customers (name VARCHAR(255), address VARCHAR(255))")
mycursor.execute("show tables")
for x in mycursor:
    print(x)
