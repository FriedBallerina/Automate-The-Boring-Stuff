grid = [['.', '.', '.', '.', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['.', 'O', 'O', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.']]
#i = 0
#while i < len(grid):
#    j = 0
#    while j < len(grid[i]):
#        print(grid[i][j], end = '')
#        j += 1
#    print()
#    i += 1

x = 0
y = 0

while y < len(grid[x]):
    while x < len(grid):
        print(grid[x][y], end = '')
        x += 1
    print()
    x = 0
    y += 1