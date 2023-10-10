from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from locators import Locators


class TestConstructorSections():

    def test_constructor_buns(self, driver):
        element = driver.find_element(*Locators.FILLINGS_HEADER)
        driver.execute_script("arguments[0].scrollIntoView();", element)
        driver.find_element(*Locators.BUNS).click()
        assert WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(Locators.BUNS_HEADER))

    def test_constructor_sauces(self, driver):
        driver.find_element(*Locators.SAUCES).click()
        assert WebDriverWait(driver, 10).until(
            expected_conditions.visibility_of_element_located(Locators.SAUCES_HEADER))

    def test_constructor_fillings(self, driver):
        driver.find_element(*Locators.FILLINGS).click()
        assert WebDriverWait(driver, 10).until(
            expected_conditions.visibility_of_element_located(Locators.FILLINGS_HEADER))
