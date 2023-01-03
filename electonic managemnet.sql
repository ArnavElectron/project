CREATE DATABASE Electronincs_list_componets;
CREATE TABLE Inventory(
PartNo VARCHAR(20) UNIQUE,
Model_no VARCHAR(100) PRIMARY KEY,
Common_Name VARCHAR(100) NOT NULL,
Quantity INT,
datasheet_link LONGTEXT,
max_voltage VARCHAR(10),
price_each DOUBLE(10,2),
stock_price DOUBLE(10,2)
);

INSERT INTO Inventor values(
    
)

create table main_table
    PartNO VARCHAR(20) UNIQUE,
    Model VARCHAR(100) PRIMARY KEY,
    Common_Name VARCHAR(500),
    Quantity INT,

create table Cart
    PartNO VARCHAR(20) UNIQUE,
    Model VARCHAR(100) PRIMARY KEY,
    Quantity INT,
    

