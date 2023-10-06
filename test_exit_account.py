from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators import Locators


class TestExitAccount():
    def test_exit_account(self, driver, sign_in):

        driver.find_element(*Locators.ACCOUNT).click()
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(Locators.PROFILE_URL))
        driver.find_element(By.XPATH, '//button[contains(text(),"Выход")]').click()
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(Locators.LOGIN_TO_ACCOUNT))

        assert driver.find_element(*Locators.LOGIN_TO_ACCOUNT).text == 'Вход'

        driver.quit()
