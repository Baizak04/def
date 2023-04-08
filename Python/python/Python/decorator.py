# Декораторы!
# Декораторы - важная часть Python. Если коротко: они являются функциями, которые изменяют работу других функций. Они помогают делать код короче и более "питонистичным". 
# Для начала краткая ретроспектива функций в Python:

# def hi(name="Джон"):
#    print("Привет " + name) 

# hi() # Привет Джон
# print(hi())
# f = hi()
# print(f)

# hi()
# res = hi()
# # print(res)

# Мы можем присвоить функцию переменной:
# greet = hi

# Мы не используем здесь скобки, поскольку наша задача не вызвать функцию,
# а передать ее объект переменной, теперь попробуем запустить!

# print(greet()) # Привет Джон

# Определение функций внутри функций!
# Итак, это были основы работы с функциями. Теперь продвинемся на шаг дальше. В Python разрешено объявлять функции внутри других функций:

# def hi(name='Ray'):
#     print("Мы внутри функции hi()")

#     def inner1():
#         return "Мы внутри функции inner1()"

#     def inner2():
#         return "Мы внутри функции inner2()"

#     print(inner1())
#     print(inner2())

# hi()



# def posts():
#     def inner():
#         print('Привет из иннера')

#     return inner()

# posts()

# Вывод: Мы внутри функции hi()
#        Мы внутри функции ineer()
#        Мы внутри функции welcome()
#        Мы внутри функции hi()

# Пример демонстрирует, что при вызове hi() вызываются также функции inner() и welcome(),
# Кроме того, две последние функции недоступны извне hi():

# Если вызывим функцию inner()
# inner() # Вывод NameError: name 'inner' is not defaind!


# Теперь мы знаем, что возможно определять функции внутри других функций. 
# Другими словами: мы можем создавать вложенные функции.
# Теперь вам нужно познакомиться с еще одной возможностью функций: возвращать другие функции.


# Теперь рассмотрим декоратор
# Простой пример:

# def property(func):
#     def wrapper():
#         print('Привет')
#         func()
#         print('До встречи!')
#     return wrapper



# @property #-- Декоратор
# def links():
#     print(''' Ссылки на социальные сети: 
#     ВКонтакете: https....
#     Инстаграм: https....
#     Телеграм: https....''')

# links()
# def hi(text):
#     text = 'салам\nалейкум'
#     print(text)

# def decorator (func):
# #     def wrapper():
# #         print ("")
# #         func ()
# #         print ("Байзак")
# #     return wrapper 

# # @decorator

# # def func ():
# #     print("Салам ")
# #     print("Алейкум ")


# # func()
# def decorator1(f):
#     def wrapped():
#         return '*****' + f() + '*****'
#     return wrapped
    
# def decorator2(f):
#     def wrapped():
#         return '+++' + f() + '+++'
#     return wrapped
# @decorator1
# @decorator2
# def function():
#     return 'Python 3.8'
# print(function())


# def decorate(func):
#    def wrapped():
#       return 'python'
# #    return wrapped

# # # @decorate
 
# # # def func():
# # #    return 'python hello'
# # # print(func())

# # func()
# def simle_decor(func):
#    def wrapper():
#       func()
#       o = 'Таанышканы кубанычтамын'
#       print(o.upper())
#    return wrapper
# @simle_decor

# def bs():
#    name = input("сиздин атыныз ким: ")


# bs()
# def simle_decor(func):
#    def wrapper():
#       func()
#       o = 'Таанышканы кубанычтамын'
#       print(f'{o.upper()}')
#    return wrapper


# @simle_decor
# def bs():
#    name = input("сиздин атыныз ким: ")

# bs()
# def decor(func):
#    def wrapper():
#       print("это первое сообщения!")
#       func()
#       print("это второе ссобщения!")
#    return wrapper

# def decor2():
#    print("чего смотришь!")
# decor2 = decor(decor2)
# decor2()
