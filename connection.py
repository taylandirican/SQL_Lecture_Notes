import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="er23Taylan/",
    database="schooldb",
    auth_plugin="mysql_native_password",
)
