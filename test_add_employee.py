import pytest
from selenium import webdriver
from time import sleep
from PIM_page import EmployeeAutomation

@pytest.fixture
def driver():
    # Set up the WebDriver instance
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()

def test_add_employee(driver):
    employee_page = EmployeeAutomation(driver)
    employee_page.login(username="admin", password="admin123")
    employee_page.add_emp_details()
    sleep(2)
    employee_page.logout()

if __name__ == "__main__":
    pytest.main(["-v", "test_employee_automation.py"])
