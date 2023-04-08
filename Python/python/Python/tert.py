# # Цикл while
# # b = 1
# # while b < 6:
# #   print(b)
# #   b += 1

# #   Заявление о перерыве
# i = 1
# while i < 6:
#   print(i)
#   if i == 3:
#     break
#   i += 1

# # Заявление о продолжении
# i = 0
# while i < 6:
#   i += 1
#   if i == 3:
#     continue
#   print(i)

# # Оператор else
# i = 1
# while i < 6:
#   print(i)
#   i += 1
# else:
#   print("i is no longer less than 6")

# # Python для циклов
# fruits = ["томас", "азирет", "таалай"]
# for x in fruits:
#   print(x)

# # Перебор строки
# for x in "banana":
#   print(x)
  
# #   Заявление о перерыве
# fruits = ["apple", "banana", "cherry"]
# for x in fruits:
#   print(x)
#   if x == "banana":
#     break

# # Функция диапазона()

# for x in range(6):
#   print(x)
# # Еще в цикле For
# for x in range(6):
#   print(x)
# else:
#   print("Finally finished!")

# # Вложенные циклы
# adj = ["red", "big", "tasty"]
# fruits = ["apple", "banana", "cherry"]

# for x in adj:
#   for y in fruits:
#     print(x, y)

# # Заявление о пропуске
# for x in [0, 1, 2]:
#   pass

# # Создание функции
# def my_function():
#   print("Hello from a function")

# # Вызов функции
# def my_function():
#   print("Hello from a function")

# my_function()

# # Аргументы
# def my_function(fname):
#   print(fname + " Refsnes")

# my_function("Emil")
# my_function("Tobias")
# my_function("Linus")

# # Количество аргументов
# def my_function(fname, lname):
#   print(fname + " " + lname)

# my_function("Emil", "Refsnes")


# # Произвольные аргументы, *args
# def my_function(*kids):
#   print("The youngest child is " + kids[2])

# my_function("Emil", "Tobias", "Linus")

# # Аргументы ключевых слов
# def my_function(child3, child2, child1):
#   print("The youngest child is " + child3)

# my_function(child1 = "Emil", child2 = "Tobias", child3 = "Linus")

# # Произвольные аргументы ключевого слова, **kwargs
# def my_function(**kid):
#   print("His last name is " + kid["lname"])

# my_function(fname = "Tobias", lname = "Refsnes")

# Значение параметра по умолчанию
def my_function(ago = "76"):
  print("I am ago " + ago)

my_function("32")
my_function("36")
my_function("94")
my_function("65")

# # Передача списка в качестве аргумента
# def my_function(food):
#   for x in food:
#     print(x)

# fruits = ["apple", "banana", "cherry"]

# my_function(fruits)
# # Возвращаемые значения
# def my_function(x):
#   return 5 * x

# print(my_function(3))
# print(my_function(5))
# print(my_function(9))

# # Заявление о пропуске
# def myfunction():
#   pass

# # Рекурсия
# def tri_recursion(k):
#   if(k > 0):
#     result = k + tri_recursion(k - 1)
#     print(result)
#   else:
#     result = 0
#   return result

# print("\n\nRecursion Example Results")
# tri_recursion(6)

# # Python лямбда
# x = lambda a : a + 10
# print(x(5))

# # Зачем использовать лямбда-функции?
# def myfunc(n):
#   return lambda a : a * n

# mydoubler = myfunc(2)

# print(mydoubler(11))

# Итера

