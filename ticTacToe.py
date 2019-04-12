aBoard = {'top-L' : ' ','top-M' : ' ','top-R' : ' ',
         'mid-L' : ' ','mid-M' : ' ','mid-R' : ' ',
         'low-L' : ' ','low-M' : ' ','low-R' : ' '}

theBoard = {'top-L': 'O', 'top-M': 'O', 'top-R': 'O', 'mid-L': 'X', 'mid-M':
'X', 'mid-R': ' ', 'low-L': ' ', 'low-M': ' ', 'low-R': 'X'}

def printBoard(board):
    print(board['top-L'] + '|' + board['top-M'] + '|' + board['top-R'] + '\n-+-+-')
    print(board['mid-L'] + '|' + board['mid-M'] + '|' + board['mid-R'] + '\n-+-+-')
    print(board['low-L'] + '|' + board['low-M'] + '|' + board['low-R'])

turn = 'X'
for i in range(9):
    print()
    printBoard(aBoard)
    print('Turn for ' + turn + '. Move on which space?')
    move = input()
    if aBoard[move] == ' ':
        aBoard[move] = turn
    else:
        print('\n*****This slot is taken. Please pick another one!*****')
        continue
    if aBoard['top-L'] == aBoard['top-M'] and aBoard['top-L'] == aBoard['top-R'] and (aBoard['top-L'] == 'X' or aBoard['top-L'] == 'O'):
        print(aBoard['top-L'] + ' won!')
        break
    elif aBoard['mid-L'] == aBoard['mid-M'] and aBoard['mid-L'] == aBoard['mid-R'] and (aBoard['mid-L'] == 'X' or aBoard['mid-L'] == 'O'):
        print(aBoard['mid-L'] + ' won!')
        break
    elif aBoard['low-L'] == aBoard['low-M'] and aBoard['low-L'] == aBoard['low-R'] and (aBoard['low-L'] == 'X' or aBoard['low-L'] == 'O'): 
        print(aBoard['low-L'] + ' won!')
        break
    elif aBoard['top-L'] == aBoard['mid-M'] and aBoard['top-L'] == aBoard['low-R'] and (aBoard['top-L'] == 'X' or aBoard['top-L'] == 'O'):
        print(aBoard['top-L'] + ' won!')
        break
    elif aBoard['top-R'] == aBoard['mid-M'] and aBoard['top-R'] == aBoard['low-L'] and (aBoard['top-R'] == 'X' or aBoard['top-R'] == 'O'):
        print(aBoard['top-R'] + ' won!')
        break
    elif aBoard['top-L'] == aBoard['mid-L'] and aBoard['top-L'] == aBoard['low-L'] and (aBoard['top-L'] == 'X' or aBoard['top-L'] == 'O'):
        print(aBoard['top-L'] + ' won!')
        break
    elif aBoard['top-M'] == aBoard['mid-M'] and aBoard['top-M'] == aBoard['low-M'] and (aBoard['top-M'] == 'X' or aBoard['top-M'] == 'O'):
        print(aBoard['top-M'] + ' won!')
        break
    elif aBoard['top-R'] == aBoard['mid-R'] and aBoard['top-R'] == aBoard['low-R'] and (aBoard['top-R'] == 'X' or aBoard['top-R'] == 'O'):
        print(aBoard['top-R'] + ' won!')
        break
    
    if turn == 'X':
        turn = 'O'
    else:
        turn = 'X'

print()
printBoard(aBoard)