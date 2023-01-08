#imports
import getpass
import mysql.connector as m #importing MySQL connector to comunicate with MySQL server
from mysql.connector import Error
import hashlib
from datetime import datetime
import setup


cnx=setup.cnx
#global variabels and objects
cursor = cnx.cursor() #creating a cursor object
def userlogin():
    username=input("Username: ")
    password=getpass.getpass()
    checkpass="SELECT passwrod from users where username=\""+username+"\""
    #print(checkpass) #debuging
    cursor.execute(checkpass)
    fet=cursor.fetchall()
    #print("hello output",fet[0][0]) #debuging
    password_in_db=fet[0][0]
    hasher=hashlib.sha256(password.encode())
    password=hasher.hexdigest()
    #print(password)
    if password_in_db==password:
        cursor.execute("SELECT USERTYPE from users where username=\""+username+"\"")
        ts=str(datetime.now())
        update="update users set last_login="+"\""+ts+"\" where username=\""+username+"\""
        d=cursor.fetchall()[0][0]
        cursor.execute(update)
        cnx.commit()
        return(d)
        
    elif password_in_db!=password:
        print("wrong password  ")
        userlogin()
        
def new_user():
    username=input("enter username")
    cursor.execute("select count(*) from users where username=\""+username+"\"")
    check=cursor.fetchall()[0][0]
    if check>=1:
        print("username exists")
        new_user()
    password=getpass.getpass()
    re_password=getpass.getpass("confirm password")
    while password!=re_password:
        print("Password incorrect!!")
        password=getpass.getpass("enter password: ")
        re_password=getpass.getpass("confirm password: ")
    usertypeli=["Admin","Genral_Manager","Floor_Manager","Technician","Guest_User"]
    print("enter 1 for Admin \n enter 2 for Genral Manager \n enter 3 for Floor Manager \n enter 4 for Techniation \n enter 5 for Guest_User") #debuging 
    c=int(input("enter choice: "))
    adminpass="admin@123"
    if c==1:
        eadminpass=getpass.getpass("ask an admin to enter admin password:")
        if adminpass==eadminpass:
            usertype=usertypeli[c-1]
            hashed_pass=hasher=hashlib.sha256(password.encode())
            password=hasher.hexdigest()
            ts=str(datetime.now())
            cursor.execute("insert into users values\n(\""+username+"\",\""+password+"\",\""+ts+"\",\""+ts+"\",\""+usertype+"\");")
            cnx.commit()
        else:
            print("enter another choice")
            print("enter 1 for Admin() \n enter 2 for Genral Manager \n enter 3 for Floor Manager \n enter 4 for Techniation \n enter 5 for Guest_User") #debuging 
            c=int(input("enter choice"))
            usertype=usertypeli[c-1]
            hashed_pass=hasher=hashlib.sha256(password.encode())
            password=hasher.hexdigest()
            ts=str(datetime.now())
            cursor.execute("insert into users values\n(\""+username+"\",\""+password+"\",\""+ts+"\",\""+ts+"\",\""+usertype+"\");")
            #print("insert into users values\n(\""+username+"\",\""+password+"\",\""+ts+"\",\""+ts+"\",\""+usertype+"\");") #debuging
            cnx.commit()
    else:
        usertype=usertypeli[c-1]
        hashed_pass=hasher=hashlib.sha256(password.encode())
        password=hasher.hexdigest()
        ts=str(datetime.now())
        cursor.execute("insert into users values\n(\""+username+"\",\""+password+"\",\""+ts+"\",\""+ts+"\",\""+usertype+"\");")
        #print("insert into users values\n(\""+username+"\",\""+password+"\",\""+ts+"\",\""+ts+"\",\""+usertype+"\");") #debuging
        cnx.commit()