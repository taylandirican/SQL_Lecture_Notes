import mysql.connector


def updateProduct(id, name, price):
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="er23Taylan/",
        database="node-app",  # 192.23.45.56
        auth_plugin="mysql_native_password",
    )
    mycursor = mydb.cursor()

    sql = "UPDATE products SET name = %s, price = %s WHERE id = %s"
    value = (name, price, id)
    mycursor.execute(sql, value)

    try:
        mydb.commit()
        print(mycursor.rowcount, "record(s) updated")
    except mysql.connector.Error as err:
        print("Error: {}".format(err))
    finally:
        mydb.close()
        print("Database connection closed.")


updateProduct(6, "Iphone_17", 150000)
