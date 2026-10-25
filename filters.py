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

    # mycursor.execute("SELECT * FROM products Where id = 1")
    # mycursor.execute("SELECT * FROM products Where name = '17'")
    # mycursor.execute("SELECT * FROM products Where id < 7 and price > 5000")
    # mycursor.execute("SELECT * FROM products Where name = 'Samsung S5' or price > 5000")
    mycursor.execute(
        "SELECT * FROM products Where name LIKE '%Samsung%'"
    )  # name içinde Samsung geçenleri getirir
    # mycursor.execute("SELECT * FROM products Where name LIKE 'Samsung%'")
    # mycursor.execute("SELECT * FROM products Where name LIKE '%Samsung'")
    mycursor.execute(
        "SELECT * FROM products Where name LIKE '%Samsung%' and price > 5000"
    )

    result = mycursor.fetchall()  # Liste getirir, for kullanılabilir
    # result = mycursor.fetchone()  # ilk kaydı getirir, liste getirmez, for kullanılamaz

    print(result)

    for product in result:
        print(product)


def getProductById(id):
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="er23Taylan/",
        database="node-app",  # 192.23.45.56
        auth_plugin="mysql_native_password",
    )

    mycursor = connection.cursor()

    sql = "Select *From Products Where id=%s"
    params = id

    mycursor.execute(sql, params)

    result = mycursor.fetchone()

    print(result)
