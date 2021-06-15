# 4-10. Срезы: добавьте в конец одной из программ, написанных в этой главе, фрагмент, который делает следующее.
# • Выводит сообщение «The first three items in the list are:»,
# а затем использует срез для вывода первых трех элементов из списка.
# • Выводит сообщение «Three items from the middle of the list are:»,
# а затем использует срез для вывода первых трех элементов из середины списка.
# • Выводит сообщение «The last three items in the list are:»,
# а затем использует срез для вывода последних трех элементов из списка.

def word_slices():
    text = 'The first three items in the list are:'
    print(text[:3])
    text_two = 'Three items from the middle of the list are:'
    print(text_two[21:24])
    text_thee = 'The last three items in the list are:'
    print(text_thee[-3:])

# word_slices()

# 4-11. Моя пицца, твоя пицца: начните с программы из упражнения 4-1.
# Создайте копию списка с видами пиццы, присвойте ему имя friend_pizzas. Затем сделайте следующее.
# • Добавьте новую пиццу в исходный список.
# • Добавьте другую пиццу в список friend_pizzas.
# • Докажите, что в программе существуют два разных списка. Выведите сообщение «My favorite pizzas are:»,
# а затем первый список в цикле for. Выведите сообщение «My friend’s favorite pizzas are:»,
# а затем второй список в цикле for. Убедитесь в том, что каждая новая пицца находится в соответствующем списке.

def value_pizza():
    pizza = ['Курица с ананасами', 'Четыре сыра', 'Мясная']
    friend_pizzas = ['Курица с ананасами', 'Четыре сыра', 'Мясная', 'Святая']

    print('Я люблю пиццу: ')
    for name_pizza in pizza:
        print(str(name_pizza.lower()))

    print('Мои друзья любят пиццу: ')
    for name_pizza in friend_pizzas:
        print(str(name_pizza.lower()))

# value_pizza()

# 4-12. Больше циклов: во всех версиях foods.py из этого раздела мы избегали использования цикла for при выводе
# для экономии места. Выберите версию foods.py и напишите два цикла for для вывода каждого списка.
# Кортежи
foods = ['Суп', 'Пицца', 'Пирог']
foods_friends = foods[:]

foods.append('Каша')
foods_friends.append('Мясо')

print('Моя еда: ')
for my_food in foods:
    print(my_food)

print('\nЕда друзей: ')
for food_friends in foods_friends:
    print(food_friends)
