#5.1 write a Python program somewhat similar to https://www.py4e.com/code3/xml3.py -
# The program will prompt for a URL, read the XML data from that URL using urllib and
# then parse and extract the comment counts from the XML data, compute the
# sum of the numbers in the file and enter the sum.

import urllib.request
import xml.etree.ElementTree as ET

url = ' http://py4e-data.dr-chuck.net/comments_2264362.xml'
xml = urllib.request.urlopen(url).read()

tree = ET.fromstring(xml)
count = tree.findall('.//count')
nums = list()
for result in count:
    print(result.text)
    nums.append(int(result.text))

print('Count:', len(nums))
print('Sum:', sum(nums))