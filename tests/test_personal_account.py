from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from locators import Locators


class TestPersonalAccount():

    def test_go_profile_main(self, driver, sign_in):

        driver.find_element(*Locators.ACCOUNT).click()
        assert WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(Locators.PROFILE_URL))