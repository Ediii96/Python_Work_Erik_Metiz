# 7-8. Сэндвичи: создайте список с именем sandwich_orders, заполните его названиями различных видов сэндвичей.
# Создайте пустой список с именем finished_sandwiches.
# В цикле переберите элементы первого списка и выведите сообщение
# для каждого элемента (например, «I made your tuna sandwich»).
# После этого каждый сэндвич из первого списка перемещается в список finished_sandwiches.
# После того как все элементы первого списка будут обработаны,
# выведите сообщение с перечислением всех изготовленных сэндвичей.

def made_sandwiches():
    sandwich_orders = ['тунцом', 'ветчиной', 'сёмгой', 'капустой', 'пивом']
    finished_sandwiches = []
    while sandwich_orders:
        current_sandwich = sandwich_orders.pop(0)
        finished_sandwiches.append(current_sandwich)
    for sandwich in finished_sandwiches:
        print('Я сделал для тебя сэндвич с ' + sandwich)


# made_sandwiches()

# 7-9. Без пастрами: используя список sandwich_orders из упражнения 7-8,
# проследите за тем, чтобы значение ‘пивом’ встречалось в списке как минимум три раза.
# Добавьте в начало программы код для вывода сообщения о том, что пастрами больше нет,
# и напишите цикл while для удаления всех вхождений ‘пивом’ из sandwich_orders.
# Убедитесь в том, что в finished_sandwiches значение ‘пивом’ не встречается ни одного раза.

def del_sandwich():
    delete_sandwich = 'пивом'
    sandwich_orders = ['тунцом', 'ветчиной', 'пивом', 'сёмгой', 'пивом', 'капустой', 'пивом']
    finished_sandwiches = []
    print('К сожалению с ' + delete_sandwich.lower() + ' сэндвичи закончились!\n')

    while delete_sandwich in sandwich_orders:
        sandwich_orders.remove(delete_sandwich)

    for sandwich in sandwich_orders:
        finished_sandwiches.append(sandwich)

    print(finished_sandwiches)


# del_sandwich()

# 7-10. Отпуск мечты: напишите программу, которая опрашивает пользователей, где бы они хотели провести отпуск.
# Включите блок кода для вывода результатов опроса.

def polling():
    responses = {}
    polling_active = True

    while polling_active:
        name = input('Назовите своё имя: \n')
        response = input('На какое море вы хотели бы поехать? \n')
        responses[name] = response
        repeat = input('Будет ли отвечать ещё кто то после вас? (yes/no)\n')
        if str(repeat) == 'no':
            polling_active = False
    print('\n--- Результаты опроса ---\n')

    for name, response in responses.items():
        print(name.title() + ', хотел бы поехать на ' + response + ' море.')


# polling()
