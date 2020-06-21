import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
count = int(input('Enter count : '))
pos = int(input('Enter Position : ')) - 1
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')

# Retrieve all of the anchor tags
for i in range(count):
    tags = soup('a')
    print('Retrieving : ' , url)
    url = tags[pos].get('href',None)
    html = urllib.request.urlopen(url,context=ctx)
    soup = BeautifulSoup(html ,'html.parser')
    if(i == count- 1):
        print(tags[pos].contents[0])
    else:
        continue
        