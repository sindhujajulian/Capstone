from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep

from test_data import credentials_det
from test_locators.all_locators import Loginpagelocators


class Orangehrm:

    def __init__(self):
        self.login_locators = Loginpagelocators()
        self.driver = webdriver.Chrome()
        self.driver.get(credentials_det.url)
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)

    def input_credentials(self):
        username_webelement = self.driver.find_element(By.NAME, self.login_locators.username_locator_name_tag)
        username_webelement.send_keys(credentials_det.username)
        sleep(4)

        password_webelement = self.driver.find_element(By.NAME, self.login_locators.password_locator_name_tag)
        password_webelement.send_keys(credentials_det.password)
        sleep(4)

        login_button_webelement = self.driver.find_element(By.XPATH, self.login_locators.login_path_xpath)
        login_button_webelement.click()
        sleep(5)