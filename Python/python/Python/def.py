# Тема : Ачкыч соз def функциялары (Именованные функция)
# python догу функция аргументерди алып, маанини кайтарган объект. функция адатта def оператору менен 
# аныкталат.

# Аты жок функциясынын синтаксис багыты!
# Биринчи биз def деген ачкыч созун жазып алабыз, андан сон 
# функцмяга ат беребиз, эскертуу функцмясынын аты цифрадан же мааниси 
# жок создон турбаш керек. Фунйиянын эн маанилуу жери биз ага ат беребиз!

# def func():
#     print('Hello Python')


# func()

# Эн жонокой функцияны аныктайлы:
# def name():
#     print('Салам!')
    
# name()

# name()

# Практика

# def ins (a, b):
#     print(a - b)
#     # a жана b - бул жерде параметр болуп эсептелинет

#     ins(1, 2)
    # Чакырылып жаткан функциянын ичиндеги элементтер алар аргумент деп аталат.

# def send_email(from_name):
#     """Данная функция выводит общии текст"""
#     text = f"""Уважаемый...!
#     вы приглашены на собесодование в Банке РСК
#     время 14:00, ждем вас!
#     С удоволствием Банк {from_name}!"""
#     print(text)


# send_email('РСК')

# Кашанын ичинде бул параметр!

# def post(name, msg):
#     print("салам" + name, msg)

# post('Актан', 'Кандайсын?')



# Под тема: Оператор звездочка

# Оператор «звёздочка»!
# Этот оператор позволяет «распаковывать» объекты, внутри которых хранятся некие элементы.

# Пример:
# a = [1,2,3]
# b = [*a, 4,5,6]

# print(b) # [1,2,3,4,5,6]
# # Тут берётся содержимое списка a, распаковывается, и помещается в список b.

# lst = [1, 2, 3]
# set = {*lst}
# print(type(set))




# *args / kwargs

# *args — это сокращение от «arguments» (аргументы),
#  а **kwargs — сокращение от «keyword arguments» (именованные аргументы).
# В Python можно передать переменное количество аргументов двумя способами:

#     *args для неименованных аргументов;
#     **kwargs для именованных аргументов.

# Мы используем *args и **kwargs в качестве аргумента, когда заранее не известно, 
# сколько значений мы хотим передать функции.

# Как было сказано, *args нужен, когда мы хотим передать неизвестное количество неименованных аргументов.
#  Если поставить * перед именем, это имя будет принимать не один аргумент, а несколько.
#  Аргументы передаются как кортеж и доступны внутри функции под тем же именем, что и имя параметра, только без *.
#  Например:

# def adder(*nums):
#     sum = 0

#     for n in nums:
#         sum += n

#     print("Sum: ", sum)

# adder(3, 5)
# adder(4, 5, 6, 7)
# adder(1, 2, 3, 5, 6)

# Здесь мы использовали *nums в качестве параметра, который позволяет передавать 
# переменное количество аргументов в функцию adder().
#  Внутри функции мы проходимся в цикле по этим аргументам, чтобы найти их сумму, и выводим результат


# **kwargs

# По аналогии с *args мы используем **kwargs для передачи переменного количества именованных аргументов.
#  Схоже с *args, если поставить  перед именем, это имя будет принимать любое количество именованных аргументов.
#  Кортеж/словарь из нескольких переданных аргументов будет доступен под этим именем. 
# Например:

def intro(**data):
    print("\nData type of argument: ",type(data))

    for key, value in data.items():
        print("{} is {}".format(key, value))

intro(Firstname="Sita", Lastname="Sharma", Age=22, Phone=1234567890)
intro(Firstname="John", Lastname="Wood", Email="johnwood@nomail.com", Country="Wakanda", Age=25, Phone=9876543210)


# Что нужно запомнить:

#*args и **kwargs — специальный синтаксис, позволяющий передавать в функцию переменное количество аргументов.
#При этом, совсем не обязательно использовать имена аргументов args и kwargs;
#*args используется для неименованных аргументов, с которыми можно работать как со списком;
#**kwargs используется для именованных аргументов, с которыми можно работать как со словарём;
# если вы хотите использовать и *args, и **kwargs, то это делается так: func(fargs, *args, **kwargs), 
# порядок следования аргументов важен;
