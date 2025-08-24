import pytest

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from config import base_url
from locators import Locators

def test_constructor_tabs(browser): # переходы к разделам "Булки", "Соусы", "Начинки"
    browser.get(base_url)

    buns_tab = browser.find_element(*Locators.BUNS_TAB) # раздел "Булки" выбран по-умолчанию
    assert "tab_tab_type_current" in buns_tab.get_attribute("class")

    sauces_tab = browser.find_element(*Locators.SAUCES_TAB)
    sauces_tab.click() # переход в раздел "Суосы"
    assert "tab_tab_type_current" in sauces_tab.get_attribute("class")

    fillings_tab = browser.find_element(*Locators.FILLINGS_TAB)
    fillings_tab.click() # переход в раздел "Начинки"
    assert "tab_tab_type_current" in fillings_tab.get_attribute("class")

    browser.quit()




