import pytest
from src.data import register_new_courier_and_return_login_password
from src.data import create_new_courier_return_list


@pytest.fixture
def register_new_courier_dict():
    courier_data_new = register_new_courier_and_return_login_password()
    return courier_data_new


@pytest.fixture()
def register_new_courier_list():
    courier_data_list = create_new_courier_return_list()
    return courier_data_list



