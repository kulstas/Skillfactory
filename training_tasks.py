# def test_range(digit, low, high):
#     if digit not in range(low, high):
#         print(f'Число {digit} не попадает в диапазон между {low} и {high}')
#
#
# test_range(5, 1, 10)

"""Задание 3.3 (External resource)"""
# def is_success_code(code):
#     return 200 <= code <= 299
#
# print(is_success_code(200))
# print(is_success_code(404))

"""Задание 3.4 (External resource)"""
# def is_valid_email(e_mail:str):
#     return "@" in e_mail and "." in e_mail[e_mail.index("@")+1::] and not " " in e_mail
#
#
# print(is_valid_email("user@example. com"))

"""Задание 3.5 (External resource)"""
# def test_function(myfunc, par1, par2):
#     return myfunc(par1) == par2
#
#
# def square(n):
#    return n ** 2
#
#
# print(test_function(square, 4, 16))
# print(test_function(square, 5, 20))


""" PHONE BOOK """
# phoneBook = {
#     'Семен': '7777777777',
#     'Петр': '8888888888',
#     'Алеша': '9999999999',
#     'Гусь': '1111111111',
#     'Жора': '2222222222',
# }
#
# print(phoneBook.keys())
# print(phoneBook.values())
#
# for abon, number in phoneBook.items():
#     print(f"Имя: {abon} — Телефон: {number}")
#
# i = 1
# while i <= 2:
#     new_abon = input(f"Введите имя нового друга {i}: ")
#     new_number = input(f"Введите телефон нового друга {i}: ")
#     phoneBook[new_abon] = new_number
#     i += 1
#
# for abon, number in phoneBook.items():
#     print(f"Имя: {abon} — Телефон: {number}")


""" CLASS BOOK """
# import random
#
# # список учеников
# students = ['Аполлон', 'Ярослав', 'Александра', 'Дарья', 'Ангелина']
# # отсортируем список учеников
# students.sort()
# # список предметов
# classes = ['Математика', 'Русский язык', 'Информатика']
# # пустой словарь с оценками по каждому ученику и предмету
# students_marks = {}
# # сгенерируем данные по оценкам:
# # цикл по ученикам
# for student in students:  # 1 итерация: student = 'Александра'
#     students_marks[student] = {}  # 1 итерация: students_marks['Александра'] = {}
#     # цикл по предметам
#     for class_ in classes:  # 1 итерация: class_ = 'Математика'
#         marks = [random.randint(1, 5) for i in range(3)]  # генерируем список из 3х случайных оценок
#         students_marks[student][class_] = marks  # students_marks['Александра']['Математика'] = [5, 5, 5]
# # выводим получившийся словарь с оценками:
# for student in students:
#     print(f'''{student}
#             {students_marks[student]}''')
#
# print('''
#         Список команд:
#         1. Добавить оценки ученика по предмету
#         2. Вывести средний балл по всем предметам по каждому ученику
#         3. Вывести все оценки по всем ученикам
#         4. Редактировать имя ученика
#         5. Удалить ученика
#         6. Редактировать предметы ученика
#         7. Удалить предмет ученика
#         8. Редактировать оценку ученика
#         9. Удалить оценку ученика
#         10. Вывести информацию по всем оценкам ученика
#         11. Вывести средний балл по предметам ученика
#         12. Выход из программы
#         ''')
#
# while True:
#     command = int(input('Введите команду: '))
#     if command == 1:
#         print('1. Добавить оценку ученика по предмету')
#         # считываем имя ученика
#         student = input('Введите имя ученика: ')
#         # считываем название предмета
#         class_ = input('Введите предмет: ')
#         # считываем оценку
#         mark = int(input('Введите оценку: '))
#         # если данные введены верно
#         if student in students_marks.keys() and class_ in students_marks[student].keys():
#             # добавляем новую оценку для ученика по предмету
#             students_marks[student][class_].append(mark)
#             print(f'Для {student} по предмету {class_} добавлена оценка {mark}')
#         # неверно введены название предмета или имя ученика
#         else:
#             print('ОШИБКА: неверное имя ученика или название предмета')
#     elif command == 2:
#         print('2. Вывести средний балл по всем предметам по каждому ученику')
#         # цикл по ученикам
#         for student in students:
#             print(student)
#             # цикл по предметам
#             for class_ in classes:
#                 # находим сумму оценок по предмету
#                 marks_sum = sum(students_marks[student][class_])
#                 # находим количество оценок по предмету
#                 marks_count = len(students_marks[student][class_])
#                 # выводим средний балл по предмету
#                 print(f'{class_} - {marks_sum // marks_count}')
#             print()
#     elif command == 3:
#         print('3. Вывести все оценки по всем ученикам')
#         # выводим словарь с оценками:
#         # цикл по ученикам
#         for student in students:
#             print(student)
#             # цикл по предметам
#             for class_ in classes:
#                 print(f'\t{class_} - {students_marks[student][class_]}')
#             print()
#     elif command == 4:
#         print('4. Редактировать имя ученика')
#         student = input('Введите имя ученика: ')
#         if student in students:
#             rename_student = input(f'Введите новое имя для ученика ({student}): ')
#             students[students.index(student)] = rename_student
#             print(f'Имя ученика {student} успешно изменено на {rename_student}')
#             print(students)
#         else:
#             print('ОШИБКА: неверное имя ученика')
#     elif command == 5:
#         print('5. Удалить ученика')
#         del_student = input(f'Введите имя ученика, которго необходмо удалить: ')
#         if del_student in students:
#             students.remove(del_student)
#             del students_marks[del_student]
#             print(students)
#             print(students_marks)
#         else:
#             print('ОШИБКА: неверное имя ученика')
#     elif command == 6:
#         print('6. Редактировать предметы ученика')
#     elif command == 7:
#         print('7. Удалить предмет ученика')
#     elif command == 8:
#         print('8. Редактировать оценку ученика')
#     elif command == 9:
#         print('9. Удалить оценку ученика')
#     elif command == 10:
#         print('10. Вывести информацию по всем оценкам ученика')
#     elif command == 11:
#         print('11. Вывести средний балл по предметам ученика')
#     elif command == 12:
#         print('12. Выход из программы')
#         break


