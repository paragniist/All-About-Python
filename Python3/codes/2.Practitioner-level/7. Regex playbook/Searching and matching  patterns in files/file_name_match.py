import re
file = open("C:\Users\91981\Documents\All-About-Python\Python3\codes\2.Practitioner-level\7. Regex playbook\Searching and matching  patterns in files\data.txt","r")
f = file.readlines()

file_extension = ['pdf','doc','ppt','txt','docx']
pattern = r'\b\w+\.(?:'+'|'.join(file_extension)+r')\b'

matches = re.findall(pattern,f)