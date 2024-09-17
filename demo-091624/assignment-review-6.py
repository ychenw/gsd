import random

rows = 9
columns = 26

for j in range(rows):
    row = f''
    for i in range (columns):
        th = i/(columns-1)
        if random.random() < th:
            row += 'O'
        else:
            row += '.'
    
    print(row)