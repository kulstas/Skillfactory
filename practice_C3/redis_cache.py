import redis
import json

red = redis.Redis(
    host='localhost',
    port=6379
)

# dict1 = {'key1': 'value1', 'key2': 'value2', 'key3': 'value3'}
# red.set('dict1', json.dumps(dict1))
#
# converted_dict = json.loads(red.get('dict1'))
#
# print(converted_dict)
#
# red.delete('dict1')
# print(red.get('dict1'))

i = 'add'
phone_book = {}

if i == 'add':
    a = 'y'
    while a == 'y':
        friend = (
            str(input('Введите имя: ')),
            int(input('Введите телефон: '))
        )
        phone_book.update([friend])
        a = input('Прродолжить ввод? y / n: ')
    red.set('phone_book', json.dumps(phone_book))
    i = str(input('Что дальше? Показать — "show" или удалить — "del" '))

if i == "show":
    converted_phone_book = json.loads(red.get('phone_book'))
    name = str(input("Введите имя: "))
    print(f"{name}: {phone_book[name]}")
    i = str(input('Что дальше? Показать — "show", удалить — "del", добавить — "add" '))
if i == "del":
    red.delete(input("Введите имя удаляемого: "))
    i = str(input('Что дальше? Показать — "show", удалить — "del", добавить — "add" '))