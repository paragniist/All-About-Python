# match object has many methods associated 
import re

text = "My phone number is 555-555-1234"
pattern = r'(\d{3})-(\d{3}-\d{4})'

match = re.search(pattern, text)

if match :
    #1. group()
    print(f'Matched phone number : {match.group()}')
    #2. groups()
    print(f'Area Code: {match.group(1)}')
    print(f'Phone Number : {match.group(2)}')
    #4. start()
    print(f'Start position: {match.start()}')
    #5. end()
    print(f'End position : {match.end()}')
    #6. span()
    print(f'Span : {match.span()}')