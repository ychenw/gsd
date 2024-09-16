for rowIndex in range(10):
    pattern = ''  
    for colIndex in range(10):
        if colIndex < rowIndex:
            pattern += 'O' 
        else:
            pattern += '.'  
   
    print(pattern)