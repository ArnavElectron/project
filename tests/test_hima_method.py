# Querying the database and then making that an object for manipulation
# Updating database once query is done
# Extracting specific data.
# Most borrowed book etc.

import pandas as pd
import pyodbc 

conn = pyodbc.connect('Driver={SQL Server};'
        'Server=RON\SQLEXPRESS;'
        'Database=test_database;'
        'Trusted_Connection=yes;')

def select(cursor,display_fields,tname,conditon,order_by=None,desc=None,print=1):
    if(display_fields[0] == '*'):
        fields = "*"
    else:
        fields = ",".join(display_fields)
    query_str = f'SELECT {fields} FROM {tname} WHERE {conditon}'
    if(desc == True):
        query_str += f'ORDER BY {order_by} DESC;'
    elif(desc == False):
        query_str += f'ORDER BY {order_by} ASC;'
    else:
        query_str += ';'
    out_df = pd.read_sql_query(query_str,cursor)
    if(print):
        print(out_df)
    else:
        return out_df


def update(cursor,t_name,updation_fields,new_values,condition):
    for i in range(len(updation_fields)):
        query_str = f'UPDATE {t_name} SET {updation_fields[i]} = {new_values[i]} WHERE {condition}'
        cursor.execute(query_str)
        print("Updated Record",select(cursor,['*'],t_name,condition),sep="\n")


def insert(cursor,t_name,values,record_df):
    pass