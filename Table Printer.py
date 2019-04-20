tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]

def printTable(data):
    
    maxLength = 0
    for row in data:
        for item in row:
            if len(item) > maxLength:
                maxLength = len(item)
    
    for i in range(len(data[0])):
        for j in range(len(data)):
            print(data[j][i].rjust(maxLength), end = '')
        print()
        
printTable(tableData)