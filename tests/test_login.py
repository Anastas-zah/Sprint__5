from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from web_locators.locators import *
from data.urls import Urls
from data.data import PersonData


class TestStellarBurgersLoginLogoutForm:

    def test_login_correct_email_and_password_show_main_page(self, login, driver):
        driver = login

        order_button = driver.find_element(*MainPage.MN_ORDER_BUTTON)
        assert driver.current_url == Urls.url_main_paige and order_button.text == 'Оформить заказ'

    def test_login_sign_in_button_show_login_page(self, driver):

        driver.find_element(*MainPage.MN_AUTH).click()
        WebDriverWait(driver, 8).until(EC.presence_of_element_located(AuthLogin.AL_LOGIN_TEXT))

        driver.find_element(*AuthLogin.AL_EMAIL_FIELD).send_keys(PersonData.login)
        driver.find_element(*AuthLogin.AL_PASSWORD_FIELD).send_keys(PersonData.password)

        driver.find_element(*AuthLogin.AL_LOGIN_BUTTON_ANY_FORMS).click()
        WebDriverWait(driver, 5).until(EC.presence_of_element_located(MainPage.MN_ORDER_BUTTON))

        order_button = driver.find_element(*MainPage.MN_ORDER_BUTTON)
        assert driver.current_url == Urls.url_main_paige and order_button.text == 'Оформить заказ'

    def test_login_personal_account_button_show_login_page(self, driver):

        driver.find_element(*MainPage.MN_PROFILE_BUTTON).click()
        WebDriverWait(driver, 10).until(EC.presence_of_element_located(AuthLogin.AL_LOGIN_TEXT))

        driver.find_element(*AuthLogin.AL_EMAIL_FIELD).send_keys(PersonData.login)
        driver.find_element(*AuthLogin.AL_PASSWORD_FIELD).send_keys(PersonData.password)
        driver.find_element(*AuthLogin.AL_LOGIN_BUTTON_ANY_FORMS).click()

        WebDriverWait(driver, 10).until(EC.presence_of_element_located(MainPage.MN_ORDER_BUTTON))

        order_button = driver.find_element(*MainPage.MN_ORDER_BUTTON)
        assert driver.current_url == Urls.url_main_paige and order_button.text == 'Оформить заказ'

    def test_login_registration_form_sign_in_button(self, driver):
        driver.get(Urls.url_register)

        driver.find_element(*AuthLogin.AL_LOGIN_TEXT_WITH_HREF).click()
        WebDriverWait(driver, 8).until(EC.presence_of_element_located(AuthLogin.AL_LOGIN_TEXT))

        driver.find_element(*AuthLogin.AL_EMAIL_FIELD).send_keys(PersonData.login)
        driver.find_element(*AuthLogin.AL_PASSWORD_FIELD).send_keys(PersonData.password)

        driver.find_element(*AuthLogin.AL_LOGIN_BUTTON_ANY_FORMS).click()
        WebDriverWait(driver, 8).until(EC.presence_of_element_located(MainPage.MN_ORDER_BUTTON))

        order_button = driver.find_element(*MainPage.MN_ORDER_BUTTON)
        assert driver.current_url == Urls.url_main_paige and order_button.text == 'Оформить заказ'

    def test_login_forgot_password_form_sign_in_button(self, driver):
        driver.get(Urls.url_forgot_password)

        driver.find_element(*AuthPassword.AP_LOGIN_TEXT_WITH_HREF).click()
        WebDriverWait(driver, 8).until(EC.presence_of_element_located(AuthLogin.AL_LOGIN_TEXT))

        driver.find_element(*AuthLogin.AL_EMAIL_FIELD).send_keys(PersonData.login)
        driver.find_element(*AuthLogin.AL_PASSWORD_FIELD).send_keys(PersonData.password)

        driver.find_element(*AuthLogin.AL_LOGIN_BUTTON_ANY_FORMS).click()
        WebDriverWait(driver, 8).until(EC.presence_of_element_located(MainPage.MN_ORDER_BUTTON))

        order_button = driver.find_element(*MainPage.MN_ORDER_BUTTON)
        assert driver.current_url == Urls.url_main_paige and order_button.text == 'Оформить заказ'