import pytest
import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from web_locators.locators import *
from data.urls import Urls
from data.data import ValidData


class TestStellarBurgersRegistration:

    def test_registration_correct_email(self, driver):
        driver.get(Urls.url_register)

        driver.find_element(*AuthRegistre.AR_NAME_FIELD).send_keys(ValidData.user_name)
        driver.find_element(*AuthRegistre.AR_EMAIL_FIELD).send_keys(ValidData.login)
        driver.find_element(*AuthRegistre.AR_PASSWORD_FIELD).send_keys(ValidData.password)

        driver.find_element(*AuthRegistre.AR_REGISTER_BUTTON).click()
        WebDriverWait(driver, 10).until(EC.presence_of_element_located(AuthLogin.AL_ELEMENT_WITH_LOGIN_TEXT))

        login_button = driver.find_element(*AuthLogin.AL_ELEMENT_WITH_LOGIN_TEXT)

        assert driver.current_url == Urls.url_login and login_button.text == 'Вход'

    def test_registration_empty_name(self, driver):
        driver.get(Urls.url_register)

        driver.find_element(*AuthRegistre.AR_EMAIL_FIELD).send_keys('mail@yandex.ru')
        driver.find_element(*AuthRegistre.AR_PASSWORD_FIELD).send_keys('12345678')

        driver.find_element(*AuthRegistre.AR_REGISTER_BUTTON).click()
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(AuthRegistre.AR_REGISTER_BUTTON))
        time.sleep(2)
        errors_messages = driver.find_elements(*AuthRegistre.AR_ERROR_MESSAGE)

        assert driver.current_url == Urls.url_register and len(errors_messages) == 0

    @pytest.mark.parametrize('email_list', ['mail@yandexru', 'mailyandex.ru', 'ma il@yandex.ru', 'mail@yand ex.ru',
                                            '@yandex.ru', 'mail6@.ru', 'mail@yandex.'])
    def test_registration_incorrect_email(self, driver, email_list):
        driver.get(Urls.url_register)

        driver.find_element(*AuthRegistre.AR_NAME_FIELD).send_keys('Петрова Ирина')
        driver.find_element(*AuthRegistre.AR_EMAIL_FIELD).send_keys(email_list)
        driver.find_element(*AuthRegistre.AR_PASSWORD_FIELD).send_keys('12345678')

        driver.find_element(*AuthRegistre.AR_REGISTER_BUTTON).click()
        WebDriverWait(driver, 10).until(EC.presence_of_element_located(AuthRegistre.AR_ERROR_MESSAGE_2))
        error_message = driver.find_element(*AuthRegistre.AR_ERROR_MESSAGE_2)

        assert error_message.text == 'Такой пользователь уже существует'

    @pytest.mark.parametrize('password_list', ['1', '12345'])
    def test_login_incorrect_password(self, driver, password_list):
        driver.get(Urls.url_register)

        driver.find_element(*AuthRegistre.AR_NAME_FIELD).send_keys('Петрова Ирина')
        driver.find_element(*AuthRegistre.AR_EMAIL_FIELD).send_keys('mail@yandex.ru')
        driver.find_element(*AuthRegistre.AR_PASSWORD_FIELD).send_keys(password_list)

        driver.find_element(*AuthRegistre.AR_REGISTER_BUTTON).click()
        WebDriverWait(driver, 10).until(EC.presence_of_element_located(AuthRegistre.AR_ERROR_MESSAGE))
        error_message = driver.find_element(*AuthRegistre.AR_ERROR_MESSAGE)

        assert error_message.text == 'Некорректный пароль'