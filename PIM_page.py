import pytest
from selenium.webdriver.common.by import By
from time import sleep
from test_data import credentials_det
from login_page import Orangehrm
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class EmployeeAutomation(Orangehrm):
    def __init__(self):
        super().__init__()
        self.all_locators = {
            'pim_xpath': '//a[@href="/web/index.php/pim/viewPimModule"]',
            'add_button': '//button[@class="oxd-button oxd-button--medium oxd-button--secondary"]',
            'first_name': '//input[@placeholder="First Name"]',
            'last_name': '//input[@placeholder="Last Name"]',
            'emp_id': '(//input[@class="oxd-input oxd-input--active"])[2]',
            'save_button': '//button[@type="submit"]',
            'save_details_button': '(//button[@type="submit"])[2]'
        }

    def click_pim(self):
       pim_webelement = self.driver.find_element(By.XPATH, self.login_locators.pim_xpath)
       pim_webelement.click()
       sleep(2)


    def click_add(self):
        add_webelement = self.driver.find_element(By.XPATH, self.login_locators.add_button)
        add_webelement.click()
        sleep(2)


    def input_details(self):
        firstname_webelement = self.driver.find_element(By.XPATH, self.login_locators.first_name)
        firstname_webelement.send_keys(credentials_det.first_name_data)
        sleep(2)

        lastname_webelement = self.driver.find_element(By.XPATH, self.login_locators.last_name)
        lastname_webelement.send_keys(credentials_det.last_name_data)
        sleep(2)

        save1_details_webelement = self.driver.find_element(By.XPATH, self.login_locators.save_details_button)
        save1_details_webelement.click()
        sleep(2)

    def add_emp_details(self):
        self.input_credentials()
        sleep(2)
        self.click_pim()
        sleep(2)
        self.click_add()
        sleep(2)
        self.input_details()
        sleep(2)


if __name__ == '__main__':
    EmployeeAutomation().add_emp_details()