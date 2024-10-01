from selenium.webdriver.common.by import By


class MainPage:
    MN_PROFILE_BUTTON = (By.XPATH, ".//p[text()='Личный Кабинет']")
    MN_AUTH = (By.XPATH, ".//button[text()='Войти в аккаунт']")
    MN_ORDER_BUTTON = (By.XPATH, ".//button[text()='Оформить заказ']")
    MN_CONSTRUCTOR_BUTTON = (By.XPATH, ".//p[text()='Конструктор']")
    MN_LOGO = (By.XPATH, ".//div[@class='AppHeader_header__logo__2D0X2']")

    MN_SAUSES_BUTTON = (By.XPATH, ".//span[text()='Соусы']/parent::*")
    MN_H_SAUSES = By.XPATH, ".//h2[@class='text text_type_main-medium mb-6 mt-10' and text()='Соусы']"

    MN_BAN_BUTTON = (By.XPATH, ".//span[text()='Булки']/parent::*")
    MN_H_BAN = By.XPATH, ".//h2[@class='text text_type_main-medium mb-6 mt-10' and text()='Булки']"

    MN_FILLING_BUTTON = (By.XPATH, ".//span[text()='Начинки']/parent::*")
    MN_H_FILLING = By.XPATH, ".//h2[@class='text text_type_main-medium mb-6 mt-10' and text()='Начинки']"


class AuthLogin:
    AL_LOGIN_TEXT = (By.XPATH, ".//h2[text()='Вход']")
    AL_LOGIN_BUTTON_ANY_FORMS = (By.XPATH, ".//button[text()='Войти']")
    AL_LOGIN_TEXT_WITH_HREF = (By.XPATH, ".//a[text()='Войти']")
    AL_LOGIN_BUTTON = (By.CLASS_NAME, "Auth_link__1f0lj")
    AL_EMAIL_FIELD = (By.XPATH, ".//label[text()='Email']//parent::*/input[@type='text' and @name='name']")
    AL_PASSWORD_FIELD = (By.XPATH, ".//input[@type='password' and @name='Пароль']")
    AL_ELEMENT_WITH_LOGIN_TEXT = (By.XPATH, ".//*[text()='Вход']")


class AuthRegistre:
    AR_NAME_FIELD = (By.XPATH, ".//label[text()='Имя']//parent::*/input[@type='text' and @name='name']")
    AR_EMAIL_FIELD = (By.XPATH, ".//label[text()='Email']//parent::*/input[@type='text' and @name='name']")
    AR_PASSWORD_FIELD = (By.XPATH, ".//input[@type='password' and @name='Пароль']")
    AR_REGISTER_BUTTON = (By.XPATH, ".//button[text()='Зарегистрироваться']")
    AR_ERROR_MESSAGE = (By.XPATH, ".//p[contains(@class, 'input__error')]")
    AR_ERROR_MESSAGE_2 = (By.XPATH, ".//div[@class='Auth_login__3hAey']/p[@class='input__error text_type_main-default']")
    AR_LOGIN_BUTTON = (By.CLASS_NAME, "Auth_link__1fOlj")


class AuthPassword:
    AP_LOGIN_TEXT_WITH_HREF = (By.XPATH, ".//a[text()='Войти']")


class LKProfile:
    LK_LOGOUT_BUTTON = (By.XPATH, ".//button[text()='Выход']")
    LK_INFO_MESSAGE = (By.XPATH, ".//p[contains(text(),'персональные данные')]")
    LK_HISTORY_SHOP_BUTTON = (By.XPATH, ".//li[@class='Account_listItem__35dAP']/a[@class='Account_link__2ETsJ text text_type_main-medium text_color_inactive']")