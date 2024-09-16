for rowIndex in range (10):
    pattern = ''
    for colIndex in range (20):
        if (colIndex + rowIndex) % 2 == 0:
            pattern += 'O'
        else:
            pattern += '.'
    
    print(pattern)