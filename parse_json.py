import json
data = '''{
    "name" : "Pritam",
    "phone" : {
        "type" : "Intl",
        "number" : "9566614767"
    },
    "email" :{
        "hide" : "yes"
    }
}'''

info = json.loads(data)
print('Name : ' , info["name"])
print('Hide : ' , info["email"]["hide"])
print("Phone : ", info["phone"]["number"])