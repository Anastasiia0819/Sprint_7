import faker
import random
import string


def get_random_data_for_order():
    fake = faker.Faker('ru_RU')
    name = fake.first_name()
    lastname = fake.last_name()
    password = fake.password()
    address = fake.address()
    deliverydate = fake.date_between(start_date='today', end_date='+30d').strftime('%Y-%m-%d')
    comment = fake.text()
    return name, lastname, password, address, deliverydate, comment

    # метод генерирует строку, состоящую только из букв нижнего регистра, в качестве параметра передаём длину строки
def generate_random_string(length):
    letters = string.ascii_lowercase
    random_string = ''.join(random.choice(letters) for i in range(length))
    return random_string