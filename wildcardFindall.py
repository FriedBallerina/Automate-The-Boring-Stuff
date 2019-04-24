import re

atRegex = re.compile(r'.at|\w+at')
print(atRegex.findall('The cat in the hat sat on the flat mat.'))