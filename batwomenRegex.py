import re

batRegex = re.compile(r'Bat(wo)?m(a|e)?n')
mo1 = batRegex.search('The Adventures of Batwomen')
print(mo1.group())