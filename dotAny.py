import re

numRegex = re.compile(r'\d+')
newText = numRegex.sub('X', '12 drummers, 11 pipers, five rings, 3 hens')
print(newText)