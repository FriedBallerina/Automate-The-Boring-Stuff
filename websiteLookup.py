import re

nameRegex = re.compile(r'(https*://\w+\.[\w//-]+)')
websites = nameRegex.findall('https://automatetheboringstuff.com/chapter7/, https://www.alexa.com/topsites, http://www.alexa.com/topsites')
for i in websites:
    if i[0:5] == 'https':
        websites[websites.index(i)] = i[8:]
    elif i[0:5] == 'http:':
        websites[websites.index(i)] = i[7:]
print(websites)