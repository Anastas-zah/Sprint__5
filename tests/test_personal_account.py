from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from web_locators.locators import *
from data.urls import Urls


class TestStellarBurgersProfileForm:

    def test_click_profile_button_open_profile_form(self, login, driver):
        driver = login

        driver.find_element(*MainPage.MN_PROFILE_BUTTON).click()

        WebDriverWait(driver, 3).until(EC.presence_of_element_located(LKProfile.LK_INFO_MESSAGE))
        profile = driver.find_element(*LKProfile.LK_HISTORY_SHOP_BUTTON)
        assert Urls.url_profile == driver.current_url and profile.text == 'История заказов'

    def test_click_constructor_button_show_constructor_form(self, login, driver):
        driver = login

        driver.find_element(*MainPage.MN_PROFILE_BUTTON).click()

        WebDriverWait(driver, 3).until(EC.presence_of_element_located(LKProfile.LK_INFO_MESSAGE))
        driver.find_element(*MainPage.MN_CONSTRUCTOR_BUTTON).click()

        h1_tag = driver.find_elements(By.XPATH, ".//h1")
        assert len(h1_tag) > 0 and h1_tag[0].text == 'Соберите бургер'

    def test_click_logo_button_show_constructor_form(self, login, driver):
        driver = login

        driver.find_element(*MainPage.MN_PROFILE_BUTTON).click()

        WebDriverWait(driver, 3).until(EC.presence_of_element_located(LKProfile.LK_INFO_MESSAGE))
        driver.find_element(*MainPage.MN_LOGO).click()

        h1_tag = driver.find_elements(By.XPATH, ".//h1")
        assert len(h1_tag) > 0 and h1_tag[0].text == 'Соберите бургер'

    def test_click_logout_button_in_lk_open_login_form(self, login, driver):
        driver = login

        driver.find_element(*MainPage.MN_PROFILE_BUTTON).click()
        WebDriverWait(driver, 8).until(EC.presence_of_element_located(LKProfile.LK_INFO_MESSAGE))

        driver.find_element(*LKProfile.LK_LOGOUT_BUTTON).click()
        WebDriverWait(driver, 8).until(EC.presence_of_element_located(AuthLogin.AL_LOGIN_BUTTON_ANY_FORMS))

        login_button = driver.find_element(*AuthLogin.AL_ELEMENT_WITH_LOGIN_TEXT)
        assert driver.current_url == Urls.url_login and login_button.text == 'Вход'