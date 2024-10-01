import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from data.data import PersonData
from data.urls import Urls
from web_locators.locators import *


@pytest.fixture
def driver():
    options = Options()
    options.add_argument("--window-size=1300,1200")
    driver = webdriver.Chrome(options=options)
    driver.get(Urls.url_main_paige)
    yield driver
    driver.quit()

@pytest.fixture
def login(driver):
    driver.get(Urls.url_login)

    driver.find_element(*AuthLogin.AL_EMAIL_FIELD).send_keys(PersonData.login)
    driver.find_element(*AuthLogin.AL_PASSWORD_FIELD).send_keys(PersonData.password)
    driver.find_element(*AuthLogin.AL_LOGIN_BUTTON_ANY_FORMS).click()

    WebDriverWait(driver, 3).until(EC.presence_of_element_located(MainPage.MN_ORDER_BUTTON))
    return driver