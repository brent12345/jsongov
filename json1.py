#!/usr/local/bin/python
# coding=utf-8
"""
 Simple example of a Python script used to query an API.

 @note:    This is a simple example without any error handling.
 @license: http://data.gc.ca/eng/open-government-licence-canada
"""
import json

import re
import requests
import urllib.request

url = "http://www.infrastructure.gc.ca/alt-format/opendata/project-list-liste-de-projets-bil.json"

with urllib.request.urlopen(url) as url:
    data = json.loads(url.read().decode())
    #print(data['data'][0], data['data'][1])

for x in data['data']:
    print(x[7], x[9])

for d in data['data']:
    str1 = d[1]
    match = re.search(r'nova', str1)
    # If-statement after search() tests if it succeeded
    if match:
        print('found', match.group()) ## 'found word:cat'
    else:
        print('did not find')
