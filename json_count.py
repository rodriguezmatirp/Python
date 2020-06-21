import json
import urllib.request, urllib.parse, urllib.error
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = 'http://py4e-data.dr-chuck.net/comments_591451.json'
uh = urllib.request.urlopen(url, context=ctx)

print('Retrieving ' , url)

data = uh.read()

info = json.loads(data)

print('Retrived ' , len(data) , 'characters')

print('Count : ' , len(info["comments"]))

sum_ = 0

for num in range(len(info["comments"])):
    sum_ += int(info["comments"][num]["count"])

print('Sum : ' , sum_)