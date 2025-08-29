import pytest

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from config import base_url
from locators import Locators

class TestConstructorTabs:
    # переходы к разделам "Булки", "Соусы", "Начинки"
    def test_buns_tab_selected_by_default(self, open_main_page): # раздел "Булки" выбран по-умолчанию
        buns_tab = open_main_page.find_element(*Locators.BUNS_TAB)
        assert "tab_tab_type_current" in buns_tab.get_attribute("class")

    def test_sauces_tab_can_be_selected(self, open_main_page): # переход в раздел "Суосы"
        sauces_tab = open_main_page.find_element(*Locators.SAUCES_TAB)
        sauces_tab.click() # переход в раздел "Суосы"
        assert "tab_tab_type_current" in sauces_tab.get_attribute("class")

    def test_fillings_tab_can_be_selected(self, open_main_page): # переход в раздел "Начинки"
        fillings_tab = open_main_page.find_element(*Locators.FILLINGS_TAB)
        fillings_tab.click()
        assert "tab_tab_type_current" in fillings_tab.get_attribute("class")





