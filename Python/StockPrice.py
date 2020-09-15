import pandas as pd 
from pandas_datareader import data
from datetime import datetime, timedelta


def get_price_data(symbols, start_date, end_date):
    return data.DataReader(symbols, 'yahoo', start_date, end_date)
    
def get_close_price_1w(symbols):
    end_date=datetime.today()
    start_date=datetime.today()-timedelta(days=7)
    return get_price_data(symbols, start_date, end_date)

def get_close_price_1m(symbols):
    end_date=datetime.today()
    start_date=datetime.today()-timedelta(days=30)
    return get_price_data(symbols, start_date, end_date)

def get_close_price_1y(symbols):
    end_date=datetime.today()
    start_date=datetime.today()-timedelta(days=365)
    return get_price_data(symbols, start_date, end_date)