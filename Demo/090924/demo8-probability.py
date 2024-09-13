import random

# for j in range(10):
#     row = ''
#     for i in range(30):
#         a = random.random()
#         if a < 0.9:
#             row += '.'
#         else:
#             row += "0"
#     print(row)


for j in range(3):
    row = ''
    # use it as the place holder
    for i in range(20):
        a = random.random()
        # a statement: give me a random number between 0 ~ 1
        if a < 0.2:
            row += '.'
        elif a < 0.7:
            row += '+'
        else:
            row += "-"
    print(row)