# def check_password(password):
#     if any(char.isalnum() for char in password):
#         if len(password) < 8:
#             print('Пароль должен быть не менее 8 символов')
#         if password.islower() or password.isdigit():
#             print('Пароль должен содержать хотя бы одну заглавную букву')
#         if password.isupper() or password.isdigit():
#             print('Пароль должен содержать хотя бы одну строчную букву')
#         if password.isalpha():
#             print('Пароль должен содержать хотя бы одну цифру')
#     else:
#         print('Пароль должен быть не менее 8 символов')
#         print('Пароль должен содержать хотя бы одну заглавную букву')
#         print('Пароль должен содержать хотя бы одну строчную букву')
#         print('Пароль должен содержать хотя бы одну цифру')

# userpass = '1'
# check_password(userpass)


"""Задание 4.3 (External resource)"""
# def is_valid_password(password, min_length=8, require_upper=True, require_lower=True, require_digit=True):
#     return (len(password) >= min_length) and ((any(i.isupper() for i in password) is require_upper) if require_upper else not require_upper) and ((any(i.islower() for i in password) is require_lower) if require_lower else not require_lower) and ((any(i.isdigit() for i in password) is require_digit) if require_digit else not require_digit)

# print(is_valid_password('Password123'))
# print(is_valid_password('abcdef', min_length=6, require_upper=False, require_lower=False, require_digit=False))


"""Задание 4.4 (External resource)"""
# import random
# def generate_test_data(n=5, min_value=1, max_value=10):
#     s = []
#     for i in range(n):
#         s.append(random.randint(min_value, max_value))
#
#     return s
#
#
# print(generate_test_data())


