

# Задача 1
# Есть список a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89].
# Выведите все элементы, которые меньше 5.
# a =[1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# a = 1
# while a < 5:
#     print(a)
#     if a == 9:
#         break
#     a += 1


# Задача 2
# Выводите все ключи из словаря
# my_dict = {'a':500, 'b':5874, 'c': 560,'d':400, 'e':5874, 'f': 20}.

# my_dict = {'a':500, 'b':5874, 'c': 560,'d':400, 'e':5874, 'f': 20}
# z = my_dict.keys()
# print(z)

# Задача 3
# Напишите проверку на то, является ли строка палиндромом. Палиндром — это слово или фраза, которые одинаково читаются слева направо и справа налево.


# Задача 4
# Выведите первый и последний элемент списка.
# # lst = [1, 2, 3, 4, 5]
# # print(list[4:])
# # print(list[:1])



# # Задача 5
# # Посчитайте, сколько раз буква о встречается в строке.
# # str = 'Python Software Foundation'
# # print(str.count('o'))

# # Задача 6
# # Выводите Hello world на терминал
# # print('Hello world')

# # Задача 7
# # Напишите все функции которые вы знаете в питоне
# # len 
# # max
# # min 
# # sorted
# # sum

# # Задача 8
# # Выводите все элементы по очереди, используя функцию iter и next
# # mytuple = ('python', 'java', 'php', 'javascript')
# # mytuple = ('python', 'java', 'php', 'javascript')
# # a = iter(mytuple)

# # print(next(a))
# # print(next(a))
# # print(next(a))
# # print(next(a))
# # Задача 9
# # Напишите простую функцию и сложите два числа
# # t = lambda a, b: a * b
# # print(t(5, 6))

# # Задача 10
# # Напишите простой калькулятор
# # a = int(input('Введите первое число: '))
# # b = int(input('Введите второе число: '))
# # c = str(input('Выберите действие * , + , - , % : '))
# # if c == '+':
# #    print('Сложение' ,  a + b)
# # elif c == '-':
# #    print('Вычитание' , a - b)
# # elif c == '%':
# #    print('Деление' , a % b)
# # elif c  == '*':
# #    print('Умножение' , a * b)
# # else:
# #    print('Неизвестная операция') 

# # Задача 11
# # С помощью среза уберите python
# # str = 'language py
# # def decorator (func):
# #     def wrapper():
# #         print ("код до выполнения функцим")
# #         func ()
# #         print ("код который сработал после функции")
# #     return wrapper 
# # def test (func):
# #     def wrapper():
# #         print ("код до выполнения функцим3")
# #         func ()
# #         print ("код который сработал после функции3")
# #     return wrapper 
# # @decorator
# # @test
# # def show ():
# #     print("я обычная функция")
    
# # show ()
# # dec = decorator (show)

# # from collections import deque
# # dq = deque('Baizak')
# # for element in dq:
# #     print(element)
# # from colorama import init
# # from colorama import Fore, Back, Style
# # init()

# # print( Fore.RED)
# # print( Back.RESET )

# # print( Back.GREEN )




# a = float(input('Введите первое число: '))

# b = float(input('Введите второе число: '))
# c = str(input('Выберите действие * , + , - , % : '))
# if c == '+':
#    print('Сложение' ,  a + b)
# elif c == '-':
#     # print( Back.YELLOW )
#     print('Вычитание' , a - b)
# elif c == '%':
#     print('Деление' , a % b)
   
   
# elif c  == '*':
    
#    print('Умножение' , a * b)
# else:
#    print('Неизвестная операция') 

# from colorama import init
# from colorama import Fore, Back, Style
# init()
# print( Back.YELLOW )
# what = input("что делаем? (+, -):" )
# print( Fore.MAGENTA)
# print( Back.GREEN )


# a = float(input("введите первое число"))
# b = float(input("введите второе число"))

# if what == "+":
#     c = a + b
#     print("Резултат:" + str(c))
# elif what == "-":
#     print( Back.BLUE )
#     c = a - b
#     print("Результат" + str(c))
    
# else:
#     print("неверная операция")


# from pyowm import OWM

# owm = OWM('8b78cb6da2d98c5f2540773af280dca0')
# observation = mgr.weather_at_place('London,GB')
# w = observation.weather
# print(w)
# sum = ("1, 1")
# print(sum)

# sum = [1] + [2]
# print = (sum)

# a = ["*", "**", "***" , "****" , "*****"]
# for j in a:
#   print(j)

# for j in range(6):
#   print(j)


# sum = ["*", "**", "***" , "****" , "*****"]
# numer = [""]

# for x in sum:
#   for y in numer:
#     print(x, y)





