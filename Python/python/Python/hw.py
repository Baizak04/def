


# V if -  если , else - еще,  while - пока, 
# for
#1)
# languages = ["C", "C++", "Perl", "Python"]
# for x in languages:
#     print(x)

#2)
# a = [0,1,1,2,3,5,8,13,21]
# for i in range(len(a)):
#     print(i,a[i])

#3)
# language = ['Python', 'C++', 'PHP', 'Java']
# for c, value in enumerate(language, 1):
#     print(c, value)

# 5)
# for i in range(1, 20):
#     print(i)
# 6)
# for i in range(3):
#     print("Hello World!")
# 7)
# b = (1,12,4,4,7,)
# for i in b: 
#     print(b) 


# 7)
# for a in range(3):
#     print(a)

# 8)
# for c in range(5, 13, 3):
#     print(c)

# 9)
# o = [1, 2, 3, 4] # внешний цикл
# n = [5, 6, 7, 8] # вложенный (внутренний) цикл
# for i in o:
#     for j in n:
#        print ('i=', i, 'j=', j)
# # 10)
# lst = [1,3,5,1,2]
# for i in lst:
#     print(i  2)
# 11)
# for i in (0, 1, 2, 3, 4):
#     print(i)
#     if i == 3:
#         break
# 12)
# for i in (0, 1, 2, 3, 4, 5):
#    if i == 2 or i == 4:
#      continue
#    print(i)
# # 13)
# for index, item in enumerate(['one', 'two', 'three', 'four']):
#     print(index, '*', item)
# 14)
# for i in range(2):
#     print(i)
#     if i == 1:
#         break
# else:
#     print('')
# # 15)
# d = {"a": 1, "b": 2, "c": 3}
# for key in d:
#    print(d)
# 16)



# Функция range()
# Достаточно часто при разработке программ необходимо получить 
# последовательность (диапазон) целых чисел:
# Для решения этой задачи в Python предусмотрена функция range(), создающая 
# последовательность (диапазон) чисел. В качестве аргументов функция принимает: 
# начальное значение диапазона (по умолчанию 0), конечное значение (не включительно) и 
# шаг (по умолчанию 1). Если вызвать функцию, то результата мы не увидим:

# 1)
# for i in range(0, 10, 1):                 #range - диапозон
#  print(i, end=' ')
#  2)
# for i in range(10):
#    print(i, end=' ')
# 3)
# for i in range(10):
#    print(i, end='number ')
# 4)
# for i in range(2, 20, 2):
#     print(i, end=' ')
# 5)
# for i in range(20, 2, -2):
#     print(i, end=' ')

# 6)
# t=0
# for i in range(1, 101):
#     t=t+i
#     print(t)
# 7)
# a = list(range(10))
# print(a)
# 8) 
# b = sum(list(range(1, 101)))
# print(b)
# 9)
# t = list(range(2, 10, 2))
# print(t)
# 10)
# lst = [4, 10, 5, -1.9]
# print (lst)
# for i in range(len(lst)):
#     lst [i]=lst [i] * 2
# print (lst)
# 11)
# a = list(range(1, 15))
# print(a)
# 12)
# a = [i for i in range(1,15)]
# print(a)
# 13)
# a = []
# for i in range(1,15):
#     a.append(i)
#     print(a)
# 14)
# a = [i**2 for i in range(1,15)]
# print(a)
# 15)
# a = [i**2 for i in range(1,15)if i!=4]
# print(a)
# 16)
# a = [2, -2, 4, -4, 7, 5]
# b = [i**2 for i in a]
# print(b)
# 17)
# c = [c*3 for c in 'list' if c != 'i']
# print(c)
# 18)
# a = ['вауу'] 
# n = int(input('число:')) 
# for i in range(n): 
#     new_element = int(input()) 
#     a.append(new_element)
# print(a)
# 19)
# p = { x * x for x in range(-9, 10) } 
# print(p)
# lst = []
# for i in range(2,4):
#  print("lst at %d contains %s" % (i, lst[i]))



# 2.while - пока
# Если заранее количество повторений цикла неизвестно, то применяется другая 
# конструкция, которая называется циклом while. при создании программ не всегда известно, сколько раз придется повторить заданный набор действий. Для этоого есть особый тип циклов с условием
# 1)
# while True:
#     print('! ')
# 2)
# i = 0 
# while i < 10:
#     i += 1
#     print(i)

