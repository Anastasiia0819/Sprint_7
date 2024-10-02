import pytest
import requests
import json
from src.config import Config
import allure


class TestGetListOrders:
    @allure.title("Получение списка заказов")
    @allure.step("Получение списка всех заказов")
    def test_get_list_orders(self):
        list_order_response = requests.get(f"{Config.URL}api/v1/orders")
        assert list_order_response.status_code == 200
        list_order_response_body = list_order_response.json()
        #Проверка, что в теле ответа есть ключ 'orders'
        assert "orders" in list_order_response_body, "Ответ не содержит ключ 'orders'"
        #Проверка, что список заказов не пуст
        assert len(list_order_response_body["orders"]) > 0, "Список заказов пуст"



