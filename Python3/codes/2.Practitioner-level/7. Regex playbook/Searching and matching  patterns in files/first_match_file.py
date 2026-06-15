import re
file = open("data.txt","r")
f = file.readlines()
for line in f:
        match = re.search("sample",line)
        if match :
            print("Found a match")
            break