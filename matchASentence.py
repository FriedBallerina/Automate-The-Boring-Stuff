import re

regex_pattern = r'^(Alice|Bob|Carol)\s(eats|pets|throws)\s(apples|cats|baseballs)\.$'

sentence = re.compile(regex_pattern, re.I)
print(bool(sentence.search(input())))