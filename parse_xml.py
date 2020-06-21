import xml.etree.ElementTree as ET

data = '''<stuff>
        <people> 
        <person>
            <name>Pritam</name>
            <phone type="Intl">
                9566614767
            </phone>
            <email hide="yes"/>
        </person>
        <person>
            <name>Tarun</name>
            <name>Rodriguez</name>
            <phone type="Local">
                9566614768
            </phone>
            <email hide="No">
                tarunpritamvrs@gmail.com
            </email>
        </person>
    </people>
    </stuff>'''

stuff = ET.fromstring(data)
# print('Name : ', tree.find('name').text)
# print('Attr : ' , tree.find('email').get('hide'))
# print('Attr : ' , tree.find('phone').get('type'))

lst = stuff.findall('people/person')
print(lst)
print('People : ' , len(lst))
for item in lst:
    print('Name : ' , item.find('name').text)
    print('Attr : ' , item.find('email').get('hide'))