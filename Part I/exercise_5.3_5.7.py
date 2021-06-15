# 5-3. Цвета 1: представьте, что в вашей компьютерной игре только что был подбит корабль пришельцев.
# Создайте переменную с именем alien_color и присвойте ей значение ‘green’, ‘yellow’ или ‘red’.
# • Напишите команду if для проверки того, что переменная содержит значение ‘green’.
# Если условие истинно, выведите сообщение о том, что игрок только что заработал 5 очков.
# • Напишите одну версию программы, в которой условие if выполняется, и другую версию, в которой оно не выполняется.
# (Во второй версии никакое сообщение выводиться не должно.)

alien_color = 'green'

print('\nЗадание 5-3.1 ')
if alien_color == 'green':
    print('Вы заработали 5 очков!!!')

print('\nЗадание 5-3.2')
if alien_color != 'green':
    pass

# 5-4. Цвета 2: выберите цвет, как это было сделано в упражнении 5-3, и напишите цепочку if-else.
# • Напишите команду if для проверки того, что переменная содержит значение ‘green’.
# Если условие истинно, выведите сообщение о том, что игрок только что заработал 5 очков.
# • Если переменная содержит любое другое значение, выведите сообщение о том, что игрок только что заработал 10 очков.
# • Напишите одну версию программы, в которой выполняется блок if, и другую версию, в которой выполняется блок else.

print('\nЗадание 5-4')

if alien_color == 'green':
    print('Вы заработали 5 очков!!!')
else:
    print('Вы заработали 10 очков!!!')

if alien_color != 'green':
    print('Вы заработали 5 очков!!!')
else:
    print('Вы заработали 10 очков!!!')

# 5-5. Цвета 3: преобразуйте цепочку if-else из упражнения 5-4 в цепочку if-elif-else.
# • Если переменная содержит значение 'green’, выведите сообщение о том, что игрок только что заработал 5 очков.
# • Если переменная содержит значение 'yellow’, выведите сообщение о том, что игрок только что заработал 10 очков.
# • Если переменная содержит значение 'red’, выведите сообщение о том, что игрок только что заработал 15 очков.
# • Напишите три версии программы и проследите за тем,
# чтобы для каждого цвета пришельца выводилось соответствующее сообщение.

print('\nЗадание 5-5')

color_alien = 'green'

if color_alien == 'green':
    print(color_alien + ' заработал 5 очков!!!')
elif color_alien == 'yellow':
    print(color_alien + ' заработал 10 очков!!!')
else:
    print(color_alien + ' заработал 15 очков!!!')

color_alien = 'yellow'

if color_alien == 'green':
    print(color_alien + ' заработал 5 очков!!!')
elif color_alien == 'yellow':
    print(color_alien + ' заработал 10 очков!!!')
else:
    print(color_alien + ' заработал 15 очков!!!')

color_alien = 'red'

if color_alien == 'green':
    print(color_alien + ' заработал 5 очков!!!')
elif color_alien == 'yellow':
    print(color_alien + ' заработал 10 очков!!!')
else:
    print(color_alien + ' заработал 15 очков!!!')

# 5-6. Периоды жизни: напишите цепочку if-elif-else для определения периода жизни человека.
# Присвойте значение переменной age, а затем выведите сообщение.
# • Если значение меньше 2 — младенец.
# • Если значение больше или равно 2, но меньше 4 — малыш.
# • Если значение больше или равно 4, но меньше 13 — ребенок.
# • Если значение больше или равно 13, но меньше 20 — подросток.
# • Если значение больше или равно 20, но меньше 65 — взрослый.
# • Если значение больше или равно 65 — пожилой человек.

print('\nЗадание 5-6. Периоды жизни')

age = 22

if age < 2:
    print('Младенец')
elif 2 <= age <= 4:
    print('Малыш')
elif 4 <= age <= 13:
    print('Ребёнок')
elif 13 <= age <= 20:
    print('Подросток')
elif 20 <= age <= 65:
    print('Взрослый')
elif 65 <= age:
    print('Пожилой человек')
else:
    print('Что то пошло не так!')

# 5-7. Любимый фрукт: составьте список своих любимых фруктов.
# Напишите серию независимых команд if для проверки того, присутствуют ли некоторые фрукты в списке.
# • Создайте список трех своих любимых фруктов и назовите его favorite_fruits.
# • Напишите пять команд if. Каждая команда должна проверять, входит ли определенный тип фрукта в список.
# Если фрукт входит в список, блок if должен выводить сообщение вида «You really like bananas!».
# Использование команд if со списками
print('\nЗадание 5-7. Любимый фрукт')

favorite_fruits = ['Банан', 'Ананас', 'Лимон']

if 'Банан' in favorite_fruits:
    print('Я люблю бананы')

if 'Апельсин' in favorite_fruits:
    print('Я не люблю апельсины')

if 'Ананас' in favorite_fruits:
    print('Я люблю ананасы')

if 'Лимон' in favorite_fruits:
    print('Я люблю лимоны')

if 'Баклажан' in favorite_fruits:
    print('Я не люблю баклажаны')
