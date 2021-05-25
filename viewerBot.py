#!/usr/bin/env python
# coding: utf-8

import requests
from bs4 import BeautifulSoup
from random import choice
import time

def get_proxy():
    url = "https://www.sslproxies.org/"
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')
    return {'https': choice(list(map(lambda x:x[0]+':'+x[1], list(zip(map(lambda x:x.text, soup.findAll('td')[::8]),
                                     map(lambda x:x.text, soup.findAll('td')[1::8]))))))}

print ("Dribble Proxy Start: " + time.strftime("%a, %d %b %Y %H:%M:%S | %s"))
get_proxy()
print (get_proxy())

def proxy_request(request_type, url, **kwargs):
    while 1:
        try:
            proxy = get_proxy()
            r = requests.request(request_type, url, proxies=proxy, timeout=5, **kwargs)
            break
        except:
            pass
    return r

r = proxy_request('GET', "http://5d20b675040c.ngrok.io")

r.text

print ("Dribble Like Finish: " + time.strftime("%a, %d %b %Y %H:%M:%S | %s"))
