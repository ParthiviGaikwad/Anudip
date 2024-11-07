import mysql.connector

mydb= mysql.connector.connect(
    host='localhost',
    user='root',
    password='sam726',
    database='Cmployee'
)

mycursor=mydb.cursor()

mycursor.execute("""
    CREATE TABLE product (
        product_id INT PRIMARY KEY,
        product_name VARCHAR(200),
        product_cost INT
    )
""")


sql="INSERT INTO product VALUES (%s, %s, %s)"
val=(1,"Abc",120)

mycursor.execute(sql,val)
mycursor.execute("Select * from product")
for x in mycursor:
     print (x)

mydb.commit()
