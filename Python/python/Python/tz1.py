

# set = {1, 2, 3, 4, 5, 'python'}
# print(1 in set)
# s = input('Введите первую цифру: ')
# a = input('введите вторую цивру')
# print(s, w,)



# строка(str)
# список(list)
# словарь(dict)
# Множеста(set)
# format(f) - срез (slice)
# Условные операторы(if, elif, else)
# for r in "aplle":
#   print(r)
# # for i in range(1, 9):
# #     for j in range(9, i, -1):
# #         print(i, end="")
# #     print()

# # # user = ("baizak", 18, True)
# # # name, age, admin = user
# # # print(name)
# # # print(age)

# # # def my_fn(a, b): #функция имя параметр
# # #     return #возврат резултата


# # start = "сб" # день недели
# # days = 30 # количество дней в этом месяце
 
# # day = 1
# # start = {"пн": 1, "вт": 2, "ср": 3, "чт": 4, "пт": 5, "сб": 6, "вс": 7}[start]
 
# # print("Пн  Вт  Ср  Чт  Пт  Сб  Вс")
# # print("-   "*(start-1), end="")
# # for week in range(start, 8):
# #     print(str(day) + "   ", end="")
# #     day += 1
# # print()
 
# # for j in range((days+start-2)//7):
# #     for week in range(7):
# #         if day < 10:
# #             print(str(day) + "   ", end="")
# #         elif day <= days:
# #             print(str(day) + "  ", end="")
# #         else:
# #             print("-   ", end="")
# #         day += 1
# #     print()

# import math
# k = int(input())
# d = int(input())
# c = math.ceil(d / 7)
# a = []
# n = 1
# for r in range(c):
#     a.append([])
#     for c in range(7):
#         a[r].append(n)
#         n += 1
# for r in a:
#     print(r)


k, d = int(input()), int(input())
 
calendar = [[None] * k]
 
for day in range(1, d + 1):
    if len(calendar[-1]) == 7:
        calendar.append([])
    calendar[-1].append(day)
 
print("Пн Вт Ср Чт Пт Сб Вс")
for week in calendar:
    print(*[f"{('  ' if day is None else f'{day:0>2}')}" for day in week])