'''Задание 4.5 (External resource)'''
# def format_date(date, format=None):
#     date_sep = date.split(sep="-")
#     if format == 'dmy'or format is None:
#         return ''.join(date_sep[::-1])
#     elif format == 'mdy':
#         return date_sep[1]+date_sep[2]+date_sep[0]
#     elif format == 'ymd':
#         return date_sep[0] + date_sep[1] + date_sep[2]
#     else:
#         return date

# print(format_date("2023-07-01"))
# print(format_date("2023-07-01", format="dmy"))
# print(format_date("2023-07-01", format="mdy"))
# print(format_date("2023-07-01", format="ymd"))
# print(format_date("2023-07-01", format="xyz"))

'''Задание 4.6 (External resource)'''
# def compare_lists(lst1, lst2, ignore_case=False):
#     if ignore_case:
#         return list(set(el.lower() for el in lst1) - set(el.lower() for el in lst2))
#     else:
#         return list(set(lst1) - set(lst2))

# print(compare_lists(["apple", "banana", "cherry"], ["Banana", "cherry", "date"]))
# print(compare_lists(["apple", "banana", "cherry"], ["Banana", "cherry", "date"], ignore_case=True))
# print(compare_lists(['a', 'b', 'c'], ['B', 'C', 'D'], ignore_case = True))

"""Задание 5.2 (External resource)"""
# def calculate_average(*args):
#     return sum(args) / len(args)

"""Задание 5.3 (External resource)"""
# def sort_data(**kwargs):
#     return sorted(kwargs.items())
#
# print(sort_data(name='Alex', age=30, city='New York'))


'''Задание 6.1 (External resource)'''
# def sort_strings_by_last_char(sorting):
#     return sorted(sorting, key=lambda x: x[-1])
#
# strings = ["apple", "banana", "cherry", "date", "elderberry"]
# print(sort_strings_by_last_char(strings))


'''Задание 6.2 (External resource)'''
# def apply_function(ratings, my_func):
#     return [my_func(rat) for rat in ratings]
#
# numbers = [1, 2, 3, 4, 5]
# print(apply_function(numbers, lambda x: x**2))

'''Задание 7.1 (External resource)'''
# def sales_stats(sales, **kwargs):
#     sales_dict = {}
#     if ('revenue' or 'quantity') in kwargs:
#         if 'revenue' in kwargs:
#             rev = sum((lambda p, q: p * q)(sale[1], sale[2]) for sale in sales)
#         else:
#             rev = None
#         if 'quantity' in kwargs:
#             for sale in sales:
#                 if sale[0] in sales_dict:
#                     sales_dict[sale[0]] += sale[1]
#                 else:
#                     sales_dict[sale[0]] = sale[1]
#         else:
#             sales_dict = None
#     else:
#         rev, sales_dict = None, None
#
#     return (rev, sales_dict)


# sales_data = [["яблоки", 10, 20], ["груши", 5, 30], ["яблоки", 7, 20]]
# print(sales_stats(sales_data, revenue=True))
# (490, None)
# print(sales_stats(sales_data, quantity=True))
# (None, {'яблоки': 17, 'груши': 5})


# print(sales_stats([('Apple', 10, 0.5), ('Orange', 5, 0.6)], revenue=True, quantity=True))
# print(sales_stats([('Apple', 10, 0.5), ('Orange', 5, 0.6)], customers=True))
# print(sales_stats([('Apple', 10, 0.5), ('Orange', 5, 0.6)], revenue = True))

'''Задание 7.2 (External resource)'''
# def create_report(data, stats):
#     reports = stats(data, revenue=True, quantity=True)
#     print(f'Средний доход за данный период составил {reports[0]/len(data)}.')
#     print('Количество проданных единиц каждого товара:')
#     return "\n".join(f'{key}: {val}' for key, val in reports[1].items())
#
# sales_data = [["яблоки", 20, 20], ["груши", 5, 30], ["яблоки", 7, 20]]
# print(create_report(sales_data, sales_stats))
# Средний доход за данный период составил 230.0.
# Количество проданных единиц каждого товара:
# яблоки: 27
# груши: 5

