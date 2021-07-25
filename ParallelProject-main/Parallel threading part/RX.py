from newsapi import NewsApiClient
from rx import create
import datetime as dt
import pandas as pd
import sys
from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, \
    QPushButton, QVBoxLayout, QLineEdit, QLabel, QMessageBox, QLineEdit, QLabel
import codeRX
a = QApplication(sys.argv)


def get():
      source1 = codeRX.source
      source1.subscribe(
          on_next=lambda i: print("Received {0}".format(i)),
          on_error=lambda e: print("Error Occurred: {0}".format(e)),
          on_completed=lambda: print("Done!"),
      )
def get_from_database():
    print('second')


def insert_into_database():
    print('third')


newsapi = NewsApiClient(api_key='f66d1d1fc6994c6f989e99d65d9a8d9a')
data1 = newsapi.get_everything(q='iphone x',
                               language='en',
                               from_param='2021-03-08',
                               to='2021-03-11',
                               page=2)

data2 = newsapi.get_everything(q='iphone x',
                               language='en',
                               from_param='2021-03-08',
                               to='2021-03-11',
                               page=3)

data3 = newsapi.get_everything(q='iphone x',
                               language='en',
                               from_param='2021-03-08',
                               to='2021-03-11',
                               page=4)

data4 = newsapi.get_everything(q='iphone x',
                               language='en',
                               from_param='2021-03-08',
                               to='2021-03-11',
                               page=5)

data5 = newsapi.get_everything(q='iphone x',
                               language='en',
                               from_param='2021-03-08',
                               to='2021-03-11',
                               page=5)

root = QWidget()
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

root.setWindowTitle('parallel')  # board title
root.setFixedSize(640, 480)

get_b = QPushButton('get', root)  # adding button
get_b.move(100, 50)
get_b.clicked.connect(get)

get_from_database_b = QPushButton('Get from database', root)  # adding button
get_from_database_b.move(250, 50)
get_from_database_b.clicked.connect(get_from_database)

insert_into_database_b = QPushButton('Insert into database', root)  # adding button
insert_into_database_b.move(450, 50)
insert_into_database_b.clicked.connect(insert_into_database)

cancel_b = QPushButton('cancel', root)  # adding button
cancel_b.move(450, 400)
cancel_b.clicked.connect(root.close)  # Exit root

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