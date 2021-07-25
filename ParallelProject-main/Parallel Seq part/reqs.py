from newsapi import NewsApiClient
import datetime as dt
import pandas as pd
import sqlite3 as db
import json
from dataClass import News

def init_api_conn(key):
  return  NewsApiClient(api_key=key)


def request_Data_1(newsapi):
  return newsapi.get_everything(q='iphone x',
                           language='en',
                         from_param='2021-03-08',
                         to='2021-03-08',
                             page=1)

def request_Data_2(newsapi):
  return newsapi.get_everything(q='iphone x',
                           language='en',
                         from_param='2021-03-08',
                         to='2021-03-08',
                             page=2)
def request_Data_3(newsapi):
  return newsapi.get_everything(q='samsung',
                           language='en',
                         from_param='2021-03-08',
                         to='2021-02-08',
                             page=1)
def request_Data_4(newsapi):
  return newsapi.get_everything(q='iphone 11',
                           language='en',
                         from_param='2021-03-08',
                         to='2021-03-08',
                             page=4)
def request_Data_5(newsapi):
  return newsapi.get_everything(q='iphone 12',
                           language='en',
                         from_param='2021-03-08',
                         to='2021-03-08',
                             page=5)


