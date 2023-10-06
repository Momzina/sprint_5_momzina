from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators import Locators


class TestLoginAccount():
    # Вход с главной страницы через кнопку" Войти в аккаунт"
    def test_login_main_page(self, driver):
        driver.find_element(By.XPATH, '//button[contains(text(),"Войти в аккаунт")]').click()
        WebDriverWait(driver, 15).until(expected_conditions.visibility_of_element_located(Locators.LOGIN_TO_ACCOUNT))

        driver.find_element(*Locators.EMAIL_MAIN).send_keys(f'Valeriya_Momzina_1111@ya.ru')
        driver.find_element(*Locators.PASSWORD_MAIN).send_keys(f'12345678')
        driver.find_element(*Locators.LOGIN_BUTTON).click()

    # Вход с главной страницы через "Личный кабинет"
    def test_login_to_account_button(self, driver):
        driver.find_element(*Locators.ACCOUNT).click()
        driver.find_element(*Locators.EMAIL_MAIN).send_keys(f'Valeriya_Momzina_1111@ya.ru')
        driver.find_element(*Locators.PASSWORD_MAIN).send_keys(f'12345678')
        driver.find_element(*Locators.LOGIN_BUTTON).click()

    # Вход через форму "Регистрация"
    def test_login_to_account_registration_form(self, driver):
        driver.find_element(*Locators.ACCOUNT).click()
        driver.find_element(*Locators.REGISTER_URL).click()
        WebDriverWait(driver, 15).until(expected_conditions.visibility_of_element_located(
            (By.XPATH, '//h2[contains(text(),"Регистрация")]')))
        driver.find_element(By.XPATH, '//a[contains(text(),"Войти")]').click()
        WebDriverWait(driver, 15).until(expected_conditions.visibility_of_element_located(Locators.LOGIN_TO_ACCOUNT))
        driver.find_element(*Locators.EMAIL_MAIN).send_keys(f'Valeriya_Momzina_1111@ya.ru')
        driver.find_element(*Locators.PASSWORD_MAIN).send_keys(f'12345678')
        driver.find_element(*Locators.LOGIN_BUTTON).click()

    # Вход черех форму "Восстановления пароля"
    def test_login_to_account_help_password_form(self, driver):
        driver.find_element(*Locators.ACCOUNT).click()
        WebDriverWait(driver, 15).until(expected_conditions.visibility_of_element_located(
            Locators.LOGIN_TO_ACCOUNT))
        driver.find_element(By.XPATH, '//a[contains(text(),"Восстановить пароль")]').click()
        driver.find_element(By.XPATH, '//a[contains(text(),"Войти")]').click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(Locators.LOGIN_TO_ACCOUNT))
        driver.find_element(*Locators.EMAIL_MAIN).send_keys(f'Valeriya_Momzina_1111@ya.ru')
        driver.find_element(*Locators.PASSWORD_MAIN).send_keys(f'12345678')
        driver.find_element(*Locators.LOGIN_BUTTON).click()

        driver.quit()