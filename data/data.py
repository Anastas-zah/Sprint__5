import random


class PersonData:
    user_name = 'Лидия Иванова'
    login = 'Ivanova@yandex.ru'
    password = '147258369'


class ValidData:
    user_name = 'Test test'
    login = f"Test_test{random.randint(10, 999)}@yandex.ru"
    password = f"{random.randint(100, 999)}{random.randint(100, 999)}"