# class Car:
#     model = "Bmw"
#     engine = 1.6

# a1 =Car()
# # a2 = Car()
# class Calculator(object):
#     def __init__(self, brand, model, arg1):
#         self.brand = brand
#         self.model = model
#         self.arg1 = arg1
 
# def __str__(self):
#         return f'{self.brand} {self.model} is ready to work!'
 
# def __add__(self, arg1, other):
#         return self.arg1 + self.arg1
 
# def __sub__(self, arg1, other):
#         return other - self.arg1
 
# def __mul__(self, arg1, other):
#         return other * self.arg1
 
# def __div__(self, arg1, other):
#         return other // self.arg1
#         if __name__ == '__main__':
#             c = Calculator('шарп', 'конопочный', 12)
# print(c.__str__())
# print(c.__add__(12, 12))
# print(c.__sub__(11, 112))
# print(c.__mul__(12, 2))
# print(c.__div__(12, 144))

# class Person:
#         def __init__(self, nationalaty, height):
#                 self.nationalaty = nationalaty
#                 self.height = height
#         def show_details(self):
#                 return self.nationaly, self.height

# Mairambek = Person("Kyrgyz", 1.70)                
# Aziret = Person("Koreec", 1.72)  
# print(Mairambek.show_details())


# # HW2
# class Person:
#         def __init__(self, firsttext, lasttext ) :
#                 self.ftext = firsttext
#                 self.ltext = lasttext
                
#         def printtext(self):
#                 print(self.ftext, self.ltext, )

#                 print(self.ltext, len(self.ltext))
# a = Person ('салам, бугун жакшы','кун!')
# a.printtext()

# class Person:
#         def __init__(self, name, old):
#                 self.__name = name
#                 self.__old = old

#         @property
#         def get_old(self):
#                 return self.__old

#         def set__old(self, old):
#                 self.__old = old

#         old = property()
#         old = old.setter(set__old)
#         old = old.getter(get_old) 


# p = Person('Акыл' , 20)
# print(p.get_old, p.__dict__)


# from string import ascii_letters


# class Person:
#         S_KG = 'Надырбеков Байзак'
#         S_KG_UPPER = S_KG.upper()

#         def __init__(self, fio, old, ps, weight):
#                 self.verify_fio(fio)
#                 self.__fio = fio.split()
#                 self.__old = old
#                 self.__passport = ps
#                 self.__weight = weight

#         @classmethod
#         def verify_fio(cls, fio):
#                 if type(fio) != str:
#                         raise TypeError("Фамилия имя отчество должно быть строкой")

#                 f = fio.split()
#                 if len(f) >= 3:
#                         raise TypeError("Неверный формат ФИО")

#                 letters = ascii_letters + cls.S_KG + cls.S_KG_UPPER
#                 for s in f:
#                         if len(s) < 1:
#                                 raise TypeError("Фамилия имя отчество должен хотя бы один символ ")
#                         if len(s.strip(letters)) != 0:
#                                 raise TypeError("Фамилия имя отчество можно использоватьб только буквенные символы")
        
#         @classmethod
#         def verify_old(cls , w):
#                 if type(w) != float or w < 100:
#                         raise TypeError("Вус должен быть числом от 20 до 120")


#         @classmethod
#         def verify_ps(cls, ps):
#                 if type(ps) != str:
#                         raise TypeError("Паспорт должен быт строкой")

#                 s = ps.split()
#                 if len(s) != 2 or len(s[0]) !=4 or len(s[1]) !=6:
#                         raise TypeError("Неверный формат паспорт")

#                 for p in s:
#                         if not p.isdigit():
#                                 raise TypeError("Серия и номер паспорта должны быть числоми")
                                
#         @property
#         def fio(self):
#                 return self.__fio

#         @property
#         def old(self):
#                 return self.__old
#         @property
#         def weight(self):
#                 return self.__weight

