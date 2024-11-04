#show database connectivity in python
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="sam726"
)

mycursor=mydb.cursor()


#Create Employee database with emp table (eid,ename,edesig)
mycursor.execute("Create database Cmployee")
mycursor.execute("use Cmployee")
mycursor.execute("Create table emp (eid int, ename varchar(200), edesig varchar (200))")

#Q.1) insert minimum 5 records in it
sql = "INSERT INTO emp (eid, ename, edesig) VALUES (%s, %s,%s)"
val = [
  (1, 'A','Manager'),
  (10, 'B','Clerk'),
  (11, 'c','Assistant'),
  (100, 'D','Secretary'),
  (101, 'E','Intern')
]

mycursor.executemany(sql, val)


print(mycursor.rowcount, "record inserted.")
#Q.2)Fetchall the records

mycursor.execute("Select * from emp")
for x in mycursor:
    print (x)

mydb.commit()