'''Задание 7.3 (External resource)'''
# def sort_users_by_activity(usrs):
#     sorted_usrs=[]
#     for k in sorted(usrs.items(), reverse=True, key=lambda usr: usr[1]):
#         sorted_usrs.append(k[0])
#     return sorted_usrs
#
#
# user_activity = {"user1": 10, "user2": 5, "user3": 20, "user4": 15, "user5": 10}
# print(sort_users_by_activity(user_activity))
# # ['user3', 'user4', 'user1', 'user5', 'user2']

'''Задание 2.4 (External resource)'''
# def fibonacci(n):
#     if n <= 0:
#         return 0
#     elif n == 1:
#         return 1
#     else:
#         return fibonacci(n-1) + fibonacci(n-2)
#
# print(fibonacci(5))
# #5
# print(fibonacci(7))
# #13
# print(fibonacci(8))
# #21

'''Задание 2.5 (External resource)'''
# def is_palindrome(s):
#     if len(s) == 0:
#         return True
#     elif s[0] != s[-1]:
#         return False
#     else:
#         return is_palindrome(s[+1:-1])
#
#
# print(is_palindrome('racecar'))
# print(is_palindrome('gong'))

'''Задание 2.6 (External resource)'''
# def binary_search(lst, el):
#     if lst[len(lst)//2] == el:
#         return True
#     if lst[0] < el < lst[-1]:
#         if lst[len(lst)//2] > el:
#             return binary_search(lst[0:len(lst)//2], el)
#         elif lst[len(lst)//2] < el:
#             return binary_search(lst[len(lst)//2:], el)
#     else:
#         return False


# print(binary_search([1, 2, 3, 4, 5], 4))
# True
# print(binary_search([1, 2, 3, 4, 5], 6))
# False

'''Задание 3.3 (External resource)'''
# def generate_urls(text, min, max):
#     for i in range(min, max+1):
#         yield f'{text}{i}'
#
# url_generator = generate_urls("/product/", 1, 3)
# for url in url_generator:
#    print(url)
# /product/1
# /product/2
# /product/3

'''Задание 3.4 (External resource)'''
# from random import randint
# def generate_user_data(limit, fnames, lnames, age):
#    for i in range(limit):
#       yield fnames[randint(0, len(fnames))-1], lnames[randint(0, len(lnames)-1)], randint(age[0], age[1])
#
#
#
# first_names = ["Alice", "Bob", "Charlie"]
# last_names = ["Smith", "Johnson", "Williams"]
# user_data_generator = generate_user_data(5, first_names, last_names, [18, 60])
# for user in user_data_generator:
#    print(user)
# ('Charlie', 'Williams', 19)
# ('Charlie', 'Johnson', 48)
# ('Bob', 'Johnson', 26)
# ('Charlie', 'Smith', 36)
# ('Charlie', 'Johnson', 35)

'''Задание 3.5 (External resource)'''
# def fibonacci(n):
#    fib, f2 = 0, 0
#    f1 = 1
#    for _ in range(n):
#        yield fib
#        fib = f1 + f2
#        f2 = fib
#        f1 = fib - f1
#
#
# fibonacci_generator = fibonacci(7)
# for number in fibonacci_generator:
#    print(number)

# 0
# 1
# 1
# 2
# 3
# 5
# 8

'''Задание 3.6 (External resource)'''
# def primes(n):
#    for d in range(2, n+1):
#       if (d == 2 or d % 2 != 0) and (d == 3 or d % 3 != 0) and (d == 5 or d % 5 != 0):
#             yield d
#
# prime_generator = primes(33)
# for prime in prime_generator:
#    print(prime)

# 2
# 3
# 5
# 7

# headers = ["name", "age", "gender"]
# row = ["Alice", 28, "Female"]
#
#
# user_data = dict(zip(headers, row))
# print(user_data)

'''Задание 4.1 (External resource)'''
# prices_in_usd = [10, 20, 30, 40, 50]
# exchange_rate = 0.85
#
# prices_in_euro = list(map(lambda x: x*exchange_rate, prices_in_usd))