# 3)
# r = 3
# while r > 0:
#     print(r)
#     r = r -1
# 4)
# while True:
#    text = input("Введите число или стоп для выхода: ")
#    if text == "стоп":
#      print("Выход из программы! До встречи!")
#      break 
#    elif text == '1':
#      print("Число 1")
#    else:
#      print("Что это?!")
# # 5)
# c = 1
# while c <= 5:
#     print(c)
#     c += 1
# 6)
# n = int(input( 'Сколько факториалов будем суммировать? '))
# i = 2
# p = 1 
# while i <= n:
#     p = p * i
#     i = i + 1
# print(p)

# 7)
# number = 0
# while number < 5:
#     print("красавчик!")
#     number = number + 1
# 8)
# number = 0
# while number < 5:
#     if number == 2:
#         print("продолжать!")
#         number += 1
#
# continue
#     print("молодец!")
#     number +=1

# 9)
# a, b = 0,1
# while a < 10:
#     print(a)
    # a , b = b, a+b
# 10)
# n = int(input("Введите число"))

# i = 1
# fact = 1
# while i <= n:
#     fact *= i
#     i += 1
# print("факториал", fact)
# 11)
# k = 0
# while k < 10:
#     print("салам")
#     k += 1
# 12)
# k = 0
# while k < 10:
#     print("салам")
#     k = 1
# 13)
# n = int(input("Введите"))
# k = 0
# while n != k:
#     print('привет')
#     k += 1
# 14)
# name = input("введите ваша имя: ")
# while name =='':
#     print("Вы не ввели свое имя")
# else:
#     print(f"привет {name}")
# 15)
# age = int(input("Введите ваше возраст: "))

# while age < 0:
#     print("Возраст не может быть отрицательным")
#     age = int(input("ваш возраст: "))
# print(f"вам {age} год")
# 16)
# p = "\n Пожалуйста, введите название города, который вы посетили:"
# p += "\n(Введите 'guit', когда вы закончите.) "
# while True:
#    city = input(p)
#    if city == 'quit':
#       break
#    else:
#      print(f"я был в {city.title()}!")
# 17)
# u_users = ['Aziret', 'Mairambek', 'Baizak']
# c_users = []
# while u_users:
#   c_user = u_users.pop()
#   print(f"Проверка пользователя: {c_user.title()}")
#   c_users.append(c_user)
#   print("\n Следующие пользователи были подтверждены:")
#   for c_user in c_users:
#     print(c_user.title())
# 18)
# x = int(input("Введите целое число (0 для выхода): "))
# while x != 0:
#   if x > 0:
#     print("Это положительное число.")
#   else:
#     print("Это отрицательное число.")
#     x = int(input("Введите целое число (0 для выхода): "))
# 19)
# message = str(input("Введите сообщение (оставьте его пустым для выхода): "))
# while message != "":
#   n = int(input("Сколько раз повторить сообщение? "))
#   for i in range(n):
#     print(message)
# 20)
# my_letters = ['a', 'b', 'c'] 
# i = 0 
# while i < len(my_letters):
#   print(my_letters[i])
#   i += 1
#   for i in range(len(my_letters)):
    # print(my_letters[i])
# # 21)
# num = int(input("Введите:"))
# while num < 1 or num > 100:
#     print(f" {num} не действует")
#     num = int(input("Введите"))

