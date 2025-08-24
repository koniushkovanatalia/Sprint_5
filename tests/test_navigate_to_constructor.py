import pytest

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from config import base_url
from locators import Locators
from data import Credentials

def test_navigate_from_personal_account_by_click_constructor_button(browser): # переход из личного кабинета в конструктор по клику на "Конструктор"
    browser.get(base_url)

    login_button = WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable(Locators.LOGIN_BUTTON_MAIN)
    )
    login_button.click()

    browser.find_element(*Locators.EMAIL).send_keys(Credentials.email)
    browser.find_element(*Locators.PASSWORD).send_keys(Credentials.password)
    browser.find_element(*Locators.LOGIN_BUTTON).click()

    order_button = WebDriverWait(browser, 10).until(
        EC.visibility_of_element_located(Locators.ORDER_BUTTON))

    assert order_button.is_displayed()

    browser.find_element(*Locators.ACCOUNT_BUTTON).click()

    constructor_button = WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable(Locators.CONSTRUCTOR_BUTTON)
    )
    constructor_button.click()

    order_button = WebDriverWait(browser, 10).until(
        EC.visibility_of_element_located(Locators.ORDER_BUTTON))

    assert order_button.is_displayed()

    browser.find_element(*Locators.ACCOUNT_BUTTON).click()

    logout_button = WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable(Locators.LOGOUT_BUTTON))

    logout_button.click()

    browser.quit()

def test_navigate_from_personal_account_by_click_logo(browser):# переход из личного кабинета в конструктор по клику на логотип Stellar Burgers
    browser.get(base_url)

    login_button = WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable(Locators.LOGIN_BUTTON_MAIN)
    )
    login_button.click()

    browser.find_element(*Locators.EMAIL).send_keys(Credentials.email)
    browser.find_element(*Locators.PASSWORD).send_keys(Credentials.password)
    browser.find_element(*Locators.LOGIN_BUTTON).click()

    order_button = WebDriverWait(browser, 10).until(
        EC.visibility_of_element_located(Locators.ORDER_BUTTON))

    assert order_button.is_displayed()

    browser.find_element(*Locators.ACCOUNT_BUTTON).click()

    logo_button = WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable(Locators.STELLAR_BURGERS_LOGO)
    )
    logo_button.click()

    order_button = WebDriverWait(browser, 10).until(
        EC.visibility_of_element_located(Locators.ORDER_BUTTON))

    assert order_button.is_displayed()

    browser.find_element(*Locators.ACCOUNT_BUTTON).click()

    logout_button = WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable(Locators.LOGOUT_BUTTON))

    logout_button.click()

    browser.quit()