'''Задание 4.2 (External resource)'''
# phone_numbers = ['123-456-7890', '123.456.7890', '(123) 456-7890', '+1234567890', '1234567890']
#
# def format_phone_number(number):
#    return ''.join(list(filter(str.isdigit, number)))
#
# formatted_numbers = list(map(format_phone_number, phone_numbers))
#
# print(formatted_numbers)

'''Задание 6.6 (External resource)'''
# def create_counter():
#     v = 0
#     def count():
#         nonlocal v
#         v += 1
#         return v
#
#     return count
#
#
# counter = create_counter()
# print(counter())  # вернет "1"
# print(counter())  # вернет "2"
# print(counter())  # вернет "3"

'''Задание 6.7 (External resource)'''
# def create_unique_checker():
#     transactions = []
#
#     def check(transaction):
#         nonlocal transactions
#         if transaction in set(transactions):
#             return False
#         else:
#             transactions.append(transaction)
#             return True
#
#     return check
#
#
# unique_checker = create_unique_checker()
# print(unique_checker(5))
# print(unique_checker(5))
# print(unique_checker(10))
#
# # True
# # False
# # True

'''Задание 6.8 (External resource)'''
# import time
#
# def timer():
#     time_before = time.time()
#
#     def time_count():
#         nonlocal time_before
#         time_now = time.time()
#         result = time_now - time_before
#         time_before = time_now
#         return result
#
#     return time_count
#
# my_timer = timer()
# print(int(my_timer())) # int — для приближенного значения секунд
# # Ждем немного...
# time.sleep(2)
# print(int(my_timer()))

# Вывод:
# 0
# 2

'''Задание 6.9 (External resource)'''
# import random
#
# symbols_for_password = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
#
#
# def create_password_generator(size, symbols):
#     def pass_gen():
#         nonlocal size
#         nonlocal symbols
#         password = ''
#         for _ in range(size):
#             password += symbols[random.randint(0, len(symbols)-1)]
#         return password
#
#     return pass_gen
#
#
# password_generator = create_password_generator(10, symbols_for_password)
# print(password_generator())
# print(password_generator())

# Stl0tgwWSL
# oboYrgROdF

'''Задание 7.5 (External resource)'''
# import random
#
# def retry_if_result_is_none(times=1):
#     def decorator(func):
#         def wrapper(*args, **kwargs):
#             if func() != None:
#                 return func(*args, **kwargs)
#
#         return wrapper
#     return decorator
#
#
# @retry_if_result_is_none(times=2)
# def test_function():
#     return random.choice([None, "Passed"])
#
# # Получилось получить значение за 2 вызова
# print(test_function())
# # Passed
#
# # Не получилось получить значение за 2 вызова
# print(test_function())
# # None


'''Задание 7.6 (External resource)'''
# import random
#
# def ensure_result_is_number(func):
#     def wrapper(*args, **kwargs):
#         res = func()
#         if type(res) == int or type(res) == float:
#             return res
#         else:
#             return None
#
#     return wrapper
#
# @ensure_result_is_number
# def test_function():
#     return random.choice(["Passed", 10, "Failed", 5.5])
#
# # Функция вернула не int и не float
# print(test_function())
# # None
#
# # Функция вернула float
# print(test_function())
# # 5.5
#
# # Функция вернула int
# print(test_function())
# # 10

