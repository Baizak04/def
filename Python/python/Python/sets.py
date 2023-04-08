# тема множества (set)
# множества бул python  тилинде озгоручуу жана ирээтелуучу эмес маалымат, ал мындайча
#  айтканда уникалдуу коллекция элементери деп атасак болот.
# Эскерттуу - множествада элементтер кайталанбайт жана бир калыптада журбогон маалымат. каща белгиси{}

# Словарь & Множестваныны айырмасы:
# Словарь менен множестванын айырмасы бир эле аныктоодо биз словарьга ключ жана элемент берсек 
# ал эми множествага бербейбиз !

# Словарь ---> dict = {1: 'os'}
#  множества ---> set = {1, 2, 3, 'hello'}

# set = {'hello', 3, 9, 9, 5, 5, 5,}
# print(set)


# эскертуу: множествада бир элемент эки жолу кайталанбайт
# мисалы:
        
# dict = {1: 'hello'}
# print(type(dict))
# set = {1: 'os'}
# print(type(set))

# Множестванын операторлору жана мотоддору

# 1) Оператор in - бул оператор множествада биз издеген элемент барбы
# же жоктугун аныктап берет 
# Мисалы:
# set = {1, 2, 3, 4, 5, 'python'}
# print(1 in set) 

# 2) Метод add() - Бул метод множестванын аягына элемент кошуу багытын аткарат
# Мисалы:
# set = {1, 2, 3, 4,}
# set.add(9)
# print(set)

# # 3)метод discard() - бул метод множестванын элементи жок кылат
# set = {1, 67, 'str'}
# set.discard(67)
# print(set)
#  Эскертуу: Индекс аркылуу эмес

# 4)  Метод remove() - Бул метод discard методуна окшош эле кызмат аткарат
# Мисалы:

set = {'ins , 45, 67'}
set.remove(45)
print(set)

# 5) Метод  update() - бул метод множествага эки же уч 
# элемент кошуу багытын аткарат 
# Мисалы:
# ind = {565, 6844}
# ind.update('HELLO , HI')
# print(ind)

# # 6) Функция () - Бул функция множествада канча элемент бар экендигин аныктайт
# # Мисалы:
# set = {13, 44,76, 67}
# print(set, len(set))


# Множестваларды кошуу багыты 
# Метод аркылуу

# a = {1, 2, 3}
# b = {4, 5, 6}
# s = a.union(b)
# print(s)

# Ал эми оператор аркылуу кошуп королу:
# a = {1, 2, 3,}
# b = {4, 5, 6,}
# print(a | b)

# множестваны кемитуу багыты
# a = {5, 6, 7}
# b = {8, 9, 10}
# print(a - b)

# a, b = 1, 2
# print(a, b)

# a, b = b, a
# print(a, b)

# baizak_nadurbekov = [
#     ((1, 2), 3),
#     ((4, 5), 6),
#     ((7, 8), 9),
# ]

# for ((a, b), c) in baizak_nadurbekov:
#     print(a, b, c)

from collections import Counter


print(Counter("test") == Counter("sett"))
