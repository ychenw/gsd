rows = 9
columns = 16

for j in range(rows):
    row = ''
    for i in range (columns):
        if i < j:
            row += 'O'
        else:
            row += '.'
    
    print(row)