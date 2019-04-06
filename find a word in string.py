name = 'Ruth a cat'
index = []
a = ' a '
the = ' the'
if  a in name:
    index = name.index(' a ')
    name = name.replace(name[index:index + 2], the)
print(name)