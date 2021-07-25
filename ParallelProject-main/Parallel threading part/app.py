import db
from dataClass import News
from reqs import init_api_conn,request_Data_1,request_Data_2,request_Data_3,request_Data_4,request_Data_5

connection = db.db_connect()
db.create_tables(connection)

   
news_api = init_api_conn("c2612454e7474eeaa7ec328a4fc8f71a") #openning connection with api

def fill_table_1_With_Data(data, lock2):
    data_obj1 = News('','','','','','')
    
    lock2.acquire()
    for x in data:
        data_obj1.author = x['author']
        data_obj1.title = x['title']
        data_obj1.description = x['description']
        data_obj1.url = x['url']
        data_obj1.publishedAt = x['publishedAt']
        data_obj1.content = x['content']
        db.insert_to_data1(connection,data_obj1)
    lock2.release()

def fill_table_2_With_Data(data , lock2):
    data_obj2 = News('','','','','','')
    
    lock2.acquire()
    for x in data:
        data_obj2.author = x['author']
        data_obj2.title = x['title']
        data_obj2.description = x['description']
        data_obj2.url = x['url']
        data_obj2.publishedAt = x['publishedAt']
        data_obj2.content = x['content']
        db.insert_to_data2(connection,data_obj2)
    lock2.release()

def fill_table_3_With_Data(data , lock2):
    data_obj3 = News('','','','','','')
    
    lock2.acquire()
    for x in data:
        data_obj3.author = x['author']
        data_obj3.title = x['title']
        data_obj3.description = x['description']
        data_obj3.url = x['url']
        data_obj3.publishedAt = x['publishedAt']
        data_obj3.content = x['content']
        db.insert_to_data3(connection,data_obj3)
    lock2.release()

def fill_table_4_With_Data(data , lock2):
    data_obj4 = News('','','','','','')
    
    lock2.acquire()
    for x in data:
        data_obj4.author = x['author']
        data_obj4.title = x['title']
        data_obj4.description = x['description']
        data_obj4.url = x['url']
        data_obj4.publishedAt = x['publishedAt']
        data_obj4.content = x['content']
        db.insert_to_data4(connection,data_obj4)
    lock2.release()

def fill_table_5_With_Data(data , lock2):
    data_obj5 = News('','','','','','')
    
    lock2.acquire()
    for x in data:
        data_obj5.author = x['author']
        data_obj5.title = x['title']
        data_obj5.description = x['description']
        data_obj5.url = x['url']
        data_obj5.publishedAt = x['publishedAt']
        data_obj5.content = x['content']
        db.insert_to_data5(connection,data_obj5)
    lock2.release()



def print_table_1(lock3):
    lock3.acquire()
    print("11111111111111111111111111111")
    x = db.select_All_from_Data1(connection)
    print(x)
    #for i in x :
        #print(i)
    lock3.release()

def print_table_2(lock3):
    lock3.acquire()
    print("22222222222222222222222222222")
    z = db.select_All_from_Data2(connection)
    print(z)
    #for i in z :
        #print(i)
    lock3.release()
    
def print_table_3(lock3):
    lock3.acquire()
    print("33333333333333333333333333333")
    y = db.select_All_from_Data3(connection)
    print(y)
    #for i in y:
        #print(i)
    lock3.release()

def print_table_4(lock3):
    lock3.acquire()
    print("44444444444444444444444444444")
    xy = db.select_All_from_Data4(connection)
    print(xy)
    #for i in xy :
        #print(i)
    lock3.release()

def print_table_5(lock3):
    lock3.acquire()
    print("55555555555555555555555555555")
    xz = db.select_All_from_Data5(connection)
    print(xz)
    #for i in xz :
        #print(i)
    lock3.release()





def main():
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
    

#main()

