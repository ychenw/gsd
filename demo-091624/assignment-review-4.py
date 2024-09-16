rows = 9
columns = 16

for j in range(rows):
    row = ''
    for i in range (columns):
        if (i%2+j%2) == 0:
            row += '.'
        else:
            row += 'O'
    
    print(row)