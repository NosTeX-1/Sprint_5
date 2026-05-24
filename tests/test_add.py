import locators
from selenium.webdriver.support import expected_conditions as ec
from config import BASE_URL
from runner import generate_unique_ad_name
from selenium.webdriver.support.ui import WebDriverWait
from runner import FIN_USER_2

class TestAds:

    def test_create_ad_unauthorized_user(self, driver):
        wait = WebDriverWait(driver, 10)
        driver.get(BASE_URL)
        wait.until(ec.element_to_be_clickable(locators.CREATE_AD_MAIN_BUTTON)).click()
        assert wait.until(ec.visibility_of_element_located(locators.AUTH_PROMPT_TEXT)).text == 'Чтобы разместить объявление, авторизуйтесь'

    def test_create_ad_authorized_user(self, driver):
        wait = WebDriverWait(driver, 10)
        ad_name = generate_unique_ad_name()
        driver.get(BASE_URL)
        wait.until(ec.element_to_be_clickable(locators.LOGIN)).click()
        wait.until(ec.visibility_of_element_located(locators.EMAIL)).send_keys(FIN_USER_2.login)
        driver.find_element(*locators.PASSWORD).send_keys(FIN_USER_2.password)
        driver.find_element(*locators.SUBMIT_LOGIN_BUTTON).click()
        wait.until(ec.invisibility_of_element_located(locators.SUBMIT_LOGIN_BUTTON))
        wait.until(ec.visibility_of_element_located(locators.CREATE_AD_MAIN_BUTTON)).click()
        wait.until(ec.visibility_of_element_located(locators.AD_NAME)).send_keys(ad_name)
        wait.until(ec.visibility_of_element_located(locators.AD_DESCRIPTION)).send_keys("Просто вещь")
        driver.find_element(*locators.AD_PRICE).send_keys("200")
        driver.find_element(*locators.CATEGORY_DROPDOWN).click()
        wait.until(ec.element_to_be_clickable(locators.CATEGORY_NAME)).click()
        driver.find_element(*locators.CITY_DROPDOWN).click()
        wait.until(ec.element_to_be_clickable(locators.CITY_NAME)).click()
        driver.find_element(*locators.CONDITION_USED_CHECKBOX).click()
        driver.find_element(*locators.PUBLISH_BUTTON).click()
        wait.until(ec.presence_of_element_located(locators.PROFILE_BUTTON))
        wait.until(ec.invisibility_of_element_located(locators.PUBLISH_BUTTON))
        driver.find_element(*locators.PROFILE_BUTTON).click()
        wait.until(ec.element_to_be_clickable(locators.PROFILE_BUTTON)).click()
        wait.until(ec.visibility_of_element_located(locators.MY_ADS_FIRST_TITLE))
        object_test_text = driver.find_element(*locators.MY_ADS_FIRST_TITLE).text
        driver.find_element(*locators.MY_ADS_FIRST_TITLE).click()
        driver.find_element(*locators.REMOVE).click()

        assert object_test_text == ad_name
