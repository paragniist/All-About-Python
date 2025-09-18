import requests

people = requests.get("http://api.open-notify.org/astros.json")
json = people.json()

print('The people currently have the following Astros: ')
for person in json['people']:
    print(person['name'])