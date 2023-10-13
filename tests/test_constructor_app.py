from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from locators import ConstrPageLocators


class TestConstructorSections():

    def test_constructor_buns(self, driver):
        element = driver.find_element(*ConstrPageLocators .FILLINGS_HEADER)
        driver.execute_script("arguments[0].scrollIntoView();", element)
        driver.find_element(*ConstrPageLocators .BUNS).click()
        assert WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(ConstrPageLocators .BUNS_HEADER))

    def test_constructor_sauces(self, driver):
        driver.find_element(*ConstrPageLocators .SAUCES).click()
        assert WebDriverWait(driver, 10).until(
            expected_conditions.visibility_of_element_located(ConstrPageLocators .SAUCES_HEADER))

    def test_constructor_fillings(self, driver):
        driver.find_element(*ConstrPageLocators .FILLINGS).click()
        assert WebDriverWait(driver, 10).until(
            expected_conditions.visibility_of_element_located(ConstrPageLocators .FILLINGS_HEADER))
