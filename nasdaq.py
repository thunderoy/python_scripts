#!/usr/bin/env python3
import requests

def nasdaq():
    n_s = input('enter the nasdaq symbol of any company: ')
    payload = {'s': n_s, 'f': 'l1'}
    res = requests.get('http://download.finance.yahoo.com/d/quotes.csv', params=payload)
    # print(res.raise_for_status())

    if res.text == 'N/A\n':
        print('wrong nasdaq symbol')
    else:
        print('nasdaq value: ' + res.text.strip())

try:
    nasdaq()
except requests.exceptions.ConnectionError:
    print("No Internet Connection :(")
