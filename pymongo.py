import pymongo
from pymongo import MongoClient

try:
    client=MongoClient('localhost',27017)
    print("Connected Successfully")

    mydatabase= client.B4
    mycollection=mydatabase.users

    def insert(id,name,age,city):
        records={'id':id,'name':name,'age':age,'city':city}
        result=mycollection.insert_one(records)
        print("Data is Inserted")

    def select():
        cursor=mycollection.find()
        for record in cursor:
            print(record)

    def update(id,name,age,city):
        #result=mycollection.update_many({'id':id},{"$set":{{'name':name},{'age':age},{'city':city}}})
        myquery = { "id": id }
        newvalues = { "$set": { 'name':name,'age':age,'city':city } } 
        result = mycollection.update_many(myquery, newvalues)
        print(result.matched_count,"documents updated")
        print("The Record is updated")

    def delete(id):
        myquery={'id':id}
        result=mycollection.delete_many(myquery)
        print(result.deleted_count,"documents deleted")
        print("Data Deleted")
            
    while True:
        print("\n*********MENU*********")
        print("  1.Insert a Record")
        print("  2.Display Records")
        print("  3.Update a Record")
        print("  4.Delete a Record")
        print("  5.Exit")
        print("**********************")
            
        ch=int(input("\nEnter your choice:"))
        print(" ")

        if(ch==1):
            id=int(input("Enter the Roll No:"))
            name=input("Enter the Name:")
            age=int(input("Enter the Age:"))
            city=input("Enter the City:")
            insert(id,name,age,city)

        elif(ch==2):
            select()

        elif(ch==3):
            id=int(input("Enter the Roll No:"))
            name=input("Enter the Name:")
            age=int(input("Enter the Age:"))
            city=input("Enter the City:")
            update(id,name,age,city)

        elif(ch==4):
            id=int(input("Enter the Roll No:"))
            delete(id)

        elif(ch==5):
            print("Program Exitted Successfully")
            exit()

        else:
            print("Enter the valid choice")
            
except :
    print("Could not connect to MongoDB")