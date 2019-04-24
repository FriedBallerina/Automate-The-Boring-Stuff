import re
nameRegex = re.compile(r'First Name: (.*?) Last Name: (.*)')
mo = nameRegex.search('First Name: Mona, Last Name: Lisa')
print(mo.group(1), mo.group(2))
print(mo.groups())
print(mo.group())