#working with text files
def read_txt(fn):
    with open(fn) as f:
        print(f.read())

def read_txt_by_line(fn):
    with open(fn) as f:
        lines = f.readlines()
        for line in lines:
            print(line,end='')
            line =f.readline()

def write_txt(fn,text):
    with open(fn,'w',encoding='utf-8') as f:
        f.write(text)

def append_txt(fn,text):
    with open(fn,'a') as f:
        f.write('\n')
        f.write(text)
write_txt('./files/example.txt','Hello World')


#working with CSV files
import csv

def read_csv(fn):
    with open(fn) as f:
        cnt = -1
        rows = csv.reader(f,delimiter='')
        for row in rows:
            if cnt == -1:
                print('{"|".join(row)}')
            else:
                print('{r[0]} | {r[1]}'.format(r=row))
            cnt += 1

def write_csv(fn,header,row):
    with open(fn,'w',newline='') as f:
         writer = csv.writer(f,delimiter=',',quotechar="'",quote=csv.QUOTE_NONE,quoting=csv.QUOTE_MINIMAL)
         writer.writerow(header)
         writer.writerow(row)

#working with XML files
import xml.etree.ElementTree as ET

def parse_xml(xml):
    tree = ET.parse(xml)
    root = tree.getroot()
    print('Domain'+root.attrib['domain'])
    for child in root:
        print(child.tag)

parse_xml('./files/example.xml')


def add_xml(xml,el,attr,val):
    tree = ET.parse(xml)
    root = tree.getroot()
    child = ET.Element(el)
    child.set(attr,val)
    root.append(child)
    tree.write(xml)

def change_xml(xml,el,attr,val,new_val):
    tree = ET.parse(xml)
    root = tree.getroot()
    child = root.find("./"+el+"[@"+attr+"="+val+"']'")
    child.attrib["value"] = new_val
    tree.write(xml)


#working with JSON files
import json

def read_json(fn,pretty,sort):
    with open(fn) as json_file:
        data = json.load(json_file)
        print(json.dumps(data,sort_keys=sort,indent=4
        if pretty else data))

def update_author_json(fn,arr_name,pos,key,value):
    with open(fn,'r') as json_file:
        data = json.load(json_file)
        data[arr_name][pos][key] = value
        with open(fn,'w') as json_file:
            json.dump(data,json_file)

#persisting objects
import pickle

class Person:
    age =45
    name = 'John smith'
    kids = ['Pete','Lily','Kate']
    employers = {'AWS':2022,'Microsoft':2018,'Yahoo':2005}
    shoe_size = (11,12)

def serialize(obj):
    pickled = pickle.dumps(obj,protocol=pickle.HIGHEST_PROTOCOL)
    print('Serialized object',pickled)
    return pickled

def deserialize(serialized):
    pickled = pickle.loads(serialized)
    print('Deserialized object',pickled)

def deserlized_employee(obj):
    unpickled = pickle.loads(obj)
    print(f'Deserialized object:  \n{unpickled.employers}')

def obj_to_file(fn,obj):
    with open(fn,'wb') as f:
        pickle.dump(obj,f,protocol=pickle.HIGHEST_PROTOCOL)

def file_to_obj(fn,obj):
    with open(fn,'rb') as f:
         obj = pickle.load(f)
         print(obj)
         return obj

pickled = serialize(Person())
deserialize(pickled)
deserlized_employee(pickled)




