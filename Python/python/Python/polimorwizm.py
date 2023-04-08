# class Cat:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def info(self):
#         print(f"I am a cat. My name is {self.name}. I am {self.age} years old.")

#     def make_sound(self):
#         print("Meow")


# class Dog:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def info(self):
#         print(f"I am a dog. My name is {self.name}. I am {self.age} years old.")

#     def make_sound(self):
#         print("Bark")


# cat1 = Cat("Kitty", 2.5)
# dog1 = Dog("Fluffy", 4)

# for animal in (cat1, dog1):
#     animal.make_sound()
#     animal.info()
#     animal.make_sound()

# ============================================================

# Пример 4: переопределение метода
# from math import pi


# class Shape:
#     def __init__(self, name):
#         self.name = name

#     def area(self):
#         pass

#     def fact(self):
#         return "I am a two-dimensional shape."

#     def __str__(self):
#         return self.name


# class Square(Shape):
#     def __init__(self, length):
#         super().__init__("Square")
#         self.length = length

#     def area(self):
#         return self.length**2

#     def fact(self):
#         return "Squares have each angle equal to 90 degrees."


# class Circle(Shape):
#     def __init__(self, radius):
#         super().__init__("Circle")
#         self.radius = radius

#     def area(self):
#         return pi*self.radius**2


# a = Square(4)
# b = Circle(7)
# print(b)
# print(b.fact())
# print(a.fact())
# print(b.area())


# от разных обектов одну обект
# способность функция работат с данными разных типов
# это возможность работы с разными с совершенно разными объектами едиными образом
# Полиморфизм — важный элемент объектно-ориентированного программирования в Python. Полиморфизм делает Python более универсальным и эффективным языком. Он позволяет использовать один оператор или функцию для выполнения нескольких задач. Это также позволяет вам повторно использовать имена методов, переопределяя их для уникальных целей разных классов.
# -способности функцииобрабатывать разные типы данных.
# class Cars:
# 	def nothing(self): # Пустая функция
# 		pass
		
# class BMW (Cars):
# 	def nothing(self, word):
# 		print (word + "!") # Функция теперь будет работать по новому
 
# a = BMW()
# a.nothing("Some")
# ===================================================================================
class Animal:
    def make_noise(self):
        print('shh')

class Cat(Animal):
    def make_noise(self):
        print('meow')

class Dog(Animal):
    def make_noise(self):
        print('gavv')

class Car:
    def make_noise(self):
        print('bi-bi')

def noise(animal: Animal):
    animal.make_noise()

if __name__ == '__main__':
    noise(Dog())




