animals = ['cat', 'dog', 'bat']
animals.append('goat')
print(animals)

animals.insert(-1, 'last animal')
animals[-1], animals[-2] = animals[-2], animals[-1]

animals.append('the very last animal')

if 'cat' in animals:
    index = animals.index('cat')
    animals[index] = 'mouse'
    
print(animals)