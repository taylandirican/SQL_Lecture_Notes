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

    # mycursor.execute("SELECT * FROM products Order By name ASC")  # name'e göre artan sırada getirir
    # mycursor.execute(
    #     "SELECT * FROM products Order By id DESC"
    # )  # id'ye göre azalan sırada getirir

    mycursor.execute("SELECT * FROM products Order By name, price")

    try:
        result = mycursor.fetchall()
        for product in result:
            print(product)
    except mysql.connector.Error as err:
        print(f"Error: {err}")
    finally:
        connection.close()
        print("Database bağlantısı kapandı")


getProducts()
