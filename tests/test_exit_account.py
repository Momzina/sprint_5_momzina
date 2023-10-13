from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from locators import AuthPageLocators, MainPageLocators


class TestExitAccount():
    def test_exit_account(self, driver, sign_in):
        driver.find_element(*MainPageLocators.ACCOUNT).click()
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(AuthPageLocators.PROFILE_URL))
        driver.find_element(*AuthPageLocators.EXIT_BUTTON_ACCOUNT).click()
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(AuthPageLocators.LOGIN_TO_ACCOUNT))

        assert driver.find_element(*AuthPageLocators.LOGIN_TO_ACCOUNT).text == 'Вход'
