import random

columns = 30 
rows = 10 

for rowIndex in range(rows):
    pattern = ''
    for colIndex in range(columns):
        a = random.random()  
        probability = colIndex / (columns - 1)  
        if a < probability:
            pattern += "O" 
        else:
            pattern += "."
    print(pattern) 