# print(f" ваш номер {num}")
# while True:
#    print("\nПожалуйста напишите имя:")
#    f_name = input("имя: ")
#    l_name = input("фамилия: ")
#    formatted_name = formatted_name(f_name, l_name)
#    print(f"\nздраствуйте, {formatted_name}!")
# 22)
# i = 0
# while i < 0:
#    a = int(input("Сколько продукты для магазина:"))
#    b = int(input("Сколько продукты для магазина:"))
#    print(a+b)
#    i += 3
#    print("Сколько бананов и ананасов для магазина?")
#    a = int(input("Сколько бананов:"))
#    b = int(input("Сколько ананасов:"))
#    print("Всего", a+b, "шт фрукты.")
#    print("Сколько конфет и печенье для магазина?")
#    a = int(input("Сколько конфет:"))
#    b = int(input("Сколько печенье:"))
#    print("Всего", a+b, "шт сладости.")
#    print("Сколько Coca Cola и  Pepsi для магазина?")
#    a = int(input("Сколько Coca Cola:"))
#    b = int(input("сколько Pepsi:"))
#    print("Всего", a+b, "шт напитков.")
# 23)
# a = 10
# while True:
#    a = a-1
#    print(a)
#    if a<7:
#      break
# print('сделанный.')





    
# if                                                    #if - если              else  -  еще
# 1)
# if 0:
#     print("True")
# else:
#     print("False")
# 2)
# a = 10
# if a == 10:
#     print("a = 10")
# elif a < 100:
#     print("a < 10")
# else:
#     print("a > 100")
# 3)
# x = int(input("Введите целое число: "))
# if x == 2 or x == 4 or x == 6 or x == 8 or x == 12:
#  print("Это одно из первых пяти простых чисел.")
# else:
#  print("Это не одно из первых пяти простых чисел.")
# 4)
# number = int(input("Введите число: "))

# if number > 10:
#     print("Число больше 10")
# if number < 10:
#     print("Число слишком кичинекей экен 10 ")
# 5)
# number = int(input("Введите число: "))
# if number > 10:
#     print("первая строка")
#     print("вторая строка")
#     print("третья строка")

# # print("Выполняется каждый раз, когда вы запускаете программу")
# print("Конец мультфилма")
# # 6)
# b = ['andrew', 'carolina', 'david']
# user = 'akul'
# if user not in b:
#     print(f"{user.title()}, Ваууу самое красивое имя.")
# 7)
# age = 8
# if age >= 18:
#     print("Вы взрослые чтобы голосовать!")
# if age <= 18:
#     print("Вы не достаточно взрослый чтобы голосовать")
# 8)
# age = 17
# if age >= 18:
#     print("Вы взрослые, чтобы голосовать!")
#     print("Вы уже зарегистрировались для голосования?")
# else:
#     print("Извините, вы слишком молодые, чтобы голосовать.")
#     print("Пожалуйста, зарегистрируйтесь для голосования, как только вам исполнится 18 лет!")
# # 9)
# name = str(input('Ваше имя: '))
# print(f"Добро пожаловать!  {name} На наш игровой площад Sky Park")

# age = int(input('Вам сколько лет!: '))
# print(f"Вауу {age} вы еще молодой")

# if age < 4:
#     price = 0
#     print("младше 4 лет вход бесплатный 0$.")
#     print(f"Стоимость вашего входа \n {price}$.")
#     print("Хорошего вам дня")
# elif age < 18:
#     price = 25
#     print("от 4 до 18 лет билет стоит . 25$.")
#     print(f"Стоимость вашего входа \n {price}$.")
#     print("Хорошего вам дня")
# else:
#     age > 18
#     price = 50
#     print("от 18 лет и старше билет стоит 40$.")
#     print(f"Стоимость вашего входа \n {price}.$")
#     print("Хорошего вам дня")
# # # )



# # 10)
# n = 10
# if n > 10:
#     print("n больше чем 10")
# if n < 10:
#     print("n меньше чем ты думаль")
# if n == 10:
#     print('n они  ровны')
# 11)
# radius = int(input("Введите радиус: "))

# if radius >= 0:
#     print("Длина окружности = ",  2  *  3.14  *  radius)
#     print("Площадь = ", 3.14 * radius  2)
#     print("это радиус длины и площады")
# else:
#     print("please, введите положительное число")
# 12)
# password = input("Введите пароль: ")
# if password == "Акыл агай  красавчик":
#     print("Добро пожаловать ваш персональный акк")
# if password == "эркек болгула":
#     print("все правильно: /n точно эркек болом")
# else:
#     print("Доступ запрещен жаль не знаешь пароль")
# 13)
# g = int(input("Введите текущий лимит: "))
# p = int(input("Введите кредитный рейтинг: "))

# if p > 60:
#         if g > 150:
#             print("Поздравляем, вам выдан кредит")
# else:
#     print("Извините, вы не имеете права на кредит")
# 14)
# score = int(input("Введите вашу оценку: "))

