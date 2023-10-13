from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from data import Data
from locators import MainPageLocators
from locators import AuthPageLocators


class TestLoginAccount():
    # Вход с главной страницы через кнопку" Войти в аккаунт"
    def test_login_main_page(self, driver):
        driver.find_element(*AuthPageLocators.SIGN_IN_BUTTON_TO_ACC).click()
        WebDriverWait(driver, 15).until(expected_conditions.visibility_of_element_located(AuthPageLocators.LOGIN_TO_ACCOUNT))

        driver.find_element(*AuthPageLocators.EMAIL_MAIN).send_keys(Data.email)
        driver.find_element(*AuthPageLocators.PASSWORD_MAIN).send_keys(Data.password)
        driver.find_element(*AuthPageLocators.LOGIN_BUTTON).click()

        assert driver.find_element(*AuthPageLocators.EMAIL_MAIN).get_attribute('value') == Data.email

    # Вход с главной страницы через "Личный кабинет"
    def test_login_to_account_button(self, driver):
        driver.find_element(*MainPageLocators.ACCOUNT).click()
        driver.find_element(*AuthPageLocators.EMAIL_MAIN).send_keys(Data.email)
        driver.find_element(*AuthPageLocators.PASSWORD_MAIN).send_keys(Data.password)
        driver.find_element(*AuthPageLocators.LOGIN_BUTTON).click()

        assert driver.find_element(*AuthPageLocators.EMAIL_MAIN).get_attribute('value') == Data.email