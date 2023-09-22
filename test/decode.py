import quopri
import os

List_contact = []
File = "text.txt"
with open(File) as file:  # чтение файла с контактами
    for i in file:
        List_contact.append(i)


# функция для обьединения перенесенных строк
def Func(List_for_change):
    List_contact_1 = []
    for i in List_contact:
        if i[-2] == '%':
            List_contact_1.append(i[:-2])
        else:
            List_contact_1.append(i)
    with open('File.txt', 'w') as file:
        for i in List_contact_1:
            file.write(i)
    List_contact_1 = []
    with open('File.txt') as file:
        for i in file:
            List_contact_1.append(i)
    os.unlink('File.txt')  # удаление temp файла
    return (List_contact_1)


List_contact = Func(List_contact)

# Запись декодированного текста в файл
with open('Contacts_Decode.txt', 'w') as file:
    for i in List_contact:
        Str_1 = bytes(i, 'UTF-8')  # модуль quopri принимает на вход двоичные данные
        Str_2 = quopri.decodestring(Str_1)
        file.write(Str_2.decode('UTF-8'))
