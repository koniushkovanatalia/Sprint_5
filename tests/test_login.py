import pytest

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from config import base_url
from locators import Locators
from data import Credentials


class TestLogin:
    def test_login_via_login_button_on_main_page(self, open_login_page, login, logout): #вход по кнопке "Войти в аккаунт" на главной странице
        browser, order_button = login

        assert order_button.is_displayed()
        logout(browser)

    def test_login_via_account_button_on_main_page(self, open_account_login_page, logout): # вход через кнопку "Личный кабинет"
        browser = open_account_login_page

        browser.find_element(*Locators.EMAIL).send_keys(Credentials.email)
        browser.find_element(*Locators.PASSWORD).send_keys(Credentials.password)
        browser.find_element(*Locators.LOGIN_BUTTON).click()

        order_button = WebDriverWait(browser, 15).until(
            EC.visibility_of_element_located(Locators.ORDER_BUTTON)
        )
        assert order_button.is_displayed()

        logout(browser)

    def test_login_via_register_form_button(self, open_account_login_page, logout): # вход через кнопку в форме регистрации
        browser = open_account_login_page

        register_link = WebDriverWait(browser, 10).until(
            EC.visibility_of_element_located(Locators.REGISTER_LINK_ON_LOGIN_PAGE)
        )
        register_link.click()

        login_link = WebDriverWait(browser, 10).until(
            EC.visibility_of_element_located(Locators.LOGIN_LINK_ON_REGISTER_PAGE)
        )
        login_link.click()

        browser.find_element(*Locators.EMAIL).send_keys(Credentials.email)
        browser.find_element(*Locators.PASSWORD).send_keys(Credentials.password)
        browser.find_element(*Locators.LOGIN_BUTTON).click()

        order_button = WebDriverWait(browser, 15).until(
            EC.visibility_of_element_located(Locators.ORDER_BUTTON)
        )
        assert order_button.is_displayed()

        logout(browser)

    def test_login_via_password_recovery_form_button(self, open_account_login_page, logout): # вход через кнопку в форме восстановления пароля
        browser = open_account_login_page

        fogot_password_link = WebDriverWait(browser, 10).until(
            EC.visibility_of_element_located(Locators.FORGOT_PASSWORD_LINK_ON_LOGIN_PAGE)
        )
        fogot_password_link.click()

        login_link = WebDriverWait(browser, 10).until(
            EC.visibility_of_element_located(Locators.LOGIN_LINK_ON_FORGOT_PASSWORD_PAGE)
        )
        login_link.click()

        browser.find_element(*Locators.EMAIL).send_keys(Credentials.email)
        browser.find_element(*Locators.PASSWORD).send_keys(Credentials.password)
        browser.find_element(*Locators.LOGIN_BUTTON).click()

        order_button = WebDriverWait(browser, 15).until(
            EC.visibility_of_element_located(Locators.ORDER_BUTTON)
        )
        assert order_button.is_displayed()

        logout(browser)











