import pytest

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from config import base_url
from locators import Locators
from data import Credentials


def test_login_via_login_button_on_main_page(browser): #вход по кнопке "Войти в аккаунт" на главной странице
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

    logout_button = WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable(Locators.LOGOUT_BUTTON))

    logout_button.click()

    browser.quit()

def test_login_via_account_button_on_main_page(browser): # вход через кнопку "Личный кабинет"

    browser.get(base_url)

    account_button = WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable(Locators.ACCOUNT_BUTTON))

    account_button.click()

    browser.find_element(*Locators.EMAIL).send_keys(Credentials.email)
    browser.find_element(*Locators.PASSWORD).send_keys(Credentials.password)
    browser.find_element(*Locators.LOGIN_BUTTON).click()

    order_button = WebDriverWait(browser, 10).until(
        EC.visibility_of_element_located(Locators.ORDER_BUTTON)
    )
    assert order_button.is_displayed()

    browser.find_element(*Locators.ACCOUNT_BUTTON).click()

    logout_button = WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable(Locators.LOGOUT_BUTTON))

    logout_button.click()

    browser.quit()

def test_login_via_register_form_button(browser): # вход через кнопку в форме регистрации
    browser.get(base_url)

    login_button = WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable(Locators.LOGIN_BUTTON_MAIN)
    )
    login_button.click()

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

    order_button = WebDriverWait(browser, 10).until(
        EC.visibility_of_element_located(Locators.ORDER_BUTTON)
    )
    assert order_button.is_displayed()

    browser.find_element(*Locators.ACCOUNT_BUTTON).click()

    logout_button = WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable(Locators.LOGOUT_BUTTON))

    logout_button.click()

    browser.quit()

def test_login_via_password_recovery_form_button(browser): # вход через кнопку в форме восстановления пароля
    browser.get(base_url)

    login_button = WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable(Locators.LOGIN_BUTTON_MAIN)
    )
    login_button.click()

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

    order_button = WebDriverWait(browser, 10).until(
        EC.visibility_of_element_located(Locators.ORDER_BUTTON)
    )
    assert order_button.is_displayed()

    browser.find_element(*Locators.ACCOUNT_BUTTON).click()

    logout_button = WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable(Locators.LOGOUT_BUTTON))

    logout_button.click()

    browser.quit()











