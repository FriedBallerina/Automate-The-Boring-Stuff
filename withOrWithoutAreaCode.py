import re

regexPhone = re.compile(r'(\d\d\d(-| ))?\d\d\d-\d\d\d\d')
mo = regexPhone.search('My number is 415-555-4242')
print(mo.group())

mo2 = regexPhone.search('My number is 555-4242')
print(mo2.group())