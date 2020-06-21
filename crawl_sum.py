import urllib.request , urllib.parse , urllib.error
from bs4 import BeautifulSoup
import ssl

#ignore SSL certificates error
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter -')
html = urllib.request.urlopen(url , context = ctx).read()
soup = BeautifulSoup(html , 'html.parser')

sum1=0
tags = soup('span')
for tag in tags:
    sum1 += int(tag.contents[0])
print("COUNT : " , len(tags))
print("SUM : " , sum1)