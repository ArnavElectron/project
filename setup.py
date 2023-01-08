'''this is the setup file to establish connection between sql server and python application'''




#-----------------------------------------------------------+
x="helloworld"#enter sql password within quotes here please |
#-----------------------------------------------------------+












import mysql.connector as m #importing MySQL connector to comunicate with MySQL server
from mysql.connector import Error

#database connection
cnx = m.connect(user='root', password=x,host='localhost',database='inventory_management_system')



#global variabels and objects
cursor = cnx.cursor() #creating a cursor object

