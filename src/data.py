import requests
import random
import string
from helpers import get_random_data_for_order
from helpers import generate_random_string
from src.config import Config


# метод регистрации нового курьера возвращает список из логина и пароля
# если регистрация не удалась, возвращает пустой список
def register_new_courier_and_return_login_password():

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
    response = requests.post(f"{Config.URL}api/v1/courier", data=payload)

    # если регистрация прошла успешно (код ответа 201), добавляем в список логин и пароль курьера
    if response.status_code == 201:
        login_pass.append(login)
        login_pass.append(password)
        login_pass.append(first_name)

    #возвращает словарь
    return payload


def create_new_courier_return_list():

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
    response = requests.post(f"{Config.URL}api/v1/courier", data=payload)

        # если регистрация прошла успешно (код ответа 201), добавляем в список логин и пароль курьера
    if response.status_code == 201:
        login_pass.append(login)
        login_pass.append(password)
        login_pass.append(first_name)

        # возвращаем список
    return login_pass


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



