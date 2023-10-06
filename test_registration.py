from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators import Locators


class TestRegistration():
    def tests_registration(self, driver):
        driver.find_element(*Locators.ACCOUNT).click()
        driver.find_element(*Locators.REGISTER_URL).click()
        WebDriverWait(driver, 15).until(expected_conditions.visibility_of_element_located(
            (By.XPATH, '//h2[contains(text(),"Регистрация")]')))


        driver.find_element(*Locators.NAME).send_keys(f'Valeriya_Momzina')
        driver.find_element(*Locators.EMAIL).send_keys(f'Valeriya_Momzina_1111@ya.ru')
        driver.find_element(*Locators.PASSWORD).send_keys(f'12345678')
        driver.find_element(*Locators.REGISTER_BUTTON).click()

    # Пароль с меньшим количеством символов
    def tests_registration_second(self, driver):
        driver.find_element(*Locators.ACCOUNT).click()
        driver.find_element(*Locators.REGISTER_URL).click()
        WebDriverWait(driver, 15).until(expected_conditions.visibility_of_element_located(
            (By.XPATH, '//h2[contains(text(),"Регистрация")]')))

        driver.find_element(*Locators.NAME).send_keys(f'Valeriya_Momzina')
        driver.find_element(*Locators.EMAIL).send_keys(f'Valeriya_Momzina_1111@ya.ru')
        driver.find_element(*Locators.PASSWORD).send_keys(f'1234')
        driver.find_element(*Locators.REGISTER_BUTTON).click()

        assert driver.find_element(By.XPATH, '//p[contains(text(),"Некорректный пароль")]').text == 'Некорректный пароль'

        driver.quit()