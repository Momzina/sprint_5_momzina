from selenium.webdriver.common.by import By

class Locators:
    # ВХОД/РЕГИСТРАЦИЯ-КНОПКИ/ССЫЛКИ
    ACCOUNT = (By.XPATH, ".//a[@href='/account']")  # кнопка "Личный кабинет" в шапке
    BUTTON_LOGIN = (By.XPATH, ".//button[text()='Войти']")  # кнопка "Войти" в форме авторизации
    REGISTER_URL = (By.XPATH, ".//a[@href='/register']")  # ссылка на регистарцию
    REGISTER_BUTTON = (By.XPATH, ".//button[text()='Зарегистрироваться']")  # "Кнопка "Зарегистрироваться"

    # РЕГИСТРАЦИЯ
    NAME = (By.XPATH, ".//h2[text()='Регистрация']/..//label[text() = 'Имя']/../input")  # "Имя" регистрации
    EMAIL = (By.XPATH, ".//h2[text()='Регистрация']/..//label[text() = 'Email']/../input")  # "Email" в регистрации
    PASSWORD = (By.XPATH,".//h2[text()='Регистрация']/..//label[text() = 'Пароль']/../input")  # "Пароль" в регистрации

    # ПРОФИЛЬ
    LOGIN_TO_ACCOUNT = (By.XPATH, '//h2[contains(text(),"Вход")]') # "войти в аккаунт" на главной
    LOGIN_BUTTON =  (By.XPATH, '//button[contains(text(),"Войти")]') # кнопка "Войти" после ввода данных
    EMAIL_MAIN = (By.XPATH, '//div/form/fieldset/div/div/input')
    PASSWORD_MAIN = (By.NAME, 'Пароль')
    PROFILE_URL = (By.XPATH, ".//a[text()='Профиль']")  # ссылка "Профиль" в личном кабинете

    # ПЕРЕХОД НА КОНСТРУКТОР
    CONSTR_BUTTON_HEAD = (By.XPATH, ".// p[text() = 'Конструктор']")  # кнопка "Конструктор" в шапке
    LOGO_ST_BURGER = (By.XPATH, ".//div[@class='AppHeader_header__logo__2D0X2']")  # логотип "Stellar Burgers" в шапке
    BURGER_HEADER = (By.XPATH, ".//h1[text()='Соберите бургер']")  # заголовок "Соберите бургер" в конструкторе

    # КОНСТРУКТОР
    BUNS = (By.XPATH, ".//span[text()='Булки']")  # "Булки" в конструкторе
    BUNS_HEADER = (By.XPATH, ".//h2[text()='Булки']")  # заголовок "Булки"
    SAUCES = (By.XPATH, ".//span[text()='Соусы']")  # "Соусы" в конструкторе
    SAUCES_HEADER = (By.XPATH, ".//h2[text()='Соусы']")  # заголовок "Соусы"
    FILLINGS = (By.XPATH, ".//span[text()='Начинки']")  # "Начинки" в конструкторе
    FILLINGS_HEADER = (By.XPATH, ".//h2[text()='Начинки']")  # заголовок "Начинки"
