from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep


from test_data import credentials_det
from test_locators.login_locators import loginPagelocators


class Orangehrm:

    def __init__(self):
        self.login_locators = loginPagelocators()
        self.driver = webdriver.Chrome()
        self.driver.get(credentials_det.url)
        self.driver.maximize_window()
        sleep(5)

    def login_username(self):
        """
        find the webelement of username,clear the text field and input the username

        :return:
        """
        username_webelement = self.driver.find_element(By.NAME, self.login_locators.username_locator_name_tag)
        username_webelement.clear()
        username_webelement.send_keys(credentials_det.username)
        sleep(2)

    def login_password(self):
        """
        find the webelement of password, clear the text field and input the invalid password

        :return:
        """
        password_webelement = self.driver.find_element(By.NAME, self.login_locators.password_locator_name_tag)
        password_webelement.clear()
        password_webelement.send_keys(credentials_det.password)
        sleep(2)

    def click_login(self):
        login_button_webelement = self.driver.find_element(By.XPATH, self.login_locators.login_path_xpath)
        login_button_webelement.click()
        sleep(2)

    def error_text(self):
        invalid_text_webelement = self.driver.find_element(By.XPATH, self.login_locators.invalid_text_xpath)
        return invalid_text_webelement.text

    def orangehrm_login(self):
        self.login_username()
        self.login_password()
        self.click_login()
        error_message = self.error_text()
        return error_message


if __name__ == '__main__':
    Orangehrm().orangehrm_login()
