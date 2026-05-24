import locators
from runner import generate_email, open_registration
from selenium.webdriver.support import expected_conditions as ec
from config import REGISTRATION_URL
from selenium.webdriver.support.ui import WebDriverWait


class TestRegistration:

    def test_successful_registration(self, driver):
        email = generate_email()
        wait = WebDriverWait(driver, 10)
        open_registration(driver, wait)
        wait.until(ec.visibility_of_element_located(locators.EMAIL)).send_keys(email)
        driver.find_element(*locators.PASSWORD).send_keys("qwe123")
        driver.find_element(*locators.PASSWORD_CONFIRM).send_keys("qwe123")
        wait.until(ec.element_to_be_clickable(locators.CREATE_ACCOUNT)).click()
        assert wait.until(ec.visibility_of_element_located(locators.PROFILE_AVATAR)).is_displayed()
        assert driver.find_element(*locators.PROFILE_NAME).text == 'User.'
        assert driver.current_url == REGISTRATION_URL

    def test_registration_with_invalid_email(self, driver):
        wait = WebDriverWait(driver, 10)
        open_registration(driver, wait)
        wait.until(ec.visibility_of_element_located(locators.EMAIL)).send_keys("user_email")
        driver.find_element(*locators.PASSWORD).send_keys("qwe123")
        driver.find_element(*locators.PASSWORD_CONFIRM).send_keys("qwe123")
        driver.find_element(*locators.CREATE_ACCOUNT).click()
        assert wait.until(ec.visibility_of_element_located(locators.ERROR_SPAN)).text == 'Ошибка'
        assert driver.find_element(*locators.EMAIL_ERROR).is_displayed()
        assert driver.find_element(*locators.PASSWORD_ERROR).is_displayed()
        assert driver.find_element(*locators.SUBMIT_PASSWORD_ERROR).is_displayed()

    def test_registration_existing_user(self, driver):
        wait = WebDriverWait(driver, 10)
        open_registration(driver, wait)
        wait.until(ec.visibility_of_element_located(locators.EMAIL)).send_keys("mail@mail.ru")
        driver.find_element(*locators.PASSWORD).send_keys("qwe123")
        driver.find_element(*locators.PASSWORD_CONFIRM).send_keys("qwe123")
        driver.find_element(*locators.CREATE_ACCOUNT).click()
        assert wait.until(ec.visibility_of_element_located(locators.ERROR_SPAN)).text == 'Ошибка'
        assert driver.find_element(*locators.EMAIL_ERROR).is_displayed()
        assert driver.find_element(*locators.PASSWORD_ERROR).is_displayed()
        assert driver.find_element(*locators.SUBMIT_PASSWORD_ERROR).is_displayed()
