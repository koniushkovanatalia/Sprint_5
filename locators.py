from selenium.webdriver.common.by import By

class Locators:

    # Шапка
    ACCOUNT_BUTTON = (By.CSS_SELECTOR, "a[href='/account']")  # кнопка "Личный кабинет"
    STELLAR_BURGERS_LOGO = (By.XPATH, "//div[contains(@class, 'AppHeader_header__logo')]//a")  # логотип Stellar Burgers
    CONSTRUCTOR_BUTTON = (By.XPATH, "//p[text()='Конструктор']")  # кнопка "Конструктор"


    # Главная страница
    LOGIN_BUTTON_MAIN = (By.XPATH, "//button[text()='Войти в аккаунт']")  # кнопка "Войти в аккаунт"
    ORDER_BUTTON = (By.XPATH, "//button[text()='Оформить заказ']")  # кнопка "Оформить заказ" на главной странице
    BUNS_TAB = (By.XPATH, "//div[contains(@class, 'tab_tab__1SPyG') and .//span[text()='Булки']]") # раздел "Булки"
    SAUCES_TAB = (By.XPATH, "//div[contains(@class, 'tab_tab__1SPyG') and .//span[text()='Соусы']]") # раздел "Соусы"
    FILLINGS_TAB = (By.XPATH, "//div[contains(@class, 'tab_tab__1SPyG') and .//span[text()='Начинки']]") # раздел "Начинки"

    # Авторизация / регистрация
    NAME = (By.XPATH, "//div[label[text()='Имя']]//input")  # поле "Имя"
    EMAIL = (By.XPATH, "//div[label[text()='Email']]//input")  # поле "Email"
    PASSWORD = (By.XPATH, "//div[label[text()='Пароль']]//input")  # поле "Пароль"
    REGISTER_BUTTON = (By.XPATH, "//button[text()='Зарегистрироваться']")  # кнопка "Зарегистрироваться"
    REGISTER_LINK_ON_LOGIN_PAGE = (By.XPATH, "//a[text()='Зарегистрироваться']")  # кнопка "Зарегистрироваться" на странице авторизации
    LOGIN_BUTTON = (By.XPATH, "//button[text()='Войти']") # кнопка "Войти"
    PASSWORD_ERROR = (By.XPATH, "//p[@class='input__error text_type_main-default']") # ошибка для некорректного пароля
    LOGIN_LINK_ON_REGISTER_PAGE = (By.XPATH, "//a[text()='Войти']")  # кнопка "Войти" на странице регистрации
    FORGOT_PASSWORD_LINK_ON_LOGIN_PAGE = (By.XPATH, "//a[contains(@class,'Auth_link') and text()='Восстановить пароль']")  # кнопка "Восстановить пароль" на странице авторизации
    LOGIN_LINK_ON_FORGOT_PASSWORD_PAGE = (By.XPATH, "//a[contains(@class,'Auth_link') and text()='Войти']")  # кнопка "Войти" на странице восстановления пароля

    # Личный кабинет
    PROFILE_BUTTON = (By.XPATH, "//a[@href='/account/profile' and text()='Профиль']") # кнопка "Профиль"
    LOGOUT_BUTTON = (By.XPATH, "//button[@type='button' and text()='Выход']")  # кнопка "Выход"











