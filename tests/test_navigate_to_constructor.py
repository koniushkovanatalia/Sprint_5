import pytest

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from config import base_url
from locators import Locators
from data import Credentials


class TestConstructorNavigation:

    def test_navigate_from_personal_account_by_click_constructor_button(self, open_login_page, login, logout): # переход из личного кабинета в конструктор по клику на "Конструктор"
        browser, order_button = login

        assert order_button.is_displayed()

        browser.find_element(*Locators.ACCOUNT_BUTTON).click()

        constructor_button = WebDriverWait(browser, 15).until(
            EC.element_to_be_clickable(Locators.CONSTRUCTOR_BUTTON)
        )
        constructor_button.click()

        order_button = WebDriverWait(browser, 15).until(
            EC.visibility_of_element_located(Locators.ORDER_BUTTON)
        )
        assert order_button.is_displayed()

        logout(browser)

    def test_navigate_from_personal_account_by_click_logo(self, open_login_page, login, logout):  # переход из личного кабинета в конструктор по клику на логотип Stellar Burgers
        browser, order_button = login

        assert order_button.is_displayed()

        browser.find_element(*Locators.ACCOUNT_BUTTON).click()

        logo_button = WebDriverWait(browser, 10).until(
            EC.element_to_be_clickable(Locators.STELLAR_BURGERS_LOGO)
        )
        logo_button.click()

        order_button = WebDriverWait(browser, 15).until(
            EC.visibility_of_element_located(Locators.ORDER_BUTTON)
        )
        assert order_button.is_displayed()

        logout(browser)













