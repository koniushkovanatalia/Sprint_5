import pytest

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from config import base_url
from locators import Locators
from data import Credentials


class TestLogOut:

    def test_logout_from_personal_account(self, open_login_page, login, logout): # выход по кнопке "Выйти" в личном кабинете
        browser, order_button = login

        assert order_button.is_displayed()

        logout(browser)

        login_button = WebDriverWait(browser, 15).until(
            EC.visibility_of_element_located(Locators.LOGIN_BUTTON)
        )
        assert login_button.is_displayed()

