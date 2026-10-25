import mysql.connector


def getProductInfo():
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="er23Taylan/",
        database="node-app",  # 192.23.45.56
        auth_plugin="mysql_native_password",
    )

    mycursor = connection.cursor()

    # sql = "Select COUNT(*) From Products where price > 5000"
    # sql = "Select AVG(price) From Products "
    # sql = "Select SUM(price) From Products "
    # sql = "Select MIN(price) From Products "
    # sql = "Select MAX(price) From Products "
    sql = "Select name,price From Products where price = (SELECT MAX(price) from Products) "

    mycursor.execute(sql)

    result = mycursor.fetchone()

    print(result)


getProductInfo()
