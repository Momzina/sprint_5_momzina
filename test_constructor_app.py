from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from locators import Locators


class TestConstructorSections():

    def test_constructor_buns(self, driver):
        driver.find_element(*Locators.BUNS)
        assert WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(Locators.BUNS_HEADER))

    def test_constructor_sauces(self, driver):
        driver.find_element(*Locators.SAUCES).click()
        assert WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(Locators.SAUCES_HEADER))

    def test_constructor_fillings(self, driver):
        driver.find_element(*Locators.FILLINGS).click()
        assert WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(Locators.FILLINGS_HEADER))


        driver.quit()