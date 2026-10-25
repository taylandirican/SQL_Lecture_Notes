import mysql.connector
from mysql_connection import mydb


def getProducts():
    mycursor = mydb.cursor()

    # sql ="SELECT * FROM products"
    # sql ="SELECT * FROM categories"
    # sql = "SELECT Products.name,Products.price,categories.name FROM products inner join categories on categories.id = Products.categoryid WHERE categories.name='Telefon'"
    # sql = "SELECT Products.name,Products.price,categories.name FROM products inner join categories on categories.id = Products.categoryid WHERE products.name LIKE '%Iphone%'"
    sql = "SELECT p.name,p.price,c.name FROM products as p inner join categories as c on c.id = p.categoryid WHERE p.name LIKE '%Iphone%'"

    mycursor.execute(sql)

    result = mycursor.fetchall()
    for p in result:
        print(p)


getProducts()
