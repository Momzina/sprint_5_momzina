from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from locators import MainPageLocators, AuthPageLocators


class TestPersonalAccount():

    def test_go_profile_main(self, driver, sign_in):

        driver.find_element(*MainPageLocators.ACCOUNT).click()
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(AuthPageLocators.PROFILE_URL))

        assert driver.find_element(*AuthPageLocators.PROFILE_URL).text == 'Профиль'