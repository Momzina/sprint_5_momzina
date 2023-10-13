from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from locators import MainPageLocators, AuthPageLocators, ConstrPageLocators


# Переход из Личного кабинета в Конструктор
class TestAccountGoConstructor():
    def test_account_constructor(self, driver, sign_in):
        driver.find_element(*MainPageLocators.ACCOUNT).click()
        WebDriverWait(driver, 15).until(expected_conditions.visibility_of_element_located(AuthPageLocators.PROFILE_URL))
        driver.find_element(*ConstrPageLocators.CONSTR_BUTTON_HEAD).click()
        assert WebDriverWait(driver, 15).until(
            expected_conditions.visibility_of_element_located(ConstrPageLocators.BURGER_HEADER))

        # Переход из Личного кабинета в Конструктор через логотип Stellar Burgers

    def test_account_constructor_tap_logo_st_burgers(self, driver, sign_in):
        driver.find_element(*MainPageLocators.ACCOUNT).click()
        WebDriverWait(driver, 15).until(expected_conditions.visibility_of_element_located(AuthPageLocators.PROFILE_URL))
        driver.find_element(*ConstrPageLocators.LOGO_ST_BURGER).click()
        assert WebDriverWait(driver, 15).until(
            expected_conditions.visibility_of_element_located(ConstrPageLocators.BURGER_HEADER))
