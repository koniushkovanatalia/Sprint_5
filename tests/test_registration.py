import pytest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from config import login_url, register_url

from locators import Locators

class Test_Registration:

    def test_successful_registration_and_login(self, open_login_page, generate_registration_data): # успешная регистрация
        browser = open_login_page

        register_link = WebDriverWait(browser, 10).until(
            EC.visibility_of_element_located(Locators.REGISTER_LINK_ON_LOGIN_PAGE))

        register_link.click()

        browser.find_element(*Locators.NAME).send_keys(generate_registration_data["name"])
        browser.find_element(*Locators.EMAIL).send_keys(generate_registration_data["email"])
        browser.find_element(*Locators.PASSWORD).send_keys(generate_registration_data["password"])
        browser.find_element(*Locators.REGISTER_BUTTON).click()

        login_button = WebDriverWait(browser, 10).until(EC.presence_of_element_located(Locators.LOGIN_BUTTON))

        assert login_button.is_displayed()


    def test_registration_shows_error_if_password_less_than_6_chars(self, open_login_page, generate_registration_data_with_short_password): # ошибка для некорректного пароля
        browser = open_login_page

        register_link = WebDriverWait(browser, 10).until(
            EC.visibility_of_element_located(Locators.REGISTER_LINK_ON_LOGIN_PAGE))

        register_link.click()

        browser.find_element(*Locators.NAME).send_keys(generate_registration_data_with_short_password["name"])
        browser.find_element(*Locators.EMAIL).send_keys(generate_registration_data_with_short_password["email"])
        browser.find_element(*Locators.PASSWORD).send_keys(generate_registration_data_with_short_password["password"])
        browser.find_element(*Locators.REGISTER_BUTTON).click()

        error_message = WebDriverWait(browser, 10).until(EC.presence_of_element_located(Locators.PASSWORD_ERROR))

        assert error_message.is_displayed()


