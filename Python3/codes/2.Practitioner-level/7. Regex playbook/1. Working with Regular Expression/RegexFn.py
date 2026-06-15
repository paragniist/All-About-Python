import re

#1. Search: scans through the string and looks for the first match 

text1 = "This is a sample test text"
pattern1 = "sample"

match1 = re.search(pattern1, text1)
if match1:
    print("Match Found")
else:
    print("No Match Found")


#2. Match : Checks if the begging of the string matches the patterns

text2 = "The quick brown fox"
pattern2 = r'The'

match2 = re.match(pattern2, text2)
if match2:
    print("The string starts with 'The'")
else:
    print("The string do not starts with 'The'")


#3. Fullmatch : Checks if the full string matches the patterns

text3 = '2023-03-11'
pattern3 = r'\d{4}-\d{2}-\d{2}'

match3 = re.fullmatch(pattern3, text3)
if match3:
    print(f"The date string {text3} is valid")
else:
    print(f"The date string {text3} is not valid")


#4. Findall : searches a string for all non-overlapping matches

text4 = 'the price of the book is $18.88 and the price of the price of the movie is $12.50'
pattern4 = r'\d+'

match4 = re.fullmatch(pattern4, text4)
print(match4)


#5.Sub and subn : Search a  string for all non-overlapping occurences and replace them with a string

text5 = 'The quick brown fox jumps over the lazy dog'
pattern5 = r'\b\w{4}\b'

match5 = re.sub(pattern5,"******", text5)
print(match5)


#6. Split Function : Splits a string at every occurence of the pattern

text6 = 'The quick brown fox jumps over the lazy dog'
pattern6 = r'\s+'

match6 = re.split(pattern6, text6)
print(match6)


#7. Escape Function : used for escaping special characters so that they can match with the text

text7 = r'The quick \brown fox jumps over the lazy dog'
pattern7 = r'\b'

escape_pattern =re.escape(pattern7)
match7 = re.search(escape_pattern, text7)

if match7:
    print("Found a word in the boundary")
else:
    print("Could not find a word in the boundary")



#8. Compile Function : used for compiling a pattern into regex object

text8 = 'the price of the book is $18.88 and the price of the price of the movie is $12.50'
pattern8 = r'\d+'

regex = re.compile(pattern8)
match8 = regex.findall(text8)
print(match8)
