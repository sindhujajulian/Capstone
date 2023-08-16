from selenium.webdriver.common.by import By
from time import sleep
from login_module import Orangehrm
from test_locators.all_locators import Loginpagelocators


class EmployeeAutomation(Orangehrm):
    def click_pim(self):
       pim_webelement = self.driver.find_element(By.XPATH, self.login_locators.pim_xpath)
       pim_webelement.click()
       sleep(2)


    def click_delete(self):
        delete_webelement = self.driver.find_element(By.XPATH, self.login_locators.delete_button)
        delete_webelement.click()
        sleep(2)



if __name__ == '__main__':
    delete_employee = EmployeeAutomation()
    delete_employee.click_delete()