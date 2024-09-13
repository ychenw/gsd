import random

columns = 30 
rows = 10 

for rowIndex in range(rows):
    pattern = ''
    for colIndex in range(columns):
        a = random.random()  
        if a < colIndex / (columns - 1):
            pattern += "O" 
        else:
            pattern += "."
    print(pattern) 
