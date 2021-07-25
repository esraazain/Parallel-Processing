import sys
from PyQt5 import QtWidgets, uic

from PyQt5.QtWidgets import QApplication, QWidget,QMainWindow,\
    QPushButton, QVBoxLayout,QLineEdit,QLabel,QMessageBox,QLineEdit,QLabel
import reqs
import db
import app
from threading import Thread
from threading import Lock


connection = db.db_connect()
db.create_tables(connection)
a = QApplication(sys.argv)
KEY='862b21667b294a1d867f620e8fc1dd9b'
d1=d2=d3=d4=d5={}
newsapi= reqs.init_api_conn(KEY)
data_list = []

threads = []
thread_num = 5

lock = Lock()


def get_data1():
    data1 = reqs.request_Data_1(newsapi)['articles']
    data_list.insert(0,data1)
    #lock.acquire()
    #print("This is request 1111111111111111111111")
    #print(data_list[0])
    #lock.release()
    #print('////////////////////')

def get_data2():
    data2 = reqs.request_Data_2(newsapi)['articles']
    data_list.insert(1,data2)
    #lock.acquire()
    #print("This is request 2222222222222222222")
    #print(data_list[1])
    #lock.release()
    #print(len(data_list))
    
def get_data3():
    data3 = reqs.request_Data_3(newsapi)['articles']
    data_list.insert(2,data3)
    #lock.acquire()
    #print("This is request 3333333333333333333333")
    #print(data_list[2])
    #lock.release()
    #print(len(data_list))
    
def get_data4():
    data4 = reqs.request_Data_4(newsapi)['articles']
    data_list.insert(3,data4)
    #lock.acquire()
    #print("This is request 4444444444444444")
    #print(data_list[3])
    #lock.release()
    #print(len(data_list))
    
def get_data5():
    data5 = reqs.request_Data_5(newsapi)['articles']
    data_list.insert(4,data5)
    #lock.acquire()
    #print("This is request 5555555555555555555555")
    #print(data_list[4])
    #lock.release()
    #print(len(data_list))

def sendd():
    
    #newsapi=reqs.init_api_conn(KEY)
    t1 = Thread(target=get_data1)   
    t2 = Thread(target=get_data2)
    t3 = Thread(target=get_data3)
    t4 = Thread(target=get_data4)
    t5 = Thread(target=get_data5)
    
    #threads.append(t1)
    #threads.append(t2)

    t1.start()
    t2.start()
    t3.start()
    t4.start()
    t5.start()
    
    t1.join()
    t2.join()
    t3.join()
    t4.join()
    t5.join()
    
    for x in data_list:
        print("**************************************")
        print(x)
    #print(data_list[0])
    #print('////////////////////')
    #print(data_list[1])
    #print(len(data_list))



def insertt():
    connection = db.db_connect()
    db.create_tables(connection)
    
    lock2 = Lock()
    
    t6 = Thread(target=app.fill_table_1_With_Data , args = (data_list[0], lock2, ))
    t7 = Thread(target=app.fill_table_2_With_Data , args = (data_list[1], lock2, ))
    t8 = Thread(target=app.fill_table_3_With_Data , args = (data_list[2], lock2, ))
    t9 = Thread(target=app.fill_table_4_With_Data , args = (data_list[3], lock2, ))
    t10 = Thread(target=app.fill_table_5_With_Data , args = (data_list[4], lock2, ))
    
    t6.start()
    t7.start()
    t8.start()
    t9.start()
    t10.start()
    #t6 = Thread(target=app.fill_table_1_With_Data , args = (t1, ))
    #app.fill_table_1_With_Data(d1)
    #app.fill_table_2_With_Data(d2)
    #app.fill_table_3_With_Data(d3)
    #app.fill_table_4_With_Data(d4)
    #app.fill_table_5_With_Data(d5)

