# Задание 2.3
name = 'Эдик '
text = 'Привет, ' + name + 'как твои дела? '
print(text)

# Задание 2.4

name = name.lower() # Перевожу имя в нижний регистр
text = 'Привет, ' + name + 'как твои дела? '
print(text)

name = name.upper() # Перевожу имя в верхний регистр
text = 'Привет, ' + name + 'как твои дела? '
print(text)

# Перевожу текст с капитализацией начальных букв каждого слова
text = text.title()
print(text)

# Задание 2.5

text_the_author = 'Богач Эдуард: "А на восьмой день Бог создал кофе =)"'
print(text_the_author)

# Задание 2.6

famous_person = 'Богач Эдуард'
message = famous_person + ': "А на восьмой день Бог создал кофе =)"'
print(message)

# Задание 2.7

name_persone = '  \n Петр  \t '
print(name_persone)
print(name_persone.lstrip()) # Убирает только пробелы в конце строки
print(name_persone.rstrip()) # Убирает только пробелы в начале строки
print(name_persone.strip()) # Убирает пробелы в начале и в конце строки

