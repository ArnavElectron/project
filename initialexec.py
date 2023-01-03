'''this is a work in progress '''



#-----------------------------------------------
x=#reomve comment and enter sql password here pls
#-----------------------------------------------












import mysql.connector as m #importing MySQL connector to comunicate with MySQL server
from mysql.connector import Error

#database connection
cnx = m.connect(user='root', password=x,host='127.0.0.1',database='inventory_test_db')



#global variabels and objects
cursor = cnx.cursor() #creating a cursor object

