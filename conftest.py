
from selenium import webdriver
from runner import User
from selenium.webdriver.support.ui import WebDriverWait
import pytest


@pytest.fixture()
def driver():
    options = webdriver.ChromeOptions()
    options.add_argument('--ignore-certificate-errors')
    # options.add_argument('--headless')
    driver = webdriver.Chrome(options=options)
    driver.set_window_position(1920,0) # Установил, что тесты будут запускать всегда на правом мониторе
    yield driver
    driver.quit()


@pytest.fixture
def wait(driver):
    return WebDriverWait(driver, 10)


@pytest.fixture()
def fin():
    yield (User(login="fin@mail.ru", password="1234567"))

@pytest.fixture()
def fin2():
    yield User(login="65912111@mail.ru", password="qwe150800")