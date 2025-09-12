#4.1 write a Python program to use urllib to read the HTML from
# the data files below, and parse the data,
# extracting numbers and compute the sum of the numbers in the file

import urllib.request, urllib.error
import re
from bs4 import BeautifulSoup
url = 'https://py4e-data.dr-chuck.net/comments_2264360.html'
html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html, 'html.parser')
html1= soup.get_text()
number = re.findall('[0-9]+', html1)
number = [int(num) for num in number]

print(sum(number))
#
# #4.2 write a Python program that expands on
# https://www.py4e.com/code3/urllinks.py
# The program will use urllib to read the HTML from the data files below,
# extract the href= values from the anchor tags,
# scan for a tag that is in a particular position from the top and follow
# that link, repeat the process a number of times, and report the last name you find.


import urllib.request
import urllib.error
from bs4 import BeautifulSoup


url = "https://py4e-data.dr-chuck.net/known_by_Famara.html"
count = int(input("Enter count: "))
position = int(input("Enter position: "))

for i in range(count):
    html = urllib.request.urlopen(url).read()
    soup = BeautifulSoup(html, 'html.parser')
    tags = soup('a')
    url = tags[position - 1].get('href', None)
name = url.split('_')[-1].split('.')[0]
print("Last name:", name)