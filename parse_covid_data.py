import json
import urllib.request, urllib.parse, urllib.error
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = 'https://api.covid19india.org/data.json'
uh = urllib.request.urlopen(url, context=ctx)

print('Retrieving ' , url)

data = uh.read()

info = json.loads(data)

print('Retrived ' , len(info["statewise"]) , 'State info')

while True:
    state_input = input('Enter State - ')
    p_state = info["statewise"]

    temp = state_input.split(' ')
    capitalize = [p.capitalize() for p in temp]
    state = " ".join(capitalize)
    print(state)

    flag = 0
    for num in range(len(p_state)):
        if(p_state[num]["state"] == state):
            print(p_state[num])
            flag = 1
            

    if( flag == 0):
        print('Check the State That You have Entered And Leave space in between if Your state has Two words or more')
    else:
        break



