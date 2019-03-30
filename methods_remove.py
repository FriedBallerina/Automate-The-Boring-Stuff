animals = ['cat', 'dog', 'bat']
animals.append('cat')
print(animals)

while 'cat' in animals:
    animals.remove('cat')
    
print(animals)