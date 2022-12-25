#imports
import getpass
import mysql.connector as m #importing MySQL connector to comunicate with MySQL server
from mysql.connector import Error
import hashlib
from datetime import datetime

#database connection
cnx = m.connect(user='root', password='helloworld',host='127.0.0.1',database='inventory_test_db')



#global variabels and objects
cursor = cnx.cursor() #creating a cursor object
def userlogin():
    username=input("Username: ")
    password=getpass.getpass()
    checkpass="SELECT passwrod from users where username=\""+username+"\""
    #print(checkpass) #debuging
    cursor.execute(checkpass)
    fet=cursor.fetchall()[0][0]
    #print(fet) #debuging
    password_in_db=fet
    hasher=hashlib.sha256(password.encode())
    password=hasher.hexdigest()
    if password_in_db==password:
        cursor.execute("SELECT USERTYPE from users where username=\""+username+"\"")
        d=cursor.fetchall()[0][0]

        return(d)
    else:
        print("wrong password  ")
        
def new_user():
    username=input("enter username")
    password=getpass.getpass()
    re_password=getpass.getpass("confirm password")
    while password!=re_password:
        print("Password incorrect!!")
        password=getpass.getpass("enter password: ")
        re_password=getpass.getpass("confirm password: ")
    usertypeli=["admin","manager","floor manager","tecnitian","guest_user"]
    #print("enter 1 for admin \n enter 2 for manager \n enter 3 for floor manager \n enter 4 for techniation \n enter 5 for guest_user") #debuging 
    c=int(input("enter choice"))
    usertype=usertypeli[c-1]
    hashed_pass=hasher=hashlib.sha256(password.encode())
    password=hasher.hexdigest()
    ts=str(datetime.now())
    cursor.execute("insert into users values\n(\""+username+"\",\""+password+"\",\""+ts+"\",\""+ts+"\",\""+usertype+"\");")
    #print("insert into users values\n(\""+username+"\",\""+password+"\",\""+ts+"\",\""+ts+"\",\""+usertype+"\");") #debuging
    cnx.commit()

