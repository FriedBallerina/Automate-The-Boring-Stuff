import re

phoneNumber = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
number = phoneNumber.search('My number is 415-9856-3654.')
try:
    print('Phone number found: ' + number.group())
except AttributeError:
    print('There is no phone number found.')