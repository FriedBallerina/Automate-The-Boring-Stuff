import re

number = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')


while True:
    userInput = input('What\'s your phone number? Please insert the number in the following format: 111-111-1111\n')
    try:
        mo = number.search(userInput)

        if type(mo.group()) != 'NoneType':
            print('Thank you.')
            break
    except:
        print('Erroneous input.'.upper(), end = ' ')