# 2) cubic power of number
# j = int(input("Введите свой число:"))
# cube = j * j * j
# print("число:" , j)
# print("его куб:" , cube)


# def cube(a):
#   return a * a * a
# a = int(input("Введите число :"))
# j = cube(a)
# print("Куб  {0} является {1}" . format(a, j))

# =========================================================

# 1) palindrome
# def polindrome(x):
#   x1 = ''
#   for i in range(len(x) -1, -1, -1):
#       x1 += x[i]
#   return x == x1
# print(polindrome('233433'))

# d = str(input('Введите слово:'))
# if d == d[:: -1]:
#   print('Является палиндромом!')
# else:
#   print('Не является палиндромом!')
# q = ["a", "b"]    
# w = [1, 2, 3]
# s = [11,22,33]

# for i in q:
#     for j in w:
#         print(i)
#     for m in s:
#         print(i, j, m)


# class MyClass:
#   x = 4

# p= MyClass()
# print(p.x)

# class Person:
#   def __init__(self, where, age):
#     self.where = where
#     self.age = age

# p1 = Person("Bishkek", 36)

# print(p1)

# ============================================

# class Person:
#   def __init__(self, fname, lname):
#     self.firstname = fname
#     self.lastname = lname

#   def printname(self):
#     print(self.firstname, self.lastname)


# x = Person("John", "Doe")
# x.printname()

# ===========================================================
# var = 42
# print(f"{var = }")


# ================================================================

# word = str(input('Введите слово:'))

# print(word[::-1])

# def reverse(s):
#     return s[::-1]
 
# print(reverse('bugun soonun kun!'))

# j1 = int(input('Введите цивру'))

# j2 = 0

# while j1 > 0:
#     number = j1 % 10
#     j1 = j1//10

#     j2 = j2 * 10 + number

# print(j2)

# ==================================================================

# факториал

# from math import*
# k = int(input('Введите число:'))
# a = factorial(k)
# print("факториал", k, "равен", a)

# 2)
# n = int(input())
# d = 1

# for i in range(2, n+1):
#     d *= i
# print(d)

# ================================================
# палиндром
# def palin(s):
#     if len(s) <= 1:
#         return True
#     if s[0] != s[-1]:
#         return False
#     return palin(s[1:-1])
# print(palin('nfn'))

# def rec(x):
#     if x<10:
#         print(x)
#         rec(x+1)
#         print(x)

# rec(1)


# таблица умножения

# for i in range(1, 10):
#     for j in range(1, 10):
#         print("%4d"%(i*j), end = '')
#     print()

# x = int(input())
# y = int(input())

# if x > 0 and y > 0:
#     print(1)
# else:
#     if x < 0

# ==================================================

# Hw

# def test(asd, k):
#     pass
#     return

# k = 3
# s = "привет пайтон"
# test(s, k)
# терминал 
# прите пайтон



# hw:
# 1)
# def check_balanced(s):
#     stack =[]                                                             
#     for char in s:
#         if char in [')(', '}{','][']:
#             stack.append(char)
#         elif char in[')','}', ']']:
#             if not stack:
#                 return False
#             if char == ')' and stack[-1] == '(':
#                 stack.pop()
#         elif char == '}' and stack[-1] == '{':
#             stack.pop()
#         elif char == ']' and stack[-1] == '[':
#             stack.pop()
#         else:
#             return True
#     return False
    
# print(check_balanced("()(){}[]()"))         
# # print(check_balanced("(][}[)[[)("))         


# # 2)
# import re
# def par(input):
#     res = re.findall(r'\(\)|\{\}|\[\]', input())
#     if len(input()) / 2 != len(res):
#         return False
#     else:
#         return True


# #  3)длинна
# a = ['салам', 'Python']
# for w in a:
#     print(w, ':', len(w))
# # 4)
# aa= "jnjn jkn kjn kjn kkkkkkkkkk"

# def len(str):
#     counter = 0
#     while str[counter:]:
#         counter += 1
#     return counter

# str = "салам"
# print(len(str))
# # 5)
# def len(str):
#     counter = 0
#     for i in str:
#         counter += 1
#     return counter
# str = "pwi"
# print(len(str))



# # Функция append() позволяет добавлять в список один новый элемент — например, число, строку или другой список. Функция extend() работает как append(), но в качестве параметра принимает итерируемый объект: список, кортеж или строку. Содержимое этого объекта поэлементно добавляется в другой список


# # Оператор return используется в функциях для возвращения данных после выполнения работы самой функции. В примере выше вызывается функция, которая считает сумму трех переданных аргументов. В конце функция возвращает это значение, поэтому мы можем записать функцию, как присвоение данных к переменной.