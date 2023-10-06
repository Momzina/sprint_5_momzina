from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from locators import Locators

# Переход из Личного кабинета в Конструктор
class TestAccountGoConstructor():
    def test_account_constructor (self, driver, sign_in):
        driver.find_element(*Locators.ACCOUNT).click()
        WebDriverWait(driver, 15).until(expected_conditions.visibility_of_element_located(Locators.PROFILE_URL))
        driver.find_element(*Locators.CONSTR_BUTTON_HEAD).click()
        assert WebDriverWait(driver, 15).until(expected_conditions.visibility_of_element_located(Locators.BURGER_HEADER))

        # Переход из Личного кабинета в Конструктор через логотип Stellar Burgers
    def test_account_constructor_tap_logo_st_burgers(self, driver, sign_in):
        driver.find_element(*Locators.ACCOUNT).click()
        WebDriverWait(driver, 15).until(expected_conditions.visibility_of_element_located(Locators.PROFILE_URL))
        driver.find_element(*Locators.LOGO_ST_BURGER).click()
        assert WebDriverWait(driver, 15).until(expected_conditions.visibility_of_element_located(Locators.BURGER_HEADER))

        driver.quit()
