# from random import random
# data = []
# for j in range(10):
#     data.append(int(random()*10))
# print(data)

# # s = []
# # for i in data:
# #     if data.count(i) == 1:
# #         s.append(i)
# # print(s)
# f =[]
# for k in data:
#     b = 0
#     for h in data:
#         if k ==h:
#             b += 1
#     if b == 1:
#         f.append(k)
# print(f)

def multipliers():
    return [lambda x: i * x for i in range(3)]   # ошибочные значения

def multipliers1():
    def item(i):
        return lambda x: i * x
    return [item(i) for i in range(3)]

def multipliers2():
    return [(lambda i_2: (lambda x: i_2 * x))(i) for i in range(3)]

def multipliers3():
    return [lambda x, i_2=i: i_2 * x for i in range(3)]

functions = [multipliers, multipliers1, multipliers2, multipliers3]

for foo in functions:
    print([m(1) for m in foo()])