from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from data import Data
from locators import Locators


class TestLoginAccount():
    # Вход с главной страницы через кнопку" Войти в аккаунт"
    def test_login_main_page(self, driver):
        driver.find_element(*Locators.SIGN_IN_BUTTON_TO_ACC).click()
        WebDriverWait(driver, 15).until(expected_conditions.visibility_of_element_located(Locators.LOGIN_TO_ACCOUNT))

        driver.find_element(*Locators.EMAIL_MAIN).send_keys(Data.email)
        driver.find_element(*Locators.PASSWORD_MAIN).send_keys(Data.password)
        driver.find_element(*Locators.LOGIN_BUTTON).click()

    # Вход с главной страницы через "Личный кабинет"
    def test_login_to_account_button(self, driver):
        driver.find_element(*Locators.ACCOUNT).click()
        driver.find_element(*Locators.EMAIL_MAIN).send_keys(Data.email)
        driver.find_element(*Locators.PASSWORD_MAIN).send_keys(Data.password)
        driver.find_element(*Locators.LOGIN_BUTTON).click()
