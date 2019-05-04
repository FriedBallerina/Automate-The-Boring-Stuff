import re

regex_pattern = r'^[A-Z][a-z]+ (Nakamoto)$'

while True:
    print('Valid name' if (bool(re.search(regex_pattern, input()))) == True else 'Invalid name')