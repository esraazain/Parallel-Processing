import sqlite3
from dataClass import News


command1 = """ CREATE TABLE IF NOT EXISTS firstData(
                author text,
                title text,
                description text,
                url text,
                publishedAt text,
                content text
            );"""
command2 = """ CREATE TABLE IF NOT EXISTS secondData(
                author text,
                title text,
                description text,
                url text,
                publishedAt text,
                content text
            );"""
command3 = """ CREATE TABLE IF NOT EXISTS thirdData(
                author text,
                title text,
                description text,
                url text,
                publishedAt text,
                content text
            );"""
command4 = """ CREATE TABLE IF NOT EXISTS forthData(
                author text,
                title text,
                description text,
                url text,
                publishedAt text,
                content text
            );"""
command5 =  """ CREATE TABLE IF NOT EXISTS fifthData(
                author text,
                title text,
                description text,
                url text,
                publishedAt text,
                content text
            );"""

select_Data1 = "SELECT * FROM firstData;"
select_Data2 = "SELECT * FROM secondData;"
select_Data3 = "SELECT * FROM thirdData;"
select_Data4 = "SELECT * FROM forthData;"
select_Data5 = "SELECT * FROM fifthData;"

add_to_data1 = "INSERT INTO firstData VALUES (?,?,?,?,?,?);"
add_to_data2 = "INSERT INTO secondData VALUES (?,?,?,?,?,?);"
add_to_data3 = "INSERT INTO thirdData VALUES (?,?,?,?,?,?);"
add_to_data4 = "INSERT INTO forthData VALUES (?,?,?,?,?,?);"
add_to_data5 = "INSERT INTO fifthData VALUES (?,?,?,?,?,?);"

clear1 = "DELETE FROM firstData;"
clear2 = "DELETE FROM secondData;"
clear3 = "DELETE FROM thirdData;"
clear4 = "DELETE FROM forthData;"
clear5 = "DELETE FROM fifthData;"


def db_connect():
    return sqlite3.connect('data_file')



def create_tables(conn):
    with conn:
        conn.execute(command1)
        conn.execute(command2)
        conn.execute(command3)
        conn.execute(command4)
        conn.execute(command5)





def insert_to_data1(conn,obj):
    with conn:
        conn.execute(add_to_data1,(obj.author,obj.title,obj.description,obj.url,obj.publishedAt,obj.content))

def insert_to_data2(conn,obj):
    with conn:
        conn.execute(add_to_data2,(obj.author,obj.title,obj.description,obj.url,obj.publishedAt,obj.content))    

def insert_to_data3(conn,obj):
    with conn:
        conn.execute(add_to_data3,(obj.author,obj.title,obj.description,obj.url,obj.publishedAt,obj.content))

def insert_to_data4(conn,obj):
    with conn:
        conn.execute(add_to_data4,(obj.author,obj.title,obj.description,obj.url,obj.publishedAt,obj.content))

def insert_to_data5(conn,obj):
    with conn:
        conn.execute(add_to_data5,(obj.author,obj.title,obj.description,obj.url,obj.publishedAt,obj.content))



def select_All_from_Data1(conn):
    with conn:
        return conn.execute(select_Data1).fetchall()

def select_All_from_Data2(conn):
    with conn:
        return conn.execute(select_Data2).fetchall()

def select_All_from_Data3(conn):
    with conn:
        return conn.execute(select_Data3).fetchall()

def select_All_from_Data4(conn):
    with conn:
        return conn.execute(select_Data4).fetchall()

def select_All_from_Data5(conn):
    with conn:
        return conn.execute(select_Data5).fetchall()



def clear_dbs(conn):
    with conn:
        conn.execute(clear1)
        conn.execute(clear2)
        conn.execute(clear3)
        conn.execute(clear4)
        conn.execute(clear5)
        
