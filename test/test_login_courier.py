import pytest
import requests
import json
from src.config import Config
import random
import string
from helpers import generate_random_string
import allure


class TestLoginCourier:
    @allure.title("Авторизация курьера")
    @allure.step("Успешная авторизация курьера")
    @allure.description("Проверка на статус код = 200, в ответе id не None")
    def test_login_courier(self, register_new_courier_list):
        # данные курьера из фикстуры
        courier_data = register_new_courier_list
        # проверка, что список не пустой
        assert len(courier_data) == 3, "Курьер не был создан, регистрация неуспешна"
        #логин, пароль и имя сгенерированы
        login, password, first_name = courier_data
        assert login != "", "Логин курьера не был сгенерирован"
        assert password != "", "Пароль курьера не был сгенерирован"
        assert first_name != "", "Имя курьера не было сгенерировано"
        # авторизации курьера
        login_payload = {
            "login": login,
            "password": password
        }
        #запрос для авторизации курьера
        login_response = requests.post(f"{Config.URL}api/v1/courier/login",
                                       json=login_payload)
        #курьер успешно авторизовался (код ответа 200)
        assert login_response.status_code == 200, f"Авторизация курьера неуспешна: {login_response.text}"
        assert login_response.json()["id"] is not None

    @allure.step("Логин не передается")
    @allure.description("В теле не передается логин пользователя")
    def test_login_without_login_error(self, register_new_courier_dict):
        courier_data = register_new_courier_dict
        payload = {"login": courier_data["login"] is None, "password": courier_data["password"]}
        response = requests.post(f"{Config.URL}api/v1/courier/login", json=payload)
        assert response.status_code == 400
        assert response.json()["message"] == "Недостаточно данных для входа"

    @allure.step("Пароль не передается")
    @allure.description("В теле не передается пароль пользователя")
    def test_login_without_password_error(self, register_new_courier_dict):
        courier_data = register_new_courier_dict
        payload = {"login": courier_data["login"], "password": courier_data["password"] is None}
        response = requests.post(f"{Config.URL}api/v1/courier/login", json=payload)
        assert response.status_code == 400
        assert response.json()["message"] == "Недостаточно данных для входа"

    @allure.step("Некорректно указан логин")
    def test_login_incorrect_login_error(self, register_new_courier_dict):
        courier_data = register_new_courier_dict
        payload = {"login": generate_random_string(10), "password": courier_data["password"]}
        response = requests.post(f"{Config.URL}api/v1/courier/login", json=payload)
        assert response.status_code == 404
        assert response.json()["message"] == "Учетная запись не найдена"

    @allure.step("Некорректно указан пароль")
    def test_login_incorrect_password_error(self, register_new_courier_dict):
        courier_data = register_new_courier_dict
        payload = {"login": courier_data["login"], "password": generate_random_string(10)}
        response = requests.post(f"{Config.URL}api/v1/courier/login", json=payload)
        assert response.status_code == 404
        assert response.json()["message"] == "Учетная запись не найдена"

    @allure.step("Авторизация под несуществующим пользователем - логин и пароль - не существует")
    def test_login_unknown_user_error(self):
        payload = {"login": generate_random_string(10), "password": generate_random_string(10)}
        response = requests.post(f"{Config.URL}api/v1/courier/login", json=payload)
        assert response.status_code == 404
        assert response.json()["message"] == "Учетная запись не найдена"
