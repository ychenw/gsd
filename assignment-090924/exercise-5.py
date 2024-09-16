import random 

for rowIndex in range(10):
    pattern = ''
    for colIndex in range (30):
        a = random.random()
        if a < 0.5:
            pattern += '/'
        else:
            pattern += '\\'
   
    print(pattern)