from selenium.webdriver.common.by import By
from time import sleep

from test_data import credentials_det
from login_module import Orangehrm
from test_locators.all_locators import Loginpagelocators

class EmployeeAutomation(Orangehrm):
    def click_pim(self):
       pim_webelement = self.driver.find_element(By.XPATH, self.all_locators.pim_xpath)
       pim_webelement.click()
       sleep(2)


    def click_add(self):
        add_webelement = self.driver.find_element(By.XPATH, self.all_locators.add_button)
        add_webelement.click()
        sleep(2)


    def input_details(self):

        lastname_webelement = self.driver.find_element(By.XPATH, self.all_locators.last_name)
        lastname_webelement.send_keys(credentials_det.last_name_data)
        sleep(2)

        save_details_webelement = self.driver.find_element(By.XPATH, self.all_locators.save_button)
        save_details_webelement.click()
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
    #edit_employee = EmployeeAutomation()
    edit_employee.add_emp_details()