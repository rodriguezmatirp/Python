import urllib.request , urllib.parse , urllib.error
fhand = urllib.request.urlopen('https://rodriguez-weather-app.herokuapp.com/weather?address=madurai')
for line in fhand:
    print(line.decode().strip())