def gett():
    lock3 = Lock()
    
    t11 = Thread(target = app.print_table_1 , args=(lock3,))
    t12 = Thread(target = app.print_table_2 , args=(lock3,))
    t13 = Thread(target = app.print_table_3 , args=(lock3,))
    t14 = Thread(target = app.print_table_4 , args=(lock3,))
    t15 = Thread(target = app.print_table_5 , args=(lock3,))
    
    t11.start()
    t12.start()
    t13.start()
    t14.start()
    t15.start()
    
    t11.join()
    t12.join()
    t13.join()
    t14.join()
    t15.join()
    
def clearDB():
    db.clear_dbs(connection)


root=QWidget()
root.setStyleSheet('''
   QWidget {
  background-color: #19232D;
  border: 0px solid #32414B;
  padding: 0px;
  color: #F0F0F0;
  selection-background-color: #1464A0;
  selection-color: #F0F0F0;
}

QWidget:disabled {
  background-color: #19232D;
  color: #787878;
  selection-background-color: #14506E;
  selection-color: #787878;
}

QWidget::item:selected {
  background-color: #1464A0;
}

QWidget::item:hover {
  background-color: #148CD2;
  color: #32414B;
}

        ''')

root.setWindowTitle('parallel') #board title
root.setFixedSize(640, 480)

get_b= QPushButton('Send Requestes',root) #adding button
get_b.move(100,50)
get_b.clicked.connect(sendd)

get_from_database_b= QPushButton('Insert into database',root) #adding button
get_from_database_b.move(250,50)
get_from_database_b.clicked.connect(insertt)

insert_into_database_b= QPushButton('Get from database',root) #adding button
insert_into_database_b.move(450,50)
insert_into_database_b.clicked.connect(gett)


cancel_b= QPushButton('clear',root) #adding button
cancel_b.move(450,400)
cancel_b.clicked.connect(clearDB) #Exit root


get_b.setStyleSheet('''
QPushButton {
  background-color: #505F69;
  border: 1px solid #32414B;
  color: #F0F0F0;
  border-radius: 4px;
  padding: 3px;
  outline: none;
  /* Issue #194 - Special case of QPushButton inside dialogs, for better UI */
  min-width: 80px;
}

QPushButton:disabled {
  background-color: #32414B;
  border: 1px solid #32414B;
  color: #787878;
  border-radius: 4px;
  padding: 3px;
}

QPushButton:checked {
  background-color: #32414B;
  border: 1px solid #32414B;
  border-radius: 4px;
  padding: 3px;
  outline: none;
}

QPushButton:checked:disabled {
  background-color: #19232D;
  border: 1px solid #32414B;
  color: #787878;
  border-radius: 4px;
  padding: 3px;
  outline: none;
}

QPushButton:checked:selected {
  background: #1464A0;
  color: #32414B;
}

QPushButton::menu-indicator {
  subcontrol-origin: padding;
  subcontrol-position: bottom right;
  bottom: 4px;
}

QPushButton:pressed {
  background-color: #19232D;
  border: 1px solid #19232D;
}

QPushButton:pressed:hover {
  border: 1px solid #148CD2;
}

QPushButton:hover {
  border: 1px solid #148CD2;
  color: #F0F0F0;
}

QPushButton:selected {
  background: #1464A0;
  color: #32414B;
}

QPushButton:hover {
  border: 1px solid #148CD2;
  color: #F0F0F0;
}

QPushButton:focus {
  border: 1px solid #1464A0;
}

''')

