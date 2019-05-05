import re

def regexStrip(userString = input('Insert the string to process:\n'), delimeter = ' ', optionalDelimiter = ''):
    subRegex = re.compile(r' ')
    stringWithoutWhitespaces = subRegex.sub('', userString)
    return stringWithoutWhitespaces

print(regexStrip())