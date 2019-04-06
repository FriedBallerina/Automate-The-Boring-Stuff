spam = ['apples', 'bananas', 'tofu', 'cats']

def commaCode(anyList):
    for i in anyList:
        if i == anyList[-1]:
            print('and ' + anyList[-1])
        else:
            print(i, end = ', ')
            
commaCode(spam)