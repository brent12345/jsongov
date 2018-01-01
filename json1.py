#!/usr/local/bin/python
# coding=utf-8
"""
 Simple example of a Python script used to query an API.

 @note:    This is a simple example without any error handling.
 @license: http://data.gc.ca/eng/open-government-licence-canada
"""
import json
import requests
import urllib.request

url = "http://www.infrastructure.gc.ca/alt-format/opendata/project-list-liste-de-projets-bil.json"

with urllib.request.urlopen(url) as url:
    data = json.loads(url.read().decode())
    #print(data['data'][0], data['data'][1])

for x in data['data']:
    print(x[7])