get_from_database_b.setStyleSheet('''
QPushButton {
  background-color: #505F69;
  border: 1px solid #32414B;
  color: #F0F0F0;
  border-radius: 4px;
  padding: 3px;
  outline: none;
  /* Issue #194 - Special case of QPushButton inside dialogs, for better UI */
  min-width: 80px;
}

QPushButton:disabled {
  background-color: #32414B;
  border: 1px solid #32414B;
  color: #787878;
  border-radius: 4px;
  padding: 3px;
}

QPushButton:checked {
  background-color: #32414B;
  border: 1px solid #32414B;
  border-radius: 4px;
  padding: 3px;
  outline: none;
}

QPushButton:checked:disabled {
  background-color: #19232D;
  border: 1px solid #32414B;
  color: #787878;
  border-radius: 4px;
  padding: 3px;
  outline: none;
}

QPushButton:checked:selected {
  background: #1464A0;
  color: #32414B;
}

QPushButton::menu-indicator {
  subcontrol-origin: padding;
  subcontrol-position: bottom right;
  bottom: 4px;
}

QPushButton:pressed {
  background-color: #19232D;
  border: 1px solid #19232D;
}

QPushButton:pressed:hover {
  border: 1px solid #148CD2;
}

QPushButton:hover {
  border: 1px solid #148CD2;
  color: #F0F0F0;
}

QPushButton:selected {
  background: #1464A0;
  color: #32414B;
}

QPushButton:hover {
  border: 1px solid #148CD2;
  color: #F0F0F0;
}

QPushButton:focus {
  border: 1px solid #1464A0;
}

''')

insert_into_database_b.setStyleSheet('''
QPushButton {
  background-color: #505F69;
  border: 1px solid #32414B;
  color: #F0F0F0;
  border-radius: 4px;
  padding: 3px;
  outline: none;
  /* Issue #194 - Special case of QPushButton inside dialogs, for better UI */
  min-width: 80px;
}

QPushButton:disabled {
  background-color: #32414B;
  border: 1px solid #32414B;
  color: #787878;
  border-radius: 4px;
  padding: 3px;
}

QPushButton:checked {
  background-color: #32414B;
  border: 1px solid #32414B;
  border-radius: 4px;
  padding: 3px;
  outline: none;
}

QPushButton:checked:disabled {
  background-color: #19232D;
  border: 1px solid #32414B;
  color: #787878;
  border-radius: 4px;
  padding: 3px;
  outline: none;
}

QPushButton:checked:selected {
  background: #1464A0;
  color: #32414B;
}

QPushButton::menu-indicator {
  subcontrol-origin: padding;
  subcontrol-position: bottom right;
  bottom: 4px;
}

QPushButton:pressed {
  background-color: #19232D;
  border: 1px solid #19232D;
}

QPushButton:pressed:hover {
  border: 1px solid #148CD2;
}

QPushButton:hover {
  border: 1px solid #148CD2;
  color: #F0F0F0;
}

QPushButton:selected {
  background: #1464A0;
  color: #32414B;
}

QPushButton:hover {
  border: 1px solid #148CD2;
  color: #F0F0F0;
}

QPushButton:focus {
  border: 1px solid #1464A0;
}

''')

cancel_b.setStyleSheet('''
QPushButton {
  background-color: #505F69;
  border: 1px solid #32414B;
  color: #F0F0F0;
  border-radius: 4px;
  padding: 3px;
  outline: none;
  /* Issue #194 - Special case of QPushButton inside dialogs, for better UI */
  min-width: 80px;
}

QPushButton:disabled {
  background-color: #32414B;
  border: 1px solid #32414B;
  color: #787878;
  border-radius: 4px;
  padding: 3px;
}

QPushButton:checked {
  background-color: #32414B;
  border: 1px solid #32414B;
  border-radius: 4px;
  padding: 3px;
  outline: none;
}

QPushButton:checked:disabled {
  background-color: #19232D;
  border: 1px solid #32414B;
  color: #787878;
  border-radius: 4px;
  padding: 3px;
  outline: none;
}

QPushButton:checked:selected {
  background: #1464A0;
  color: #32414B;
}

QPushButton::menu-indicator {
  subcontrol-origin: padding;
  subcontrol-position: bottom right;
  bottom: 4px;
}

QPushButton:pressed {
  background-color: #19232D;
  border: 1px solid #19232D;
}

QPushButton:pressed:hover {
  border: 1px solid #148CD2;
}

QPushButton:hover {
  border: 1px solid #148CD2;
  color: #F0F0F0;
}

QPushButton:selected {
  background: #1464A0;
  color: #32414B;
}

QPushButton:hover {
  border: 1px solid #148CD2;
  color: #F0F0F0;
}

QPushButton:focus {
  border: 1px solid #1464A0;
}

''')



root.show()
sys.exit(a.exec_())