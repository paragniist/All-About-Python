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