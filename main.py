#https://github.com/ranaroussi/yfinance
from pandas_datareader import data as pdr
import yfinance as yf

yf.pdr_override() # <== that's all it takes :-)

# download dataframe
data = pdr.get_data_yahoo("SPY", start="2017-01-01", end="2017-04-30")
print (data.head())

'''
Project: starlingbank-ibank, SavingsRounder
Author: Miro Gregorovic, m.gregorovic1@gmail.com
Date: 20190402
'''

"""
import pandas as pdª
import requests
import os
import pprint
from monzo import Monzo # Import Monzo class
import pymonzo as pm
account_id = 'acc_00009fhkE9hjNt9d2mL6Ab'
bearer_id ='eyJhbGciOiJFUzI1NiIsInR5cCI6IkpXVCJ9.eyJlYiI6ImxXcmo2Z3hOWnlENzlSejJvemhDIiwianRpIjoiYWNjdG9rXzAwMDA5cTV1YkNHRUFlOWxMdTdodFIiLCJ0eXAiOiJhdCIsInYiOiI2In0.MYAqyQl-X3HkFUhDRpncA0532subpO1dXwqb5wlg8-PO_jpwxO7fjOX9QnThS4RRo_fuNapn4JFXFhI1MMzASQ'
client = Monzo(bearer_id) # Replace access token with a valid token found at: https://developers.monzo.com/
balance = client.get_balance(account_id) # Get your balance object
print(balance['balance']) # 100000000000
print(balance['currency']) # GBP
print(balance['spend_today']) # 2000

transactions = client.get_transactions(account_id)
print (transactions[0])
"""
"""
import time
import numpy as np

size_of_vec = 100000

def pure_python_version():
    t1 = time.time()
    X = range(size_of_vec)
    Y = range(size_of_vec)
    Z = [X[i] + Y[i] for i in range(len(X)) ]
    return time.time() - t1

def numpy_version():
    t1 = time.time()
    X = np.arange(size_of_vec)
    Y = np.arange(size_of_vec)
    Z = X + Y
    return time.time() - t1

t1 = pure_python_version()
t2 = numpy_version()
print(t1, t2)
print("Numpy is in this example " + str(t1/t2) + " faster!")
"""