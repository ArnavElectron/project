#imports
import pandas as pd #importing pandas library 
import numpy as np #importing numpy library
import matplotlib.pyplot as pl #importing matplotlib
import mysql.connector as m #importing MySQL connector to comunicate with MySQL server
from mysql.connector import Error


#database connection
cnx = m.connect(user='root', password='helloworld',host='127.0.0.1',database='inventory_test_db')
cnx1 = m.connect(user='root', password='helloworld',host='127.0.0.1',database='users')


#global variabels and objects
cursor = cnx.cursor() #creating a cursor object
list_data_types=["varchar(20)","varchar(10)","date","int","doubel(8,2)","timestamp","char(2)","char(5)","char(10)","decimal()"] 
list_constraints=["Primary key","Foriegn key","unique","NOT NULL"]


#functions
def usertype():
    user_Id=input("enter user id: ")
    password=input("enter password: ")


def create_tabel():
    tabelname=input("enter tabel name")
    n=int(input("enter nuber of collumns (NOTE:new collomns can be added later using alter_tabel)"))
    ct="create table "+tabelname +"(\n"
    for i in range(0,n):
        print("when using diffrent datatype/constraint make sure datatype or constraint is present in mySQL and that its syntax is the right one ")
        #collomn name
        col_name=input("enter column name")
        ct=ct+col_name
        #datatype 
        print(" enter 1 to set datatype as varchar(20) \n enter 2 to set datatype as varchar(10) \n enter 3 to set datatype as date \n enter 4 to set datatype as int \n enter 5 to set data type as doubel(8,2) \n enter 6 to set datatype as timestamp \n enter 7 to set datatype as char(2) \n enter 8 to set datatype as char(5) \n enter 9 to set datatype as char(10) \n enter 10 to set datatype as decimal() \n enter 11 to input a diffrent datatype \n enter 12 to set a diffrent size for datatypes listed above ")
        col_dtype_choice=int(input('enter choice'))
        if col_dtype_choice in range(1,11):
            datatype=list_data_types[col_dtype_choice-1]
            ct=ct+" "+datatype
        elif col_dtype_choice == 11:
            datatype=input("enter datatype")
            ct=ct+" "+datatype
        elif col_dtype_choice== 12:
            ch1=int(input("enter datatype to modify size"))
            si=input("enter size")
            flag1=list_data_types[ch1-1]  
            print(si,"\n",flag1)
            print(type(flag1),"\n",type(si))
            flag2=flag1.split("(")[0]
            print(flag2)
            datatype=flag2+"("+si+")"
            ct=ct+" "+datatype
        print("\n\n ",ct,"\n\n")
        #collmn constraint
        print("enter 1 to set constraint as primary key \n enter 2 to set constraint as foreign key \n enter 3 to set constraint as unique \n enter 4 to set constraint as NOT NULL \n eneter 5 to set consraint as default \n enter 6 to use a diffrent constraint")
        col_constraint_choice=int(input("enter choice"))
        if col_constraint_choice in range(1,6):
           
            if col_constraint_choice == 2:
                reftabel=input("enter refrence tabel name : ")
                refcol=input("enter refrence collumn name : ")
                constraint_type="Foreign key REFRENCES "+reftabel+"("+refcol+")"
                print(constraint_type)
            
            else:
                constraint_type=list_constraints[col_constraint_choice-1]
                ct=ct+" "+constraint_type+",\n"
    ct=ct+" \n);"
    print(ct)
    cursor.execute(ct)
#main loop
create_tabel()