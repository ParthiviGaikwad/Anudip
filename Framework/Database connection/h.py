import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="sam726"
)

print(mydb)

mycursor = mydb.cursor()

mycursor.execute("create database parthivi")
mycursor.execute("Show databases")

for x in mycursor:
  print(x)
