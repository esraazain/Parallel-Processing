from newsapi import NewsApiClient
from rx import create
import datetime as dt
import pandas as pd

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


def push_five_strings(observer, schedule):
    observer.on_next(data1)
    observer.on_next(data2)
    observer.on_next(data3)
    observer.on_next(data4)
    observer.on_next(data5)

    observer.on_completed()


source = create(push_five_strings)

