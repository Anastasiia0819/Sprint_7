import pytest
import requests
import json
from src.config import Config
import random
import string
from helpers import generate_random_string
import allure
from src.data import data_for_order


class TestCreateOrder:
    @allure.title("Создание заказа")
    @allure.step("Успешное создание заказа")
    @pytest.mark.parametrize("color", [(["BLACK"]), (["GREY"]), (["BLACK", "GREY"]), ([])])
    def test_create_order(self, color):
        data_for_order()["color"] = color
        response = requests.post(f"{Config.URL}api/v1/orders", json=data_for_order())
        assert response.status_code == 201
        response_body = response.json()
        assert response_body["track"] is not None
        assert "track" in response_body