#         @weight.setter
#         def weight(self, weight):
#                 self.verify_weight(weight)
#                 self.__weight = weight

#         @property
#         def passport(self):
#                 return self.__passport

#         @passport.setter 
#         def passport(self, ps):
#                 self.verify_ps(ps)
#                 self.__passport = ps



         



# # p = Person('Надырбеков Байзак', 18, '1293993 282', 53.0)
# # # p.old = 18
# # p.passport = '122337 26776'
# # p.weight = 70
# # print(p.__dict__)


# def prt(n,a):
#     if n==0:
#         return
#     else:
#         print(a,end='')
#         prt(n-1,a)
        
# def foo(s,a):
#     if s==0:
#         return
#     else:
#         prt(s,' ')
#         prt(a,'*')
#         print()
#         foo(s-1,a+2)
        
# foo(12,1)


# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#     def get(self):
#         print(self.name , self.age)
        
# p1 = Person("skm" , 19)
# p1.get()


# class Point:
#     color = 'red'
#     circle = 2

#     def set_coords(self, x, y):
#         self.x = x
#         self.y = y


# pr= Point()
# pr2 = Point()
# pr.set_coords(1, 2)
# pr2.set_coords(10, 20)
# print(pr.__dict__)
# print(pr2.__dict__)


# class Cat:
#     name = None
#     age = None
#     isHappy = None

# cat1 = Cat()
# cat1.name = "bars"
# cat1.age = 1
# cat1.isHappy = True

# cat2 = Cat()
# cat2.name ="jor"
# cat2.age = 3
# cat2.isHappy =  False

# print(cat1.age)
# print(cat2.name)

# class Cat:
#     name = None
#     age = None
#     isHappy = None

#     def set_data(self, name, age, isHappy):
#         self.name = name
#         self.age = age
#         self.isHappy = isHappy

# cat1 =Cat()
# cat1.set_data("bars", 1, True)

# cat2 = Cat()
# cat2.set_data("jor", 3, False)

# print(cat1.age)
# print(cat2.name)

# Коллекция__slots__
# ограничения создаемых локальных свойств
# уменьшение занимаемой памяти
# ускорение работы с локальным свойствами

# ==============================================================
# class Animal:
#     def make_noise(self):
#         print('shh')

# class Cat(Animal):
#     def make_noise(self):
#         print('meow')

# class Dog(Animal):
#     def make_noise(self):
#         print('gavv')

# class Car:
#     def make_noise(self):
#         print('bi-bi')

# def noise(animal: Animal):
#     animal.make_noise()

# if __name__ == '__main__':
#     noise(Dog())

# dunder - методы (от англ. сокращения double underscope)

# __str__() - для отображения информации об объекте класса для пользователей (например, для функций print, str).
# __repr__() - для отображения информации об объекте класса в режиме отладки (для разработчиков).
# __len__() - позволяет применять функцию len() к экземплярам класса.
# __abs__() - позволяет применять функцию abs() к экземплярам класса.

# Магические методы для атрибутов 
# __setattr__(self, key, value)__ - автоматически вызывается при изменении свойства key класса.
# __getattribute__(self, item) - автоматически вызывается при получении свойства класса с именем item.
# __getattr__(self, item) -  автоматически вызывается при получении несуществующего свойства item класса.
# __delattr__(self, item) - автоматически вызывается при удалении свойства item(не важно: существует или нет).


# __doc__ - содержит строку с описанием класса.
# __dict__ - содержит набор атрибутов экземляра класса.
# getattr(obj, name, default) - возвращает значение атрибута объекта.
# hasattr(obj, name) - проверяет на наличие атрибута name в obj/
# setattr(obj, name, value) - задает значение атрибута (если атрибут не существует, то он создается).
# delattr(obj, name) - удаляет атрибут с именем name.



# s = 'hello'
# d = {}
# try:
#     1/5
# except (KeyError):
#     print('fjdin')
# else:
#     print('good')
# finally:
#     print('end')