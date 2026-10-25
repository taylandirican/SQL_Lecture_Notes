import mysql.connector
from connection import mydb
from datetime import datetime


class Student:
    connection = mydb
    mycursor = connection.cursor()

    def __init__(self, studentnumber, name, surname, birthday, gender):
        self.studentnumber = studentnumber
        self.name = name
        self.surname = surname
        self.birthday = birthday
        self.gender = gender

    def saveStudent(self):
        sql = "INSERT INTO students (studentnumber, name, surname, birthday, gender) VALUES (%s, %s, %s, %s, %s)"
        values = (
            self.studentnumber,
            self.name,
            self.surname,
            self.birthday,
            self.gender,
        )
        Student.mycursor.execute(sql, values)
        try:
            mydb.commit()
        except mysql.connector.Error as err:
            print("Error: {}".format(err))
        finally:
            print(f"{Student.mycursor.rowcount} adet kayıt eklendi.")
            print(f"son eklenen ürünün id: {Student.mycursor.lastrowid}")
            Student.connection.close()

    @staticmethod
    def saveStudents(students):
        sql = "INSERT INTO students (studentnumber, name, surname, birthday, gender) VALUES (%s, %s, %s, %s, %s)"
        values = students
        Student.mycursor.executemany(sql, values)
        try:
            mydb.commit()
        except mysql.connector.Error as err:
            print("Error: {}".format(err))
        finally:
            print(f"{Student.mycursor.rowcount} adet kayıt eklendi.")
            print(f"son eklenen ürünün id: {Student.mycursor.lastrowid}")
            Student.connection.close()


Taylan = Student("2799138", "Taylan", "Dirican", 2008, "Male")
Taylan.saveStudent()


# mycursor.executemany(sql, liste)
# try:
#     mydb.commit()
# except mysql.connector.Error as err:
#     print("Error: {}".format(err))
# finally:
#     print(f"{mycursor.rowcount} adet kayıt eklendi.")
#     print(f"son eklenen ürünün id: {mycursor.lastrowid}")
#     mydb.close()
