import mysql.connector
from mysql_connection import mydb


def deleteProduct(id):
    cursor = mydb.cursor()
    sql = "DELETE FROM PRODUCTS WHERE id = %s"
    value = (id,)  # Liste şeklinde göndermemizin sebebi güvenliği sıklaştırmamız

    cursor.execute(sql, value)

    try:
        mydb.commit()
        print(cursor.rowcount, "record(s) deleted")
    except mysql.connector.Error as err:
        print(f"Error: {err}")
    finally:
        mydb.close()
        print("Database connection closed.")


deleteProduct()
