greetings = ['hello', 'hi', 'howdy', 'heyas', 'hello']
searchword = input('What word would you like to search? ')
if searchword in greetings:
    print('The word ' + searchword + ' is listed under index ' + str(greetings.index(searchword)))
else:
    print('The word ' + searchword + ' is not in the list.')