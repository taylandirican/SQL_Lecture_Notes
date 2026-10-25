import mysql.connector


def getProducts():
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="er23Taylan/",
        database="node-app",  # 192.23.45.56
        auth_plugin="mysql_native_password",
    )

    mycursor = connection.cursor()

    # mycursor.execute("SELECT * FROM products")
    mycursor.execute("SELECT name,price FROM products")

    # result = mycursor.fetchall()
    result = mycursor.fetchone()  # ilk kaydı getirir

    for product in result:
        print(product)


getProducts()
