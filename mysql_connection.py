import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="er23Taylan/",
    database="node-app",  # 192.23.45.56
    auth_plugin="mysql_native_password",
)

mycursor = mydb.cursor()

# mycursor.execute("CREATE DATABASE mydatabase")
# mycursor.execute("SHOW DATABASES")

# for x in mycursor:
#     print(x)

# mycursor.execute("CREATE TABLE customers (name VARCHAR(255), address VARCHAR(255))")
