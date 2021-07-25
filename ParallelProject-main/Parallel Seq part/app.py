import db
from dataClass import News
from reqs import init_api_conn,request_Data_1,request_Data_2,request_Data_3,request_Data_4,request_Data_5

connection = db.db_connect()
db.create_tables(connection)

   
news_api = init_api_conn("c2612454e7474eeaa7ec328a4fc8f71a") #openning connection with api


def fill_table_1_With_Data(data,conn1):
    data_obj = News('','','','','','')
    
    for x in data:
        data_obj.author = x['author']
        data_obj.title = x['title']
        data_obj.description = x['description']
        data_obj.url = x['url']
        data_obj.publishedAt = x['publishedAt']
        data_obj.content = x['content']
        db.insert_to_data1(conn1,data_obj)


def fill_table_1_With_Data(data,conn1):
    data_obj = News('','','','','','')
    
    for x in data:
        data_obj.author = x['author']
        data_obj.title = x['title']
        data_obj.description = x['description']
        data_obj.url = x['url']
        data_obj.publishedAt = x['publishedAt']
        data_obj.content = x['content']
        db.insert_to_data1(conn1,data_obj)

def fill_table_2_With_Data(data,conn1):
    data_obj = News('','','','','','')
    
    for x in data:
        data_obj.author = x['author']
        data_obj.title = x['title']
        data_obj.description = x['description']
        data_obj.url = x['url']
        data_obj.publishedAt = x['publishedAt']
        data_obj.content = x['content']
        db.insert_to_data2(conn1,data_obj)

def fill_table_3_With_Data(data,conn1):
    data_obj = News('','','','','','')
    
    for x in data:
        data_obj.author = x['author']
        data_obj.title = x['title']
        data_obj.description = x['description']
        data_obj.url = x['url']
        data_obj.publishedAt = x['publishedAt']
        data_obj.content = x['content']
        db.insert_to_data3(conn1,data_obj)

def fill_table_4_With_Data(data,conn1):
    data_obj = News('','','','','','')
    
    for x in data:
        data_obj.author = x['author']
        data_obj.title = x['title']
        data_obj.description = x['description']
        data_obj.url = x['url']
        data_obj.publishedAt = x['publishedAt']
        data_obj.content = x['content']
        db.insert_to_data4(conn1,data_obj)

def fill_table_5_With_Data(data,conn1):
    data_obj = News('','','','','','')
    
    for x in data:
        data_obj.author = x['author']
        data_obj.title = x['title']
        data_obj.description = x['description']
        data_obj.url = x['url']
        data_obj.publishedAt = x['publishedAt']
        data_obj.content = x['content']
        db.insert_to_data5(conn1,data_obj)



def print_table_1():
    x = db.select_All_from_Data1(connection)
    for i in x :
        print(i)

def print_table_2():
    z = db.select_All_from_Data2(connection)
    for i in z :
        print(i)
def print_table_3():
    y = db.select_All_from_Data3(connection)
    for i in y:
        print(i)

def print_table_4():
    xy = db.select_All_from_Data4(connection)
    for i in xy :
        print(i)

def print_table_5():
    xz = db.select_All_from_Data5(connection)
    for i in xz :
        print(i)

def pprint(x):
    for i in x:
        print(i)



def test():
    db.create_tables(connection)
    data1 = request_Data_1(news_api)['articles']
    data2 = request_Data_2(news_api)['articles']
    data3 = request_Data_3(news_api)['articles']
    data4 = request_Data_4(news_api)['articles']
    data5 = request_Data_5(news_api)['articles']

    db.clear_dbs(connection)
    fill_table_1_With_Data(data1)
    fill_table_2_With_Data(data2)
    fill_table_3_With_Data(data3)
    fill_table_4_With_Data(data4)
    fill_table_5_With_Data(data5)
    

    print_table_1()
    print('*************')

    print_table_2()
    print('*************')

    print_table_3()
    print('*************')

    print_table_4()
    print('*************')

    print_table_5()
    print('*************')
    

#test()

