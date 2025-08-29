import pytest

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from config import base_url
from locators import Locators
from data import Credentials


class TestProfileNavigation:

    def test_navigate_to_account_page(self, open_login_page, login, logout): # переход по клику на «Личный кабинет»
        browser, order_button = login

        assert order_button.is_displayed()

        browser.find_element(*Locators.ACCOUNT_BUTTON).click()

        profile_button = WebDriverWait(browser, 10).until(
            EC.visibility_of_element_located(Locators.PROFILE_BUTTON))

        assert profile_button.is_displayed()

        logout(browser)









