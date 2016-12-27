import pytest
from selenium import webdriver
# from selenium.webdriver.support.ui import Select
# from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

@pytest.mark.usefixtures('before_method')
class TestSimpleSelenium:

    @pytest.fixture(scope='class')
    def before_class(self, request):
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.implicitly_wait(10)
        request.cls.driver = driver
        yield driver
        driver.quit()

    @pytest.fixture()
    def before_method(self, request, before_class):
        request.cls.driver.get('http://the-internet.herokuapp.com/')


    def test_login(self):
        self.driver.find_element_by_link_text('Form Authentication').click()
        username_input = self.driver.find_element_by_id('username')
        password_input = self.driver.find_element_by_id('password')
        submit_button = self.driver.find_element_by_css_selector('button[type="submit"]')
        username_input.send_keys('tomsmith')
        password_input.send_keys('SuperSecretPassword!')
        submit_button.click()
        message = self.driver.find_element_by_id('flash')
        logout_button = self.driver.find_element_by_css_selector('a.button')
        assert logout_button.is_displayed
        assert logout_button.text == 'Logout'
        assert 'You logged into a secure area!' in message.text

    def test_internet(self):
        self.driver.find_element_by_link_text('Form Authentication').click()
        username_input = self.driver.find_element_by_id('username')
        password_input = self.driver.find_element_by_id('password')
        submit_button = self.driver.find_element_by_css_selector('button[type="submit"]')
        username_input.send_keys('tomsmith')
        password_input.send_keys('SuperSecretPassword!')
        submit_button.click()
        message = self.driver.find_element_by_id('flash')
        logout_button = self.driver.find_element_by_css_selector('a.button')
        assert logout_button.is_displayed
        assert logout_button.text == 'Logout'
        assert 'You logged into a secure area!' in message.text

    def test_wait_for_visibility(self):
        self.driver.find_element_by_link_text('Dynamic Loading').click()
        self.driver.find_element_by_partial_link_text('Example 1').click()
        finish_message = self.driver.find_element_by_id('finish')
        assert not finish_message.is_displayed()
        start_button = self.driver.find_element_by_css_selector('#start button')
        start_button.click()
        wait = WebDriverWait(self.driver, 15)
        wait.until
        wait.until(lambda driver: not start_button.is_displayed())
        assert not start_button.is_displayed()
        wait.until(EC.visibility_of(finish_message))
        assert finish_message.is_displayed()
