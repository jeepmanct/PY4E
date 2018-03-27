
#imported the libs
from urllib import request
import xml.etree.ElementTree as ET

#URL of test
#url = 'http://py4e-data.dr-chuck.net/comments_42.xml'
url = 'http://py4e-data.dr-chuck.net/comments_55628.xml'


print ("Retrieving....", url)
html = request.urlopen(url)
data = html.read()
print("Retrieved...",len(data),"characters")

#find the comments that we need
tree = ET.fromstring(data)
results = tree.findall('comments/comment')
count=len(results)
total=0

#get the counts and totals
for result in results:
    total += float(result.find('count').text)
print("And the count is:", count)
print("And the grand total is:" ,total)
