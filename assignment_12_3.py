# To run this, you can install BeautifulSoup
# https://pypi.python.org/pypi/beautifulsoup4

# Or download the file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl
import urllib

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

#data entry
theurl = input('Enter - ')
count = int(input('Count: '))
position = int(input('Position: '))

taglist=list()

for i in range(count):
    print(count)
    print ("Retrieving:",theurl)
    html = urllib.request.urlopen(theurl, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
    tags=soup('a')
    for tag in tags:
        taglist.append(tag)
    theurl = taglist[position-1].get('href', None)
    del taglist[:]
print ("Retrieving:",theurl)
