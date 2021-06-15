# 8-6. Названия городов: напишите функцию city_country(), которая получает название города и страну.
# Функция должна возвращать строку в формате “Santiago, Chile”.
# Вызовите свою функцию по крайней мере для трех пар «город—страна» и выведите возвращенное значение.

def city_country(city, country):
    city_count = city + ', ' + country
    return city_count.title()


result1 = city_country('москва', 'россия')
result2 = city_country('минск', 'беларусь')
result3 = city_country('прага', 'чехия')
print(result1)
print(result2)
print(result3)


# 8-7. Альбом: напишите функцию make_album(), которая строит словарь с описанием музыкального альбома.
# Функция должна получать имя исполнителя и название альбома и возвращать словарь, содержащий эти два вида информации.
# Используйте функцию для создания трех словарей, представляющих разные альбомы.
# Выведите все возвращаемые значения, чтобы показать, что информация правильно сохраняется во всех трех словарях.
# Добавьте в make_album() дополнительный параметр для сохранения количества дорожек в альбоме.
# Если в строку вызова включено значение количества дорожек, добавьте это значение в словарь альбома.
# Создайте как минимум один новый вызов функции с передачей количества дорожек в альбоме.

def make_album(name_player, name_album, num_tracks=''):
    album = {
        'name': name_player.title(),
        'album': name_album
    }
    if num_tracks:
        album['num_tracks'] = num_tracks
    return album


print(make_album(name_player='аматоры', name_album='дыши со мной'))
print(make_album(name_player='анакондаз', name_album='смотри на меня'))
print(make_album(name_player='кукушка', name_album='кукареку', num_tracks=2))


# 8-8. Пользовательские альбомы: начните с программы из упражнения 8-7.
# Напишите цикл while, в котором пользователь вводит исполнителя и название альбома.
# Затем в цикле вызывается функция make_album() для введенных пользователей и выводится созданный словарь.
# Не забудьте предусмотреть признак завершения в цикле while.

def enter_make_album():
    power_active = True
    while power_active:
        print('\nДля выхода введите "q"')
        name_player = input('Введите исполнителя: ')
        if name_player.lower() == 'q':
            break
        name_album = input('Введите название альбома: ')
        print(make_album(name_player, name_album))


enter_make_album()
