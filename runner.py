import random

import locators
from selenium.webdriver.support import expected_conditions as ec
from config import BASE_URL


def generate_email():
    return f"user_test{random.randint(1, 5000)}@example.ru"

def generate_unique_ad_name():
    return f"Объявление_{random.randint(1, 5000)}"

def open_registration(driver, wait):
    driver.get(BASE_URL)
    wait.until(ec.element_to_be_clickable(locators.LOGIN)).click()
    wait.until(ec.visibility_of_element_located(locators.NO_ACCOUNT)).click()


class User:
    login: str
    password: str

    def __init__(self, login: str, password: str):
        self.login = login
        self.password = password

FIN_USER = User(login="fin@mail.ru", password="1234567")
FIN_USER_2 = User(login="65912111@mail.ru", password="qwe150800")
