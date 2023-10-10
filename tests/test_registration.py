from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from data import Data
from locators import Locators


class TestRegistration():

    def tests_registration(self, driver):
        driver.find_element(*Locators.ACCOUNT).click()
        driver.find_element(*Locators.REGISTER_URL).click()
        WebDriverWait(driver, 15).until(expected_conditions.visibility_of_element_located(Locators.SIGN_IN))
        driver.find_element(*Locators.NAME).send_keys(Data.name)
        driver.find_element(*Locators.EMAIL).send_keys(Data.email)
        driver.find_element(*Locators.PASSWORD).send_keys(Data.password)
        driver.find_element(*Locators.REGISTER_BUTTON).click()
        WebDriverWait(driver, 15).until(expected_conditions.visibility_of_element_located(Locators.ACCOUNT)).click()
        WebDriverWait(driver, 15).until(expected_conditions.visibility_of_element_located(Locators.EMAIL_INPUT))

    # Пароль с меньшим количеством символов
    def tests_registration_second(self, driver):
        driver.find_element(*Locators.ACCOUNT).click()
        driver.find_element(*Locators.REGISTER_URL).click()
        WebDriverWait(driver, 15).until(expected_conditions.visibility_of_element_located(Locators.SIGN_IN))
        driver.find_element(*Locators.NAME).send_keys(Data.name)
        driver.find_element(*Locators.EMAIL).send_keys(Data.email)
        driver.find_element(*Locators.PASSWORD).send_keys(Data.invalid_password)
        driver.find_element(*Locators.REGISTER_BUTTON).click()

        assert driver.find_element(*Locators.INCORRECT_PASSWORD)