# if score >= 95:
#     print("Ваауууу Отлично! Ваша оценка 5")
# elif score >= 86:
#     print("Здорово! Ваша оценка - 4")
# elif score >= 70:
#     print("так себе! Ваша оценка - 3")
# elif score >= 63:
#     print("Ваша оценка - 2. эркек бол.")
# else:
#     print("Вы не сдали экзамен позор")


# 15)
# n = float(input("Введите число: "))
# if n == 0:
#  result = "Введен ноль"
# if n != 0:
#  result = "Введен не ноль"
# print(result)
# 16)
# num = float(input("Введите число: "))
# if num > 0:
#  result = "Введено положительное число"
# elif num < 110:
#  result = "Введено отрицательное число"
# else:
#  result = "Введен ноль"
# print(result)
# 17)
# old = int(input('Ваш возраст: '))
# print('Рекомендовано:', end=' ')
# if 0 <= old < 18:
#   print(" маленький")
 
# if 18 <= old < 30:
#   print("молодой")
 
# if 30 <= old < 60:
#   print("средный возраст")
# if 60 <= old < 150:
#   print("старый")
# 18)
# season = int(input('Времени года: '))

# if 12 <= season < 2:
#   print('Сезон:', ' Зима')
 
# if 3 <= season < 5:
#   print('Сезон:', 'Весна ')
 
# if 6 <= season < 9:
#   print('Сезон:', 'Лето ')
# if 10 <= season < 12:
#   print('Сезон:', 'Осень')
# 19)


# def

# 1)
# def greet_user(ok):
#   text = f"""Выводит простое приветствие {ok}."""
#   print(text)

# greet_user("Hello")
# 2)
# def greet_user(username):
#   print(f"Hello, {username.title()}!")
 
# greet_user('jesse')
# 3)
# def display_massage(massagetext):
#   print(f"Hello Акылай агай, {massagetext.title()}")

# # display_massage('\n салам')
# 4)
# def favorite_book(book):
#     print(f"Мой самый любимый книга {book.title()}!")
    
# favorite_book('самурай без меча')
# 5)
# def describe_pet(animal_type, pet_name):
#   print(f"\nУ меня есть {animal_type}.")
#   print(f"Моего {animal_type} зовут {pet_name.title()}.")
 
# describe_pet('хомяка', 'кери')
# 6)
# def describe_pet(animal_type, pet_name):
#   print(f"\nУ меня есть {animal_type}.")
#   print(f"Моего {animal_type} зовут {pet_name.title()}.")
 
# describe_pet('Хомяк', 'кери')
# describe_pet('собака', 'рекс')
# 7)
# def describe_pet(pet_name, animal_type='собака'):
#   print(f"\nУ меня есть {animal_type}.")
#   print(f"моего {animal_type} зовут {pet_name.title()}.")
# describe_pet(pet_name='крутой')
# 8)
# def get_formatted_name(first_name, last_name):
#   full_name = f"{first_name} {last_name}"
#   return full_name.title()
# m = get_formatted_name('baizak', 'nadurbekov')
# h = get_formatted_name('aziret', 'kudurkylov ')
# print(m, h)
# 9)
# def build_person(first_name, last_name):
#   person = {'Имя': first_name, 'Фамилия': last_name}
#   return person
 
# musician = build_person('Байзак', 'Надырбеков')
# print(musician)
# # 10)
# # def m_pizza(*toppings):             #toppings - начинка
# #     print(toppings)
 
# # m_pizza('рецепты')
# # m_pizza('колбаса','помидор', 'доплнение сыр')
# # 11)
# def m_pizza(*toppings):
#     print("\nПриготовление пиццы со следующими начинками:")
#     for topping in toppings:
#         print(f"- {topping}")
# m_pizza('рецепты')
# m_pizza('колбаса','помидор', 'доплнение сыр')
# 12)
# def build_profile(first, last, user_info):
#    user_info['имя'] = first
#    user_info['фамилия'] = last
#    return user_info
# user_profile = build_profile('Байзак', 'Надырбеков',location='Бишкек',field='что-то')
# print(user_profile)
# # 13)
# def rectangle():                                                            #rectangle - прямоугольник
#     a = float(input("Ширина: "))
#     b = float(input("Высота: "))
#     print("Площадь: %.2f" % (a*b))
 
