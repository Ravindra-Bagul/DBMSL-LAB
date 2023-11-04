import mysql.connector
from mysql.connector import Error
from tabulate import tabulate

try:
    connection = mysql.connector.connect(host='localhost',database='dbms',user='root', password='Root@123')
    if connection.is_connected():
        db_Info = connection.get_server_info()
        print("Connected to MySQL Server version ", db_Info)
        cursor = connection.cursor()

        def insert(name, age, city):
            cursor = connection.cursor()
            sql = "insert into users (name,age,city) values (%s,%s,%s)"
            user = (name, age, city)
            cursor.execute(sql, user)
            connection.commit()
            print("Data Insert Success")


        def update(name, age, city,id):
            cursor = connection.cursor()
            sql = "update users set name=%s,age=%s,city=%s where id=%s"
            user = (name, age, city,id)
            cursor.execute(sql, user)
            connection.commit()
            print("Data Update Success")



        def select():
            cursor = connection.cursor()
            sql = "SELECT ID,NAME,AGE,CITY from users"
            cursor.execute(sql)
            # cursorult=cursor.fetchone()
            # cursorult=cursor.fetchmany(2)
            cursorult = cursor.fetchall()
            print(tabulate(cursorult, headers=["ID", "NAME", "AGE", "CITY"]))


        def delete(id):
            cursor = connection.cursor()
            sql = "delete from users where id=%s"
            user = (id,)
            cursor.execute(sql, user)
            connection.commit()
            print("Data Delete Success")



        while True:
            print("1.Insert Data")
            print("2.Update Data")
            print("3.Select Data")
            print("4.Delete Data")
            print("5.Exit")
            choice = int(input("Enter Your Choice : "))
            
            if choice == 1:
                name = input("Enter Name : ")
                age = input("Enter Age : ")
                city = input("Enter City : ")
                insert(name, age, city)
            elif choice == 2:
                id = input("Enter The Id : ")
                name = input("Enter Name : ")
                age = input("Enter Age : ")
                city = input("Enter City : ")
                update(name, age, city,id)
            elif choice == 3:
                select()
            elif choice == 4:
                id = input("Enter The Id to Delete : ")
                delete(id)
            elif choice == 5:
                quit()
            else:
                print("Invalid Selection . Please Try Again !")

except Error as e:
    print("Error while connecting to MySQL", e)

finally:
    if connection.is_connected():
        cursor.close()
        connection.close()
        print("MySQL connection is closed")