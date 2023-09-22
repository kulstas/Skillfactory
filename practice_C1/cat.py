class Cat:
    def __init__(self, name, sex, age):
        self.name = name
        self.sex = sex
        self.age = age

    def get_name(self):
        return self.name

    def get_sex(self):
        return self.sex

    def get_age(self):
        return self.age

class Dog(Cat):
    def get_pet(self):
        return self.get_name(), self.get_age()

class Client:
    def __init__(self, name, lastname, city, balance):
        self.name = name
        self.lastname = lastname
        self.city = city
        self.balance = balance

    def get_name(self):
        return self.name

    def get_lastname(self):
        return self.lastname

    def get_city(self):
        return self.city

    def get_balance(self):
        return self.balance

    def __str__(self):
        return f"{self.get_name()} {self.get_lastname()}. {self.get_city()}. {self.get_balance()} руб."

    def get_corporate(self):
        return f"{self.get_name()} {self.get_lastname()}. {self.get_city()}."