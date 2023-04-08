# Тема: итератор и итерируемый объект!

# итерация (iterable) - это общий термин , который описывает процедуры взятия элементов чего - то по очкредие
# В python за получение итератора отвечает фугкеция oter():

# tuple = ("яблоко" , "банан", "вишня")
# myit = iter(tuple)
# print(next(myit))
# print(next(myit))
# print(next(myit))

# Итерируемый объект (iterables objeekt)  -  это объект, который способен возвращать элементы по одному. кроме того, это оюъект, из которого иожно получить итератор.

# Примеры итеруемых объектов:
# все последовательности: список, строка, кортеж
# словари 
# файлы

# dict = {1 : 'pu', 3: 'ru', 4: 'ty'}
# d = iter(dict)
# print(next(d))
# print(next(d))
# print(next(d))
m = "LIKE"
myit = iter(m)

print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))


# a = 3

# b = eval('a + 2')
# print('b =', b)

# exec('c = a ** 2')
# print('b is', 6)
