import random

rows = 9
columns = 26

for j in range(rows):
    row = ''
    for i in range (columns):
        if random.random() < 0.5:
            row += '/'
        else:
            row += '\\'
    
    print(row)