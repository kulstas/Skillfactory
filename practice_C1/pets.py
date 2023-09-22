# from cat import Cat
#
# pet1 = Cat("Барон", "Мальчик", "2 года")
# pet2 = Cat("Гоша", "Мальчик", "1 год")
# pet3 = Cat("Мухтар", "Мальчик", "0 лет")
# pet4 = Cat("Сэм", "Мальчик", "2 года")
#
# print(f"Питомец №1: {pet1.get_name()}, пол: {pet1.get_sex()}, возраст: {pet1.get_age()}")
# print(f"Питомец №2: {pet2.get_name()}, пол: {pet2.get_sex()}, возраст: {pet2.get_age()}")
# print(f"Питомец №3: {pet3.get_name()}, пол: {pet3.get_sex()}, возраст: {pet3.get_age()}")
# print(f"Питомец №4: {pet4.get_name()}, пол: {pet4.get_sex()}, возраст: {pet4.get_age()}")

from cat import Dog, Client

pet1 = Dog("Барон", "Мальчик", "2 года")
pet2 = Dog("Гоша", "Мальчик", "1 год")
pet3 = Dog("Мухтар", "Мальчик","0 лет")
pet4 = Dog("Сэм", "Мальчик","2 года")

print(f"Питомец №1: {pet1.get_pet()}")
print(f"Питомец №2: {pet2.get_pet()}")
print(f"Питомец №3: {pet3.get_pet()}")
print(f"Питомец №4: {pet4.get_pet()}")

client_1 = Client("Иван", "Петров", "Москва", 99)
client_2 = Client("Петр", "Иванов", "Тула", 120)
client_3 = Client("Иван", "иванов", "Брянск", 500)

print(client_1)
print(client_2)
print(client_3)

clients = [client_1, client_2, client_3]

for client in clients:
    print(client.get_corporate())


