import re

threeCommaRegex = re.compile(r'^\d{1,3}(,d{3})*')
mo1 = threeCommaRegex.search('1,234')
print(mo1.group())