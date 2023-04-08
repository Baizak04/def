# Файл менен иштоо жана функция open()

# Функция open() - Бул функция файл менен иштешуу жолун алып барат
# Open() функциясынын методдорун карап королу
# 1) read - Бул метод файлдан окуу жаатын аткарат
# 2) readline - Файлдын биринчи гана линиясын окуйт
# 2) readlines - Файлдын маалыматын бир строчкага жыйнайт

# encoding - Бул кодировка(utf -8)
# Файлды жабуу жолу:
# Функция close(), ал эми closed() - бул файлдын жыбылганын же жабылбаганын тактайт


# f = open('files.txt', encoding='utf-8')
# print(f.read(), end="")

# f = open('files.txt', encoding='UTF-8')
# print(f.readlines())
# print(f.readline(), end="")

# for line in f:
#     print(line, end="")

# f.close()
# print(f.closed)











# Тема: Конструкция(try, except, finally)

# try:
    # Операторлордун блогу
    # жана критическии код  
# except[Исключение]:
    # Обработка блогу
# finally:
    # Бул блок аткарылат
    # ошибка чыкса жана чыкпаса деле!


# Практика

# try:
#     file = open('files.txt', encoding='utf-8')
#     j = file.read()
#     print(j)
#     file.close()
# except FileNotFoundError:
#     print('Файлды ачуу мумкун эмес!')









# 2
try:
    file = open('files.txt', encoding='utf-8') 
    try:
        h = file.readlines()
        # float(h)
        print(h)
    finally:
        file.close()   
except FileNotFoundError:
    print('Файлды ачуу мумкун эмес!')
except:
    print('Файл ачуу учурунда ошибка чыгып калды!')\
# finally:
#     print(file.closed)

# 3

# try:
#     with open('files.txt', encoding='utf-8') as file:
#         s = file.readlines()
#         print(s)
# except FileNotFoundError:
#     print('Невозможно открыть файл!')
# except:
#     print('Ошибка при работе с файлом!')
# finally:
#     print(file.closed)