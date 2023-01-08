'''this is the '''



#-----------------------------------------------------------+
x="helloworld"#enter sql password within quotes here please |
#-----------------------------------------------------------+














import mysql.connector as m #importing MySQL connector to comunicate with MySQL server
from mysql.connector import Error


cnx=m.connect(user='root', password=x,host='localhost')
cursor=cnx.cursor()



cursor.execute("create database inventory_management_system ")
inventory='''CREATE TABLE Inventory(
PartNo VARCHAR(20) UNIQUE,
Model_no VARCHAR(100) PRIMARY KEY,
Common_Name VARCHAR(100) NOT NULL,
Quantity INT,
datasheet_link LONGTEXT,
max_voltage VARCHAR(10),
price_each DOUBLE(10,2),
stock_price DOUBLE(10,2)
);'''
cursor.execute(inventory)

users='''create table users(
username varchar(500) PRIMARY KEY,
password varchar(500),
id_create_date varchar(100),
last_login varchar(100),
usertpye varchar(100)
);'''
cursor.execute(users)

insert="""insert into inventory values
("LED001","5MM LED WHITE","LED",500,"http://www1.futureelectronics.com/doc/EVERLIGHT%C2%A0/334-15__T1C1-4WYA.pdf","3V",1.5,750),
("LED002","5MM LED GREEN","LED",500,"http://www1.futureelectronics.com/doc/EVERLIGHT%C2%A0/334","3V",1.5,750),
("LED003","5MM LED RED","LED",500,"http://www1.futureelectronics.com/doc/EVERLIGHT%C2%A0/334","3V",1.5,750),
("LED004","5MM LED BLUE","LED",500,"http://www1.futureelectronics.com/doc/EVERLIGHT%C2%A0/334","3V",1.5,750),
("LED005","SMD LED WHITE","LED",300,"https://www.mouser.com/datasheet/2/239/LTST-S326KGKFKT-1143909.pdf","2.5V",5,1500),
("LED006","SMD LED BLUE","LED",300,"https://www.mouser.com/datasheet/2/239/LTST-S326KGKFKT-1143909.pdf","2.5V",5,1500),
("LED007","SMD LED RED","LED","300","https://www.mouser.com/datasheet/2/239/LTST-S326KGKFKT-1143909.pdf","2.5V",5,1500),
("LED008","SMD LED GREEN","LED","300","https://www.mouser.com/datasheet/2/239/LTST-S326KGKFKT-1143909.pdf","2.5V",5,1500),
("LED009","SMD LED WS8212B","neopixel",1000,"https://cdn-shop.adafruit.com/datasheets/WS2812B.pdf","3V",5,5000),
("LED010","RGB LED","LED",1000,"https://www.mouser.com/datasheet/2/239/LTST-S326KGKFKT-1143909.pdf","3V",5,5000),
("Q001","IRF540N","TRANSITOR/MOSFET",200,"https://pdf1.alldatasheet.com/datasheet-pdf/view/67486/INTERSIL/IRF540N.html","60V",15,3000),
("Q002","2n222A","TRANSITOR/MOSFET",500,"https://pdf1.alldatasheet.com/datasheet-pdf/view/5612/MOTOROLA/2N222.html","20V",5,2500),
("IC001","NE555","INTEGRATED CIRCUIT",500,"https://pdf1.alldatasheet.com/datasheet-pdf/view/17972/PHILIPS/NE555.html","30v",10,5000),
("IC002","Attiny85","INTEGRATED CIRCUIT",500,"https://pdf1.alldatasheet.com/datasheet-pdf/view/174761/ATMEL/ATTINY85.html","5v",60,30000),
("IC003","ATmega328","INTEGRATED CIRCUIT",250,"https://pdf1.alldatasheet.com/datasheet-pdf/view/392243/ATMEL/ATMEGA328.html","5v",150,37500),
("IC004","LM393","INTEGRATED CIRCUIT",300,"https://pdf1.alldatasheet.com/datasheet-pdf/view/3068/MOTOROLA/LM393.html","36v",20,6000),
("IC005","LM555","INTEGRATED CIRCUIT",300,"https://pdf1.alldatasheet.com/datasheet-pdf/view/53587/FAIRCHILD/LM555.html","16v",20,6000),
("IC006","LM317","INTEGRATED CIRCUIT",500,"https://pdf1.alldatasheet.com/datasheet-pdf/view/1147586/ARTSCHIP/LM317.html","33v",5,2500),
("IC007","L293D","INTEGRATED CIRCUIT",300,"https://pdf1.alldatasheet.com/datasheet-pdf/view/3065/MOTOROLA/LM239D.html","30v",20,6000),
("IC008","IC7733","INTEGRATED CIRCUIT",300,NULL,NULL,10,3000),
("IC009","RB156","INTEGRATED CIRCUIT",250,"https://pdf1.alldatasheet.com/datasheet-pdf/view/34064/WTE/RB156.html",NULL,NULL,250),
("IC010","LM3914","INTEGRATED CIRCUIT",250,"https://pdf1.alldatasheet.com/datasheet-pdf/view/524103/TI1/LM3914N-1.html","22v",10,2500),
("R001","100ohm","RESISTOR",1000,"https://www.mouser.in/datasheet/2/418/3/NG_CS_1309350_PASSIVE_COMPONENT_0807-1235562.pdf","20V",2,2000),
("R002","220ohm","RESISTOR",1000,"https://www.mouser.in/datasheet/2/418/3/NG_CS_1309350_PASSIVE_COMPONENT_0807-1235562.pdf","20V",2,2000),
("R003","300ohm","RESISTOR",1000,"https://www.mouser.in/datasheet/2/418/3/NG_CS_1309350_PASSIVE_COMPONENT_0807-1235562.pdf","20V",2,2000),
("R004","330ohm","RESISTOR",1000,"https://www.mouser.in/datasheet/2/418/3/NG_CS_1309350_PASSIVE_COMPONENT_0807-1235562.pdf","20V",2,2000),
("R005","500ohm","RESISTOR",1000,"https://www.mouser.in/datasheet/2/418/3/NG_CS_1309350_PASSIVE_COMPONENT_0807-1235562.pdf","20V",2,2000),
("R006","1000ohm","RESISTOR",1000,"https://www.mouser.in/datasheet/2/418/3/NG_CS_1309350_PASSIVE_COMPONENT_0807-1235562.pdf","20V",2,2000),
("R007","2200ohm","RESISTOR",1000,"https://www.mouser.in/datasheet/2/418/3/NG_CS_1309350_PASSIVE_COMPONENT_0807-1235562.pdf","20V",2,2000),
("R008","5000ohm","RESISTOR",1000,"https://www.mouser.in/datasheet/2/418/3/NG_CS_1309350_PASSIVE_COMPONENT_0807-1235562.pdf","20V",2,2000),
("R009","4700ohm","RESISTOR",1000,"https://www.mouser.in/datasheet/2/418/3/NG_CS_1309350_PASSIVE_COMPONENT_0807-1235562.pdf","20V",2,2000),
("R010","10000ohm","RESISTOR",1000,"https://www.mouser.in/datasheet/2/418/3/NG_CS_1309350_PASSIVE_COMPONENT_0807-1235562.pdf","20V",2,2000),
("R011","15000ohm","RESISTOR",1000,"https://www.mouser.in/datasheet/2/418/3/NG_CS_1309350_PASSIVE_COMPONENT_0807-1235562.pdf","20V",2,2000),
("R012","20000ohm","RESISTOR",1000,"https://www.mouser.in/datasheet/2/418/3/NG_CS_1309350_PASSIVE_COMPONENT_0807-1235562.pdf","20V",2,2000),
("R013","22000ohm","RESISTOR",1000,"https://www.mouser.in/datasheet/2/418/3/NG_CS_1309350_PASSIVE_COMPONENT_0807-1235562.pdf","20V",2,2000),
("R014","1M0hm","RESISTOR",1000,"https://www.mouser.in/datasheet/2/418/3/NG_CS_1309350_PASSIVE_COMPONENT_0807-1235562.pdf","20V",2,2000),
("R015","100000ohm","RESISTOR",1000,"https://www.mouser.in/datasheet/2/418/3/NG_CS_1309350_PASSIVE_COMPONENT_0807-1235562.pdf","20V",2,2000),
("R016","500000ohm","RESISTOR",1000,"https://www.mouser.in/datasheet/2/418/3/NG_CS_1309350_PASSIVE_COMPONENT_0807-1235562.pdf","20V",2,2000),
("R017","50ohm","RESISTOR",1000,"https://www.mouser.in/datasheet/2/418/3/NG_CS_1309350_PASSIVE_COMPONENT_0807-1235562.pdf","20V",2,2000),
("R018","470ohm","RESISTOR",1000,"https://www.mouser.in/datasheet/2/418/3/NG_CS_1309350_PASSIVE_COMPONENT_0807-1235562.pdf","20V",2,2000),
("R019","1ohm 1W","RESISTOR",100,"https://www.mouser.in/datasheet/2/418/3/NG_CS_1309350_PASSIVE_COMPONENT_0807-1235562.pdf","100V",10,1000),
("R020","2ohm 5W","RESISTOR",100,"https://www.mouser.in/datasheet/2/418/3/NG_CS_1309350_PASSIVE_COMPONENT_0807-1235562.pdf","100V",10,1000),
("D001","1N4007","DIODE",700,"https://pdf1.alldatasheet.com/datasheet-pdf/view/14624/PANJIT/1N4007.html","700v",5,300),
("D002","1n4148","DIODE",500,"https://pdf1.alldatasheet.com/datasheet-pdf/view/190208/WTE/1N4148.html","100v",5,2500);"""

cursor.execute(insert)

usersdata="""insert into users values 
("admin","8c6976e5b5410415bde908bd4dee15dfb167a9c873fc4bb8a81f6f2ab448a918","2023-01-05 22:56:43.429940","2023-01-05 22:56:43.429940","Admin")"""

cursor.execute(usersdata)

cnx.commit()