'''Задание 9.1 (External resource)'''
# from datetime import date
# from typing import List, Dict, Any
#
#
# def calculate_age(birth_date: str) -> int:
#     return int((date.today() - date.fromisoformat(birth_date)).days/365.25)
#
#
# print(calculate_age("1990-05-15"))
# # 33
#
# users_data = [{'first_name': 'John', 'last_name': 'Doe', 'birth_date': '1990-05-15'},
#               {'first_name': 'Bob', 'last_name': 'Johnson', 'birth_date': '1985-10-22'},
#               {'first_name': 'Lev', 'last_name': 'Sergeev', 'birth_date': '2015-01-01'}]
#
#
# def filter_adults(users: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
#     checked_users = []
#     for user in users:
#         if calculate_age(user['birth_date']) >= 18:
#             checked_users.append(user)
#
#     return checked_users
#
#
# print(filter_adults(users_data))
# # [{'first_name': 'John', 'last_name': 'Doe', 'birth_date': '1990-05-15'}, {'first_name': 'Bob', 'last_name': 'Johnson', 'birth_date': '1985-10-22'}]
#
#
# def generate_username(first_name: str, last_name: str) -> str:
#     return str(first_name[0] + '.' + last_name).lower()
#
# print(generate_username("John", "Doe"))
# # "j.doe"

'''Задание 9.2 (External resource)'''
# from typing import List, Dict, Any
# # А также вам наверняка может понадобиться модуль functools...
#
# def convert_to_full_name(users: List[Dict[str, Any]]) -> List[str]:
#     full_names_users = []
#     for user in users:
#         full_names_users.append(user['first_name']+' '+user['last_name'])
#     return full_names_users
#
#
# def find_matching_emails(users1: List[Dict[str, Any]], users2: List[Dict[str, Any]]) -> set:
#     emails_1, emails_2 = [], []
#     for user in users1:
#         emails_1.append(user['email'])
#
#     for user in users2:
#         emails_2.append(user['email'])
#
#     return set(emails_1) & set(emails_2)
#
#
# def combine_user_data(users: List[Dict[str, Any]]) -> Dict[str, List[Any]]:
#     combine_users = {}
#
#     for user in users:
#         for key in user:
#             combine_users[key] = ()
#
#     for key in combine_users.keys():
#         combine_users[key] = tuple(user[key] for user in users)
#
#     return combine_users
#
#
# users_data = [{'first_name': 'John', 'last_name': 'Doe', 'birth_date': '1990-05-15', 'email': 'johndoe@gmail.com'},
#              {'first_name': 'Bob', 'last_name': 'Johnson', 'birth_date': '1985-10-22', 'email': 'bobJ@gmail.com'},
#              {'first_name': 'Lev', 'last_name': 'Sergeev', 'birth_date': '2015-01-01', 'email': 'lev46@gmail.com'}]
#
# users_data_ext = [{'first_name': 'John', 'last_name': 'Doe', 'birth_date': '1990-05-15', 'email': 'johndoe@gmail.com'}]

# print(convert_to_full_name(users_data))
# ['John Doe', 'Bob Johnson', 'Lev Sergeev']

# print(find_matching_emails(users_data, users_data_ext))
# {'johndoe@gmail.com'}

# print(combine_user_data(users_data))
# {'first_name': ('John', 'Bob', 'Lev'), 'last_name': ('Doe', 'Johnson', 'Sergeev'), 'birth_date': ('1990-05-15', '1985-10-22', '2015-01-01'), 'email': ('johndoe@gmail.com', 'bobJ@gmail.com', 'lev46@gmail.com')}

'''Задание 9.3 (External resource)'''
# import time
# from typing import Callable
#
#
# def time_it(func: Callable):
#     def wrapper(*args, **kwargs):
#         time_start = time.time()
#         func(*args, **kwargs)
#         time_ex = time.time() - time_start
#         print(f"Execution time of '{func.__name__}': {int(time_ex)} seconds")
#     return wrapper
#
#
# # Функция — пример
# # Она просто делает копию списка, добавляет value в конец списка и возвращает этот список
# def add_point(original_list: list, value):
#     # Специально делаем sleep, потому как без него время выполнения будет около нуля
#     time.sleep(2)
#     return original_list[:].append(value)
#
#
# # Делаем новую функцию уже с декоратором
# @time_it
# def add_point_with_timer(original_list: list, value):
#     add_point(original_list, value)
#
#
# # Выполняем функцию с декоратором
# add_point_with_timer([1, 2, 3, 4, 5], 6)
#
# # Execution time of 'add_point_with_timer': 2.003331 seconds

