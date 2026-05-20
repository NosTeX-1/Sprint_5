from selenium.webdriver.common.by import By

LOGIN = (By.XPATH, "//button[text()='Вход и регистрация']")
NO_ACCOUNT = (By.XPATH, "//button[text()='Нет аккаунта']")
CREATE_ACCOUNT = (By.XPATH, "//button[text()='Создать аккаунт']")
SUBMIT_LOGIN_BUTTON = (By.XPATH, "//button[text()='Войти']")
LOGOUT_BUTTON = (By.XPATH, "//button[text()='Выйти']")
CREATE_AD_MAIN_BUTTON = (By.CLASS_NAME, "buttonPrimary")
PUBLISH_BUTTON = (By.XPATH, "//button[text()='Опубликовать']")

EMAIL = (By.NAME, "email")
PASSWORD = (By.NAME, "password")
PASSWORD_CONFIRM = (By.NAME, "submitPassword")

PROFILE_AVATAR = (By.CLASS_NAME, 'svgSmall')
PROFILE_NAME = (By.CSS_SELECTOR, '.profileText.name')
PROFILE_BUTTON = (By.CLASS_NAME, 'circleSmall')

ERROR_SPAN = (By.CLASS_NAME, "input_span__yWPqB")
EMAIL_ERROR = (By.XPATH, "//div[contains(@class, 'inputError') and .//input[@name='email']]")
PASSWORD_ERROR = (By.XPATH, "//div[contains(@class, 'inputError') and .//input[@name='password']]")
SUBMIT_PASSWORD_ERROR = (By.XPATH, "//div[contains(@class, 'inputError') and .//input[@name='submitPassword']]")

AUTH_PROMPT_TEXT = (By.CLASS_NAME, "h1")

AD_NAME = (By.NAME, "name")
AD_DESCRIPTION = (By.XPATH, "//textarea[@name='description']")
AD_PRICE = (By.NAME, "price")

CATEGORY_DROPDOWN = (By.XPATH, "//input[@name='category']/following-sibling::button")
CATEGORY_NAME = (By.XPATH, "//span[text()='Садоводство']")
CITY_DROPDOWN = (By.XPATH, "//input[@name='city']/following-sibling::button")
CITY_NAME = (By.XPATH, "//span[text()='Казань']")
CONDITION_USED_CHECKBOX = (By.XPATH, "//label[text()='Б/У']/preceding-sibling::div")
MY_ADS_FIRST_TITLE = (By.XPATH, "//div[contains(@class, 'profilePage_listningBlock')]//div[@class='card'][1]//h2[@class='h2']")