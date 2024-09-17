rows = 9
columns = 16

for j in range(rows):
    row = ''
    for i in range (columns):
        if i%2 == 0 and j%2 == 0:
            row += '.'
        else:
            row += 'O'
    
    print(row)

	# •	(i + j) % 2 == 0 会产生交错的效果，像棋盘格子一样的排列。
	# •	i % 2 == 0 and j % 2 == 0 只会在偶数行的偶数列显示特定的字符，形成不连续的、较为稀疏的模式。