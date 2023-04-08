# {% %} -спецификатор шаблон;
# {{}} - выражение для вставки конструкций Python в шаблон;
# {##} - блок комментариев;
# ## - строковый комментарий.
# выражение for 
# {% for<выражение>-%}
# <повторяемый фрагмент>
# {% endfor %}

# Выражение if  

# {% if <условие>%}
    # <фрагмент при истинности условия>
# {% endif%}

# блок filter
# {{filter<названия фильтра> %}}
# <фрагмент для применения фильтра>
# {% endfilter%}

# Вложенные макросы - call
# {% call[(параметры)]<вызов макроса>%}
# <вложеный шаблон>
# {% endcall %}

# templates

# PackageLoader - для загрузки шаблонов из пакета;
# DictLoader - для загрузки шаблонов из словаря;
# FunctionLoader - для загрузки на основе функции;
# PrefixLoader - загрузчик, использующий словарь для построения подкаталогов;
# ChoiceLoader - загрузчик, содержащий список других загрузчиков 
# ModuleLoader - загрузчик для скомпилированных шаблонов.




# from Jinja import Template

# name = "Байзак"

# tm = Template("Привет{{ name}}")
# msg = tm.render(name=name)

# msg2 = f"Привет{name}"
# print(msg, msg2, sep="\n")
# #ТЕрминал
# # Привет Федор
# #Привет Федор

# 2)

# from Jinja import Template

# name = "wel"
# age = 28

# tm = Template(" Мне {{ a }} лет и зовут {{ n }}")
# msg = tm.render(n=name, a = age)

# print(msg)

# 3)

# from Jinja import Template

# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

# per = Person("Baizak", 22)

# tm = Template(" Мне {{ p.age }} лет и зовут {{ p.name }}.")
# msg = tm.render(p = per)

# print(msg)

# 4)

# from Jinja import Template

# per = { 'name': 'wer', 'age': 34}
# tm = Template(" Мне {{ p['age] }} лет и зовут {{ p['name] }}.")
# msg = tm.render(p = per)

# print(msg)

# 5)

#  from Jinja import Template

# link = '''В HTML-документе ссылки определяются так:
# <a href="#"> Ссылка</a>'''

# tm = Template(link)
# msg = tm.render()

# print(msg)


# 6)
# from Jinja import Template

# cities = [{'id' : 1, 'city' : 'Москва'},
#           {'id' : 1, 'city' : 'Москва'},
#           {'id' : 1, 'city' : 'Москва'},
#           {'id' : 1, 'city' : 'Москва'},
#           {'id' : 1, 'city' : 'Москва'}]

# link = '''<select name="cities
# {% for c in cities %}
#     <option value="{{c['id]}}">{{c['city]}}</option>
# {% endfor %}
# </select>'''
#  tm = Template(link)
# msg = tm.render(cities = cities)

# print(msg)