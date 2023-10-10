import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from data import Data
from locators import Locators


@pytest.fixture
def driver():
    options = Options()
    options.add_argument("--window_size=1600,900")
    service = Service(ChromeDriverManager().install())
    browser = webdriver.Chrome(options=options, service=service)
    browser.get(Data.url)

    yield browser
    browser.quit()


@pytest.fixture
def sign_in(driver):
    driver.find_element(*Locators.ACCOUNT).click()
    driver.find_element(*Locators.EMAIL_MAIN).send_keys('Valeriya_Momzina_1111@ya.ru')
    driver.find_element(*Locators.PASSWORD_MAIN).send_keys('12345678')
    driver.find_element(*Locators.BUTTON_LOGIN).click()

    return driver
