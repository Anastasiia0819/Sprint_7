import requests
import random
import string
from helpers import get_random_data_for_order




# метод регистрации нового курьера возвращает список из логина и пароля
# если регистрация не удалась, возвращает пустой список
def register_new_courier_and_return_login_password():
    # метод генерирует строку, состоящую только из букв нижнего регистра, в качестве параметра передаём длину строки
    def generate_random_string(length):
        letters = string.ascii_lowercase
        random_string = ''.join(random.choice(letters) for i in range(length))
        return random_string

    # создаём список, чтобы метод мог его вернуть
    login_pass = []

    # генерируем логин, пароль и имя курьера
    login = generate_random_string(10)
    password = generate_random_string(10)
    first_name = generate_random_string(10)

    # собираем тело запроса
    payload = {
        "login": login,
        "password": password,
        "firstName": first_name
    }

    # отправляем запрос на регистрацию курьера и сохраняем ответ в переменную response
    response = requests.post('https://qa-scooter.praktikum-services.ru/api/v1/courier', data=payload)

    # если регистрация прошла успешно (код ответа 201), добавляем в список логин и пароль курьера
    if response.status_code == 201:
        login_pass.append(login)
        login_pass.append(password)
        login_pass.append(first_name)

    # возвращаем список
    #return login_pass
    #возвращает словарь
    return payload


def create_new_courier_return_list():
    # метод генерирует строку, состоящую только из букв нижнего регистра, в качестве параметра передаём длину строки
    def generate_random_string(length):
        letters = string.ascii_lowercase
        random_string = ''.join(random.choice(letters) for i in range(length))
        return random_string

        # создаём список, чтобы метод мог его вернуть
    login_pass = []

        # генерируем логин, пароль и имя курьера
    login = generate_random_string(10)
    password = generate_random_string(10)
    first_name = generate_random_string(10)

        # собираем тело запроса
    payload = {
        "login": login,
        "password": password,
        "firstName": first_name
    }

        # отправляем запрос на регистрацию курьера и сохраняем ответ в переменную response
    response = requests.post('https://qa-scooter.praktikum-services.ru/api/v1/courier', data=payload)

        # если регистрация прошла успешно (код ответа 201), добавляем в список логин и пароль курьера
    if response.status_code == 201:
        login_pass.append(login)
        login_pass.append(password)
        login_pass.append(first_name)

        # возвращаем список
    return login_pass


def data_for_order_1():
    name, lastname, password, address, deliverydate, comment = get_random_data_for_order()
    data_order_color_black = {
    "firstName": name,
    "lastName": lastname,
    "address": address,
    "metroStation": 4,
    "phone": "+78003553535",
    "rentTime": 5,
    "deliveryDate": deliverydate,
    "comment": comment,
    "color": [
        "BLACK"
    ]
    }
    data_order_color_grey = {
    "firstName": name,
    "lastName": lastname,
    "address": address,
    "metroStation": 4,
    "phone": "8 915 355 35 22",
    "rentTime": 5,
    "deliveryDate": deliverydate,
    "comment": comment,
    "color": [
        "GREY"
    ]
    }
    data_order_color_black_and_grey = {
    "firstName": name,
    "lastName": lastname,
    "address": address,
    "metroStation": 4,
    "phone": "+7 877 888 33 15",
    "rentTime": 5,
    "deliveryDate": deliverydate,
    "comment": comment,
    "color": [
        "GREY", "BLACK"
    ]
    }
    data_order_without_color = {
    "firstName": name,
    "lastName": lastname,
    "address": address,
    "metroStation": 4,
    "phone": "78003550099",
    "rentTime": 5,
    "deliveryDate": deliverydate,
    "comment": comment
    }
    return data_order_without_color, data_order_color_grey, data_order_color_black, data_order_color_black_and_grey


def data_for_order():
    name, lastname, password, address, deliverydate, comment = get_random_data_for_order()
    data_order = {
    "firstName": name,
    "lastName": lastname,
    "address": address,
    "metroStation": 1,
    "phone": "+78003553535",
    "rentTime": 10,
    "deliveryDate": deliverydate,
    "comment": comment,
    "color": []
    }
    return data_order



