from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from data import Data
from locators import MainPageLocators, AuthPageLocators


class TestRegistration():

    def tests_registration(self, driver):
        driver.find_element(*MainPageLocators.ACCOUNT).click()
        driver.find_element(*MainPageLocators.REGISTER_URL).click()
        WebDriverWait(driver, 15).until(expected_conditions.visibility_of_element_located(MainPageLocators.SIGN_IN))
        driver.find_element(*MainPageLocators.NAME).send_keys(Data.name)
        driver.find_element(*MainPageLocators.EMAIL).send_keys(Data.email)
        driver.find_element(*MainPageLocators.PASSWORD).send_keys(Data.password)
        driver.find_element(*MainPageLocators.REGISTER_BUTTON).click()
        WebDriverWait(driver, 15).until(expected_conditions.visibility_of_element_located(MainPageLocators.ACCOUNT)).click()
        WebDriverWait(driver, 15).until(expected_conditions.visibility_of_element_located(MainPageLocators.EMAIL_INPUT))

        assert driver.find_element(*AuthPageLocators.LOGIN_TO_ACCOUNT).text == 'Вход'

    # Пароль с меньшим количеством символов
    def tests_registration_second(self, driver):
        driver.find_element(*MainPageLocators.ACCOUNT).click()
        driver.find_element(*MainPageLocators.REGISTER_URL).click()
        WebDriverWait(driver, 15).until(expected_conditions.visibility_of_element_located(MainPageLocators.SIGN_IN))
        driver.find_element(*MainPageLocators.NAME).send_keys(Data.name)
        driver.find_element(*MainPageLocators.EMAIL).send_keys(Data.email)
        driver.find_element(*MainPageLocators.PASSWORD).send_keys(Data.invalid_password)
        driver.find_element(*MainPageLocators.REGISTER_BUTTON).click()

        assert driver.find_element(*MainPageLocators.INCORRECT_PASSWORD).text == 'Некорректный пароль'
