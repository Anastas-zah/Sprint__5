from web_locators.locators import *


class TestStellarBurgersConstructorForm:

    def test_constructor_go_to_sauces_scroll_to_sauces(self, login, driver):
        driver = login

        driver.find_element(*MainPage.MN_CONSTRUCTOR_BUTTON).click()
        driver.find_element(*MainPage.MN_SAUSES_BUTTON).click()

        h_sauce = driver.find_element(*MainPage.MN_H_SAUSES)

        assert h_sauce.text == 'Соусы'

    def test_constructor_go_to_filling_scroll_to_filling(self, login, driver):
        driver = login

        driver.find_element(*MainPage.MN_CONSTRUCTOR_BUTTON).click()
        driver.find_element(*MainPage.MN_FILLING_BUTTON).click()
        h_filling = driver.find_element(*MainPage.MN_H_FILLING)

        assert h_filling.text == 'Начинки'

    def test_constructor_go_to_bun_scroll_to_bun(self, login, driver):
        driver = login

        driver.find_element(*MainPage.MN_CONSTRUCTOR_BUTTON).click()
        driver.find_element(*MainPage.MN_FILLING_BUTTON).click()
        driver.find_element(*MainPage.MN_BAN_BUTTON).click()

        h_ban = driver.find_element(*MainPage.MN_H_BAN)

        assert h_ban.text == 'Булки'