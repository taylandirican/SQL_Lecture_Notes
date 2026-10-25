import mysql.connector
from connection import mydb

mycursor = mydb.cursor()

# mycursor.execute("SELECT * FROM students")

# result = mycursor.fetchall()


# mycursor.execute("SELECT studentnumber, name, surname FROM students")

# result = mycursor.fetchall()


# mycursor.execute(
#     "SELECT studentnumber, name, surname FROM students WHERE gender = 'Kadın'"
# )

# result = mycursor.fetchall()


# mycursor.execute(
#     "SELECT studentnumber, name, surname FROM students WHERE birthday = 2008"
# )

# result = mycursor.fetchall()


# mycursor.execute(
#     "SELECT studentnumber, name, surname FROM students WHERE name = 'Taylan' OR birthday =1997"
# )

# result = mycursor.fetchall()

sql = "SELECT studentnumber, name, surname FROM students WHERE name LIKE '%an%' or surname LIKE '%an%'"
mycursor.execute(sql)

result = mycursor.fetchall()
print(result)

mycursor.execute(
    "SELECT name, surname FROM students WHERE GENDER = 'Erkek' or GENDER = 'Male'"
)

result_list = mycursor.fetchall()

i = 0
for result in result_list:
    i += 1
    print(f"{i}. {result[0]} {result[1]}")
print(f"Total male students: {i}")


mycursor.execute("SELECT name FROM students WHERE gender = 'Kadın' ORDER BY name ")

result = mycursor.fetchall()


print(result)
