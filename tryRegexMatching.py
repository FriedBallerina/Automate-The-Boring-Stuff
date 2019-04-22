import re

regexObject = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
mo = regexObject.search('Hello, my number is 555-555-5555.')
print(mo.group())