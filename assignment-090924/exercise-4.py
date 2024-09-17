rows = 10
columns = 20

for j in range (rows):
    pattern = ''
    for i in range (columns):
        if (i + j) % 2 == 0:
            pattern += 'O'
        else:
            pattern += '.'
    
    print(pattern)