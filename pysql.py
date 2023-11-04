import mysql.connector
from mysql.connector import Error
from tabulate import tabulate

print("\nHellow User !!")

try:
    connection = mysql.connector.connect(host='localhost',database='dbms',user='root', password='Root@123')
    if connection.is_connected():
        db_Info = connection.get_server_info()
        print("\nYou're Connected to MySQL Server version ", db_Info)
        cursor = connection.cursor()
        cursor.execute("select database();")
        record = cursor.fetchone()
        print("You're Connected to Database: ", record)

        def insert():
            print("We are inserting Data...\n")
            rn = int(input("Enter Roll No : "))
            nam = input("Enter Name : ")
            mark = int(input("Enter Marks : "))   
            sql = "INSERT INTO info (roll_no,name,marks) VALUES (%s,%s, %s)"
            val = (rn,nam,mark)
            cursor.execute(sql, val)
            connection.commit()
            print(cursor.rowcount, "record inserted.")
            

        def display():
            print("We are displaying Data...\n")
            cursor.execute("SELECT * FROM info order by roll_no")
            myresult = cursor.fetchall()
            print(tabulate(myresult, headers=["RN", "Name","Marks"]))

        def delete():
            print("We are deleting Data...\n")
            rn = int(input("Enter Roll No to Delete : "))
            sql = "DELETE FROM info WHERE roll_no = %s"
            val = (rn,)
            cursor.execute(sql,val)
            connection.commit()
            print(cursor.rowcount, "record(s) deleted")

        def update():
            print("We are updating Data...\n")
            rn = int(input("Enter Roll No to Upadte : "))
            rn_new = int(input("Enter New Roll No : "))
            name_new = input("Enter New Name : ")
            marks_new = int(input("Enter New Marks : "))
            sql = "UPDATE info SET roll_no = %s, name = %s, marks = %s WHERE roll_no = %s"
            val = (rn_new,name_new,marks_new,rn)
            cursor.execute(sql,val)
            connection.commit()
            print(cursor.rowcount, "record(s) affected")

        while True:
            print('''
    
    ****** MENU ******
    *    1] Insert   *
    *    2] Display  *
    *    3] Update   *
    *    4] Delete   *
    *    5] Exit     *
    ******************
                ''')
            
            ch = int(input("Enter your choice :- "))
            print()
            if (ch==1):
                insert()

            elif (ch==2):
                display()

            elif (ch==3):
                update()

            elif (ch==4):
                delete()

            elif (ch==5):
                print("Program Exited Successfully!!\n")
                break
            else:
                print("Invalid Selection.. Please Try Again !!\n")

except Error as e:
    print("Error while connecting to MySQL !!\n", e)

finally:
    if connection.is_connected():
        cursor.close()
        connection.close()
        print("MySQL connection is closed Successfully !!\n")