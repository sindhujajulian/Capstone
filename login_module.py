from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep

from test_data import credentials
from test_locators.all_locators import Loginpagelocators


class Orangehrm:

    def __init__(self):
        self.login_locators = Loginpagelocators()
        self.driver = webdriver.Chrome()
        self.driver.get(credentials.url)
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)

    def login_username(self):
        """
        find the webelement of username,clear the text field and input the username

        :return:
        """
        username_webelement = self.driver.find_element(By.NAME, self.login_locators.username_locator_name_tag)
        username_webelement.clear()
        username_webelement.send_keys(credentials.username)

    def login_password(self):
        """
        find the webelement of password, clear the text field and input the password

        :return:
        """
        password_webelement = self.driver.find_element(By.NAME, self.login_locators.password_locator_name_tag)
        password_webelement.clear()
        password_webelement.send_keys(credentials.password)

    def click_login(self):
        login_button_webelement = self.driver.find_element(By.XPATH, self.login_locators.login_path_xpath)
        login_button_webelement.click()

    def orangehrm_login(self):
        self.login_username()
        self.login_password()
        sleep(2)
        self.click_login()
        sleep(5)

    def title_of_page(self):
        return self.driver.title


if __name__ == '__main__':
    orangehrm_instance = Orangehrm()
    orangehrm_instance.orangehrm_login()
    print("Page title:", orangehrm_instance.title_of_page())  # Call the method on the instance
