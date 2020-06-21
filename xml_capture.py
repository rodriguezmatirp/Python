import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

while True:
    url = input('Enter location: ')
    if len(url) < 1: break
    
    print('Retrieving', url)
    uh = urllib.request.urlopen(url, context=ctx)

    data = uh.read()
    print('Retrieved', len(data), 'characters')
    
    commentinfo = ET.fromstring(data)

    lst = commentinfo.findall('comments/comment')
    # counts = commentinfo.findall('.//count')
    # sum2 = 0 
    # for count in counts:
    #     sum2 += int(count.text)
    # print(sum2)
    print('Count : ' , len(lst))
    sum_count = 0
    for item in lst:
        sum_count += int(item.find('count').text)
    print('Sum : ' , sum_count)
    break