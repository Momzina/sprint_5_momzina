import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from data import Data
from locators import MainPageLocators, AuthPageLocators



@pytest.fixture()
def driver():
    driver = webdriver.Chrome()
    driver.get(Data.url)

    yield driver
    driver.quit()


@pytest.fixture
def sign_in(driver):
    driver.find_element(*MainPageLocators.ACCOUNT).click()
    driver.find_element(*AuthPageLocators.EMAIL_MAIN).send_keys(Data.email)
    driver.find_element(*AuthPageLocators.PASSWORD_MAIN).send_keys(Data.password)
    driver.find_element(*MainPageLocators.BUTTON_LOGIN).click()

    return driver
