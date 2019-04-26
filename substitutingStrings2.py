import re

namesRegex = re.compile(r'Agent (\w)\w*')
print(namesRegex.sub(r'Agent \1*****', 'Agent Alice gave the secret documents to Agent Bob.'))