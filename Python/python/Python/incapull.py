# class Base:
#     def __init__(self):
 
#         # Protected member
# #         self._a = 2
 
# # # Creating a derived class
# # class Derived(Base):
# #     def __init__(self):
 
# #         # Calling constructor of
# #         # Base class
# #         Base.__init__(self)
# #         print("Calling protected member of base class: ",
# #               self._a)
 
# #         # Modify the protected variable:
# #         self._a = 3
# #         print("Calling modified protected member outside class: ",
# #               self._a)
 
 
# # obj1 = Derived()
 
# # obj2 = Base()

# # print("Accessing protected member of obj1: ", obj1._a)
 
# # # Accessing the protected variable outside
# # print("Accessing protected member of obj2: ", obj2._a)

# class Employee:
#     def __init__(self, name, salary, project):
        
#         self.name = name
#         self.salary = salary
#         self.project = project

#     def show(self):
      
#         print("Name: ", self.name, 'оплата труда в:', self.salary)

# #     def work(self):
# #         print(self.name, 'он учиться', self.project)

# # emp = Employee('Байзак', 9000, 'itspace_kg')


# # emp.show()
# # emp.work()


# # class Employee:
# #    def __init__(self, name, salary):
# #     self.name = name
# #     self.__salary = salary

# # emp = Employee('Jessa', 10000)
# # print('Salary:', emp.__salary)

# # class Phone:
# #     def __init__(self, number):      # magic method / inititalizer
# #         print( "The Phone object was created" )
# #         self.number = number

# # #     def __lt__(self, other):         # magic method / rich comparison
# # #         return self.number < other.number

# # # my_phone = Phone(20)
# # # other_phone = Phone(30)

# # # if my_phone < other_phone:
# # #     print( "Two instances of custom class were compared" )
# # #     print( "'__lt__' was called implicitly" )

# # # if my_phone.__lt__(other_phone):
# # #     print( "Now, '__lt__' was used explicitly" )

# # # input( "Press Enter to exit" )


# class B:
#     B__count = 1

 
#     def __count__(self):
#         B.__count += 1
#         if B.__count == 1:
#             print(True)
#         elif B!=10:
#             print(False)
#     def __del__(self):
#         B.__count -= 1
 
 
# a = B()
# print(B._B__count)

# class j:
#     j = print()
#     j._count += 1
#     if j._count == "123456":
    
#         print('True')
#     elif j!=10:
#         print('dfgh')
#     else:
#         print('False')
#         j._count -= 1
# from random import order
# data =[]
# for i in range(10):
#     data.count(int(order()*10))
# print(data)

# j = []
# for i in data:
#     if data.count(i) == 1:
#         j.append(i)
# print(j)




# attribute(без одного или двух подчеркиваний вначале) - публичное свойство (public)
# _attribute(с одним подчеркиванием) - режим доступа protected (служит для обращения внутр класса и во всех его подчеркиваних классах)
# __attribute(с двумя подчеркиваниями) - режим доступа private (служит для обращения только внутри класса)

#  =============================================================================================================================================

