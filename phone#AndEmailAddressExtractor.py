#! python3
# phone#AndEmailAddressExtractor.py - finds phone numbers and email addresses on the clipboard and prints them in a column

import pyperclip, re

matches = []
copiedFromClipboard = pyperclip.paste()

phoneNumberRegex = re.compile(r'''\d{3}|(\d{3}\))?
                             (\s|-|\.)?
                             (\d{3})
                             (\s|-|\.)
                             (\d{4})
                             (\s*(ext|x|ext.)\s*(\d{2,5}))?
                             ''', re.VERBOSE)

emailAddressRegex = re.compile(r'''(
                                [a-zA-Z0-9._%+-]+                    # local part
                                @                           # at-sign
                                [a-zA-Z0-9.-]+
                                (\.[a-zA-Z]{2,4})                # domain
                                )''', re.VERBOSE)

findEmailAddresses = emailAddressRegex.findall(copiedFromClipboard)

for groups in phoneNumberRegex.findall(copiedFromClipboard):
    phoneNum = '-'.join([groups[1], groups[3], groups[5]])
    if groups[8] != '':
        phoneNum += ' x' + groups[8]
    matches.append(phoneNum)
    
for groups in emailAddressRegex.findall(copiedFromClipboard):
    matches.append(groups[0])
    
finds = ''
for i in matches:
    if i != matches[-1]:
        finds = finds + i + ', '
    else:
        finds = finds + i

copiedToClipboard = pyperclip.copy(finds)

print(copiedToClipboard)