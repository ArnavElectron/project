import pandas as pd
import numpy as np
import matplotlib.pyplot as pl
import getpass
import mysql.connector as m #importing MySQL connector to comunicate with MySQL server
from mysql.connector import Error
import hashlib
from datetime import datetime
import setup


cnx=setup.cnx
#global variabels and objects
cursor = cnx.cursor()
list_data_types=["varchar(20)","varchar(10)","date","int","doubel(8,2)","timestamp","char(2)","char(5)","char(10)","decimal()"] 
list_constraints=["Primary key","Foriegn key","unique","NOT NULL"]
def update_stock_price():
    cursor.execute("select count(*) from inventory")
    count=cursor.fetchall()[0][0]
    cursor.execute("select quantity*price_each from inventory")
    vals=cursor.fetchall()
    cursor.execute("select quantity from inventory")
    qty=cursor.fetchall()
    for i in range(0,count):
        cursor.execute("update inventory set stock_price="+str(vals[i][0])+"where quantity="+str(qty[i][0]))

def show_inventory_tabel():
    query="select * from inventory"
    result_dataFrame = pd.read_sql(query,cnx)
    print(result_dataFrame)

def show_user_table():
    query="select username,id_create_date,last_login from users"
    result_dataFrame = pd.read_sql(query,cnx)
    print(result_dataFrame)

def show_table():
    cursor.execute("show tables")
    ta=cursor.fetchall()
    for i in ta:
        print(i[0])
    tabname=input("enter table name")
    query="select * from "+tabname
    result_dataFrame = pd.read_sql(query,cnx)
    print(result_dataFrame)


def add_inventory():
    numitems=int(input("enter number of items to add: "))
    query=("insert into inventory(PartNo,Model_no,Common_name,Quantity,datasheet_link,max_voltage,price_each,stock_price) values(%s, %s, %s, %s,%s,%s,%s,%s)")
    li=[]
    for i in range(0,numitems):
        partno=input("enter part no: ")
        model_no=input("enter model no: ")
        common_name=input("enter name: ")
        qty=int(input("enter quantity"))
        link=input("enter datasheet link")
        voltage=input("enter voltage: ")
        price_e=eval(input("enter price per part:"))
        li.append(partno)
        li.append(model_no)
        li.append(common_name)
        li.append(qty)
        li.append(link)
        li.append(voltage)
        li.append(price_e)
        stock=qty*price_e
        li.append(stock)
        # print(tuple(li))
        # print(query)
        cursor.execute(query,tuple(li))
        cnx.commit()
def update_qty():
    partno=input("enter part number: ")
    cursor.execute("select Quantity from inventory where partno=\""+partno+"\"")
    qty=cursor.fetchall()[0][0]
    print(qty)
    print("enter 1 to subtract to the current quantity \n enter 2 to add the current quantity \n enter 3 to specify a new quantity")
    choice=int(input("enter choice: "))
    if choice==1:
        qtyflag=int(input("enter number of iteams to subtract: "))
        qty=qty-qtyflag
    elif choice==2:
        qtyflag=int(input("enter number of iteams to add: "))
        qty=qty+qtyflag
    elif choice==3:
        qtyflag=int(input("enter number of iteams to subtract: "))
        qty=qtyflag
    cursor.execute("update inventory set quantity=\""+str(qty)+"\"where partno=\""+partno+"\"")
    update_stock_price()
    cnx.commit()
def graph_parts_quantity_price():
    cursor.execute("select count(*) from inventory")
    count=cursor.fetchall()[0][0]
    cursor.execute("select partno from inventory")
    idxv=cursor.fetchall()
    idx=[]
    colors=["green","black","red"]
    for i in range(0,count):
        idx.append(idxv[i][0])
    #print("cols",colors) debuging
    cnx.commit()
    query="select partno,quantity,price_each,stock_price from inventory"
    result_dataFrame = pd.read_sql(query,cnx)
    result_dataFrame.index=idx
    result_dataFrame.plot(kind="hist",color=colors)
    pl.show()
    #print(result_dataFrame) debuging
def show_datasheet():
    inp=input("enter part number/ model number :")
    cursor.execute("select datasheet_link from inventory where partno=\'"+inp+"\' OR model_no=\""+inp+"\"")
    print(cursor.fetchall()[0][0])
