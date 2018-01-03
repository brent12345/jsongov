#!/usr/local/bin/python
# coding=utf-8
"""
script imports Federal projects in Canada
"""
import json
import re
import requests
import urllib.request

url = "https://data.novascotia.ca/api/views/7dfb-h4nw/rows.json?accessType=DOWNLOAD"

with urllib.request.urlopen(url) as url:
    data = json.loads(url.read().decode())
    #print(data['data'][0], data['data'][1])



for d in data['data']:
    str1 = d[12]
    #match = re.search(r'nova', str1)
    # If-statement after search() tests if it succeeded
    #if match:
        #for x in data['data']:
           # print(x[7], x[9])
             #print(match.string)
    #else:
            #pass
    if int(str1) > 12:
        print('found')