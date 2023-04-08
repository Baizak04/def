class Person:
    def can_breathe(self):
        print('я могу дышать')

    def can_walk(self):
        print('я могу ходить')

class Doctor(Person):

    def can_cure(self):
        print('я могу лечить')

class Architest(Person):

    def can_build(self):
        print('я могу построить здание')

d = Doctor()
d.can_cure()
d.can_walk()
d.can_breathe()
a = Architest()
a.can_build()
a.can_walk
# print(isinstance(d, Person))
# print(isinstance(d, Person))
# print(isinstance(a, Person))

# ====================================================


