import pytest

from selenium import webdriver

from faker import Faker

from locators import Locators

from data import Credentials

faker = Faker()

@pytest.fixture(params=["chrome", "firefox"]) # запускает браузер, разворачивает окно на весь экран и возвращает драйвер
def browser(request):
    if request.param == "chrome":
        driver = webdriver.Chrome()
    elif request.param == "firefox":
        driver = webdriver.Firefox()
    else:
        raise ValueError(f"Unsupported browser: {request.param}")

    driver.maximize_window()
    return driver

@pytest.fixture # для регистрации с валидными значениями
def generate_registration_data():
    return {
        "name": faker.first_name(),
        "email": faker.email(),
        "password": faker.password(length=6, special_chars=True, digits=True, upper_case=True, lower_case=True)
    }

@pytest.fixture # для регистрации с невалидными значениями
def generate_registration_data_with_short_password():
    return {
        "name": faker.first_name(),
        "email": faker.email(),
        "password": faker.password(length=5, special_chars=True, digits=True, upper_case=True, lower_case=True)  # короткий пароль
    }