# row = ''
# for j in range(3):
#     print(f'j:{j}')
#     for i in range(3):
#         print(f'i:{i}')

# print(row)



# row = ''
# for j in range(3):
#     for i in range(3):
#         print(f'[{j},{i}]', end='')
#     print()

# print(row)



# row = ''
# for j in range(3):
#     for i in range(3):
#         row += f'[{j},{i}]'
#     print(row)



# for j in range(6):
#     row = ''
#     for i in range(5):
#         row += f'[{j},{i}]'
#     print(row)



for j in range(5):
    row = ''
    for i in range(6):
        if i< 3:
            row += f'*'
        else:
            row += f'.'
    print(row)

