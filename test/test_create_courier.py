import pytest
import requests
import json
import string
import random
from src.config import Config
import allure
from helpers import generate_random_string


class TestCreateCourier:
    @allure.title("Создание нового курьера")
    @allure.step("Успешное создание курьера")
    @allure.description("Проверка на статус код = 201, в ответе {'ok':True}")
    def test_create_new_courier(self):
       # Данные для нового курьера
        courier_data = {
            "login": generate_random_string(10),
            "password": generate_random_string(10),
            "firstName": generate_random_string(10)
        }
        # отправляем запрос на создание курьера и сохраняем ответ в переменную response
        response = requests.post(f"{Config.URL}/api/v1/courier", json=courier_data)
        assert response.status_code == 201, f"Курьер не был создан, код ответа: {response.status_code}, текст: {response.text}"
        json_data = response.json()
        assert 'ok' in json_data
        assert json_data['ok'] is True

    @allure.step("Создание дубликата (полный дубликат)")
    @allure.description("Проверка на статус код = 409, в ответе message == Этот логин уже используется. Попробуйте другой.")
    def test_create_duplicate_all_data_courier_error(self, register_new_courier_dict):
        courier_data = register_new_courier_dict
        duplicate_response = requests.post(f"{Config.URL}/api/v1/courier", json=courier_data)
        assert duplicate_response.status_code == 409
        duplicate_response_json = duplicate_response.json()
        assert duplicate_response_json["message"] == "Этот логин уже используется. Попробуйте другой."

    @allure.step("Создание дубликата с повторяющимся логином")
    @allure.description("Проверка на статус код = 409, в ответе message == Этот логин уже используется. Попробуйте другой.")
    def test_create_duplicate_only_login_error(self, register_new_courier_dict):
        courier_data = register_new_courier_dict
        payload = {"login": courier_data["login"], "password": generate_random_string(10), "firstName": generate_random_string(10)}
        duplicate_response = requests.post(f"{Config.URL}/api/v1/courier", json=payload)
        assert duplicate_response.status_code == 409
        duplicate_response_json = duplicate_response.json()
        assert duplicate_response_json["message"] == "Этот логин уже используется. Попробуйте другой."

    @allure.step("Создание курьера без логина")
    @allure.description("Проверка на статус код = 400")
    def test_create_without_login_error(self):
        payload = {"login": None, "password": generate_random_string(10), "firstName": generate_random_string(10)}
        response = requests.post(f"{Config.URL}/api/v1/courier", json=payload)
        assert response.status_code == 400
        assert response.json()["message"] == "Недостаточно данных для создания учетной записи"

    @allure.step("Создание курьера без пароля")
    @allure.description("Проверка на статус код = 400")
    def test_create_without_password_error(self):
        payload = {"login": generate_random_string(10), "password": None, "firstName": generate_random_string(10)}
        response = requests.post(f"{Config.URL}api/v1/courier", json=payload)
        assert response.status_code == 400
        assert response.json()["message"] == "Недостаточно данных для создания учетной записи"

    @allure.step("Создание курьера без фамилии")
    @allure.description("Проверка на статус код = 200")
    def test_create_without_firstname_not_error(self):
        payload = {"login": generate_random_string(10), "password": generate_random_string(10), "firstName": None}
        response = requests.post(f"{Config.URL}/api/v1/courier", json=payload)
        assert response.status_code == 201
        json_data = response.json()
        assert 'ok' in json_data
        assert json_data['ok'] is True





