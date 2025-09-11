import re

sum =0
file_hand = open('text.txt','r')

for lines in file_hand:
    number = re.findall(r'\d+',lines)
    for num in number:
        sum += int(num)
print("sum = ",sum)