# def triangle():
#     a = float(input("Основание: "))
#     h = float(input("Высота: "))
#     print("Площадь: %.2f" % (0.5 * a * h))
 
# def circle():                                                                 #circle - круг
#     r = float(input("Радиус: "))
#     print("Площадь: %.2f" % (3.14 * r**2))
# figure = input("1-прямоугольник, 2-треугольник, 3-круг: ")
# if figure == '1':
#   rectangle()
# elif figure == '2':
#   triangle()
# elif figure == '3':
#   circle()
# else:
#   print("Ошибка ввода")
# 14)






# asd = [10,9,8,7,6,5,4,3,2,1]
# for i in asd:
#     print(type(i))






















# >>> a= range(10)
# >>> a
# range(0, 10)
# >>> list(a)
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]












# a = ["*", "", "***" , "****" , "" "***", "****","****","***","","*" ]
# for j in a:
#   print(j)

# for i in range(8):
#    j=8
#    if i>3:
#       print('*' * (j-i))
#    else:
#       print('*' * i)










# =/==/=/=/=/=//=/==/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=//=/=/=/=/=/=/=//==/=/=/=/=

# дата:19-февраль


# # 1)

# def send_mail():
#     text = "салам python"
#     print(text)


# send_mail()
# send_mail()

# # 2)

# def b_mail(from_name, old):
#     text = f"'салам менин атым {from_name} жашым {old}'"
#     print(text)


# b_mail("таалай", 18)

# 3)

# def ex_e(y):
#     print('Квадрат числа', 'x' '=', y**2)

# ex_e(5)    

# 4)

# def di(a):
#     if a%2==0:
#         print(a,'четный')
#     else:
#         print(a,'не четное')

# for i in range(1,11):
#     di(i)

# 5)

# def si(k):
#     return k**2


# a = si(si(7))
# print(a)

# 6)
 
# def ev(a):
#     if a%2==0:
#         return True
#     return False

    
    
# for i in range(1,10):
#     print(i,ev(i))

# 7)

# def sl(a,b):
#     return a*b, 2*(a+b)


# print(sl(3,6))

# 8)

# x = int(input("1 число: "))
# y = int(input("2 число: "))

# def sum(a, b):
#     return a + b 

# z = sum(x,y)
# print(z)

# =============================================

# for, while

# 1)

# i = 0
# while i < 10:
#     print(i)
#     i += 1

# 2)


# =/=/=/=/=/=/=/=/==/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=//==/=/=/=/=/==/=/=/=/=/=/=/=//==/=/=/=/=/=/=/=/=/

# дата:21-февраль


# 1)

# def greet_r(one_name, two_name):
#     result = f'кандай {one_name}, Сен {two_name} '
#     print(result)

# greet_r(one_name='кто-то', two_name='кто-то?')

# 2)

# def ru():
#     print("кандай ")
#     print("сен ")


# ru()
# ru()
# ru()

# 3)

# def add_num(n1, n2,):
#     result = n1 * n2
#     print(f"Ваш число", result)

# num1 = 100
# num2 = 67
# add_num(num1, num2)

# ====================================================================

# if, elif,else.


# 1)

# a = 4
# b = 2
# if a < b:
#     print("a меньше, чем b")
# else:
#     print("c либо больше, чем d либо равнется d")

# 2)

# e = 3
# b = 2
# if e < b:
#     print("e меньше,чем b")
# elif e == b:
#     print("e равняется b")
# else:
#     print("e либо больше,чем f либо равняется f")

# 3)

# s = 7
# g = 8
# if s < g:
#     print("s меньше, чем g")
# else:
#     if s == g:
#         print("s равняется g")
#     else:
#         print("s больше,чем g")

# 4)

# name = "Tomas"
# height = 2
# weight = 80

# bmi = weight / (height ** 2)
# print("массы тело:" + str(bmi))

# if bmi < 25:
#     print("У" +  name + "нет лишнего веса")
# else:
#     print("у"  +  name + "есть лишний вес")

# 5)

