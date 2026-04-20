#6.1 The program will prompt for a URL, read the JSON data from that URL using urllib and then parse and extract the comment counts from the JSON data, compute the sum of the numbers
# in the file.

import urllib.request
import json

url = 'https://py4e-data.dr-chuck.net/comments_2264363.json'

jn = urllib.request.urlopen(url).read().decode('utf8')
data = json.loads(jn)
ls = list()
for comment in data['comments']:
    number = comment['count']
    ls.append(number)

print(len(ls))
print(sum(ls))

###
import urllib.request, urllib.parse
import json, ssl

# Heavily rate limited proxy of https://www.geoapify.com/ api
serviceurl = 'https://py4e-data.dr-chuck.net/opengeo?'

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

while True:
    address = input('Enter location: ')
    if len(address) < 1: break

    address = address.strip()
    parms = dict()
    parms['q'] = address

    url = serviceurl + urllib.parse.urlencode(parms)

    print('Retrieving', url)
    uh = urllib.request.urlopen(url, context=ctx)
    data = uh.read().decode()
    print('Retrieved', len(data), 'characters', data[:20].replace('\n', ' '))

    try:
        js = json.loads(data)
    except:
        js = None

    if not js or 'features' not in js:
        print('==== Download error ===')
        print(data)
        break

    if len(js['features']) == 0:
        print('==== Object not found ====')
        print(data)
        break

    # print(json.dumps(js, indent=4))

    lat = js['features'][0]['properties']['lat']
    lon = js['features'][0]['properties']['lon']
    print('lat', lat, 'lon', lon)
    location = js['features'][0]['properties']['formatted']
    print(location)


print('\n')


##
import urllib.request, urllib.parse, json, ssl

# Google Maps Geocoding API endpoint
serviceurl = 'https://maps.googleapis.com/maps/api/geocode/json?'

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

address = "Federal University of Minas Gerais"
parms = {
    'address': address,
    'key': 'AIzaSyAqddvD7WqDtOJE4LMwSDa898McJ2FCmNI'   # <-- replace with your API key
}
url = serviceurl + urllib.parse.urlencode(parms)

print("Retrieving", url)
uh = urllib.request.urlopen(url, context=ctx)
data = uh.read().decode()

js = json.loads(data)

if 'plus_code' in js:
    print("Global Code:", js['plus_code']['global_code'])
    print("Compound Code:", js['plus_code']['compound_code'])




