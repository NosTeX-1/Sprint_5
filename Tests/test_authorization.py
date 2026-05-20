import locators
from config import BASE_URL, LOGIN_URL
from selenium.webdriver.support import expected_conditions as ec

class Test_authentication():

    def test_login(self, driver, wait, fin):
        driver.get(BASE_URL)
        wait.until(ec.element_to_be_clickable(locators.LOGIN)).click()
        wait.until(ec.visibility_of_element_located(locators.EMAIL)).send_keys(fin.login)
        driver.find_element(*locators.PASSWORD).send_keys(fin.password)
        driver.find_element(*locators.SUBMIT_LOGIN_BUTTON).click()
        assert wait.until(ec.visibility_of_element_located(locators.PROFILE_AVATAR)).is_displayed()
        assert driver.find_element(*locators.PROFILE_NAME).text == 'User.'
        assert driver.current_url == LOGIN_URL

    def test_logout_user(self, driver, wait, fin):

        driver.get(BASE_URL)
        wait.until(ec.element_to_be_clickable(locators.LOGIN)).click()
        wait.until(ec.visibility_of_element_located(locators.EMAIL)).send_keys(fin.login)
        driver.find_element(*locators.PASSWORD).send_keys(fin.password)
        driver.find_element(*locators.SUBMIT_LOGIN_BUTTON).click()
        wait.until(ec.element_to_be_clickable(locators.LOGOUT_BUTTON)).click()
        assert wait.until(ec.invisibility_of_element_located(locators.PROFILE_AVATAR))
        assert wait.until(ec.invisibility_of_element_located(locators.PROFILE_NAME))
        assert driver.find_element(*locators.LOGIN).is_displayed()