# ro = int(input("введите число: "))
# if ro == 1:
#     print('1 doroga')
# elif ro == 2:
#     print("2 doroga")
# elif ro ==3:
#     print('3 doroga')
# else:
#     print('error')

# 6)

# day = int(input("Введите день: "))
# if day == 1:
#     print('monday')
# elif day==2:
#     print('tuesday')
# elif day==3:
#     print('wednesday')
# elif day==4:
#     print('thursday')
# elif day==5:
#     print('friday')
# elif day==6:
#     print('saturday')
# elif day==7:
#     print('sunday')
# else:
#     print('Такой день недели нету')

# 7)

# a = int(input("Введите цивру: "))
# if a < 0 or a >=10000:
#     print('error')
# elif a<10:
#     print('1 цивра')
# elif a<100:
#     print('2 цивра')
# elif a<1000:
#     print('3 цивра')
# elif a<10000:
#     print('4 цивра')

# 8)

# age = 22
# if age >= 18:
#     message = "eligible"
# else:
#     message = 'not eligible'

# 9)

# s = int(input("введите вашу оценку: "))

# if s >= 90:
#     print("Ваша оценка А (супер)")
# elif s >= 70:
#     print("Ваша оценка B (хорошо)")
# elif s >= 50:
#     print("Ваша оценка B (средный)")
# elif s >= 30:
#     print("Ваша оценка B (низкий)")
# else:
#     print("Вы не сдали экзамен")



# =/=/=/=/=/=/=/=/=/==/=/=//=/==/=//==/=/=/=/=/=/=/=/=/=/==/=/=/=/==/=/=/=/=/=/=/==//==/=/=/=/=/=/==/=//=/==/=/=//==/=/=/=/=/

# дата: 22-февраль

# if, elif,else

# 1)

# money = 100
# bilet = 90
# if money>=bilet:
#     print("Урааа!")
#     print("Я иду в кино")
# print("Пора идти домой")

# 2)

# a = int(input("Введите число: "))
# t = int(input("ВВедите второе число: "))
# if t>a:
#     a,t = t,a
# print(a,t)

# 3)

# a = int(input("Введите число: "))

# if a>100:
#     print(f'Введеное число{a} > 100')
# elif a > 50 and a <100:
#     print(f'Введеное число {a}находится в предалах от 50 до 100')
# elif a ==100:
#     print(f'Введеное число{a} = 100')
# else:
#     print(f'Введеное число {a} <= 50')


# while 

# 1)

# i = 0
# while i < 3:
#     print("Akul agai")
    # i = i+1    

# 2)

# s = 0
# a = 0
# while a < 1000:
#     a = int(input("Введите число: "))
#     s = s + a
# print(s)

# 3)

# v = [{}], [{}]

# for i in v:
#     print(bool(i), end=" ")


# =/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/==/=/=/=/=/=/=//=

# дата:23-февраль

# if 

# 1)

# n = -3
# if n < 0:
#     n = -n

# print(n)

# 2)

# m = [3, 3, 4, 4, 4]

# if 4 in m:
#     print("Студент будет отчислен!")
# else:
#     print("Студент успешно сдал сессию!")

# 3)

# x = int(input("Введите число: "))

# if x < 0:
#     print("x - отрицательное число")
# else:
#     print("x - не отрицательное число")


# =//=/=/=/=/=/=/=/=/==/=/=/=//=/=/=/=/=/=/=/=/==/=/=/=/=/

# data:23-февраль


# 1)

# w = "scrin"
# for i in w:
#     print(i)

# 2)

# count = 0
# w = "hello, lllll"
# for i in w:
#     if i == "l":
#         count +=1
# print("count", count)

# 3)

# i = 5
# while i < 15:
#     print(i)
#     i += 6

# 4)

# for i in "{{{{}}{[[]]]]}}}":
#     if i == "{":
#         f = True
#         break
# else:
#     f = False

# print(f)


# ==//=/=/=/=/=/=/=/=/==/=/=/=/=/=/=/=/=/=/=/=/=/=

# 27 - февраль

# for  

# 1)

# for i in range(1, 6):
#     for j in range(5,22):
#         print("%4d" % (i*j), end='')
#     print()

# 2)











































































