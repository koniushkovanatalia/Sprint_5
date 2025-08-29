import pytest

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from config import base_url
from locators import Locators
from data import Credentials

from faker import Faker

@pytest.fixture(params=["chrome", "firefox"]) # запускает браузер, разворачивает окно на весь экран и возвращает драйвер
def browser(request):
    if request.param == "chrome":
        driver = webdriver.Chrome()
    elif request.param == "firefox":
        driver = webdriver.Firefox()
    else:
        raise ValueError(f"Unsupported browser: {request.param}")

    driver.maximize_window()
    yield driver
    driver.quit()

@pytest.fixture
def open_main_page(browser): # открытие главной страницы
    browser.get(base_url)
    return browser

@pytest.fixture
def open_login_page(open_main_page): # вход с главной страницы
    login_button = WebDriverWait(open_main_page, 10).until(
        EC.element_to_be_clickable(Locators.LOGIN_BUTTON_MAIN)
    )
    login_button.click()
    return open_main_page

@pytest.fixture
def open_account_login_page(browser): # переход в личный кабинет с главной страницы
    browser.get(base_url)
    account_button = WebDriverWait(browser, 15).until(
        EC.element_to_be_clickable(Locators.ACCOUNT_BUTTON)
    )
    account_button.click()
    return browser

@pytest.fixture
def login(open_main_page): # вход в систему зарегистрированным пользователем
    browser = open_main_page
    browser.find_element(*Locators.EMAIL).send_keys(Credentials.email)
    browser.find_element(*Locators.PASSWORD).send_keys(Credentials.password)
    browser.find_element(*Locators.LOGIN_BUTTON).click()
    order_button = WebDriverWait(browser, 10).until(
        EC.visibility_of_element_located(Locators.ORDER_BUTTON)
    )
    return browser, order_button

@pytest.fixture
def logout(): # выход из системы
    def _logout(browser):
        browser.find_element(*Locators.ACCOUNT_BUTTON).click()
        logout_button = WebDriverWait(browser, 10).until(
            EC.element_to_be_clickable(Locators.LOGOUT_BUTTON)
        )
        logout_button.click()
    return _logout

@pytest.fixture # для регистрации с валидными значениями
def generate_registration_data():
    faker = Faker()
    return {
        "name": faker.first_name(),
        "email": faker.email(),
        "password": faker.password(length=6, special_chars=True, digits=True, upper_case=True, lower_case=True)
    }

@pytest.fixture # для регистрации с невалидными значениями
def generate_registration_data_with_short_password():
    faker = Faker()
    return {
        "name": faker.first_name(),
        "email": faker.email(),
        "password": faker.password(length=5, special_chars=True, digits=True, upper_case=True, lower_case=True)  # короткий пароль
    }