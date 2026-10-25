import mysql.connector


def insertProduct(list):
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="er23Taylan/",
        database="node-app",
        auth_plugin="mysql_native_password",
    )
    cursor = connection.cursor()

    sql = "INSERT INTO products(name,price,imageUrl,description) VALUES (%s,%s,%s,%s)"
    values = list

    cursor.executemany(sql, values)

    try:
        connection.commit()
        print(f"{cursor.rowcount} adet kayıt eklendi.")
        print(f"son eklenen ürünün id: {cursor.lastrowid}")
    except mysql.connector.Error as err:
        print("Error: {}".format(err))
    finally:
        connection.close()
        print("Database bağlantısı kapandı")


list = []
while True:
    name = input("Ürün adı: ")
    price = float(input("Ürün fiyatı: "))
    imageUrl = input("Ürün resmi URL: ")
    description = input("Ürün açıklaması: ")

    list.append((name, price, imageUrl, description))

    result = input("Ürün eklemek istiyor musunuz? (e/h): ")
    if result.lower() == "h":
        print("Kyıtlarınız veritabanına ekleniyor...")
        print(list)
        insertProduct(list)
        break
# insertProduct(name, price, imageUrl, description)
