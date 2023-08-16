from test_utilities import login_module

def test_login_successful():
    orangehrm = login_module.Orangehrm()
    orangehrm.orangehrm_login()
    actual_title = orangehrm.title_of_page()
    assert actual_title == "OrangeHRM", f"Page title '{actual_title}' does not match expected title."

if __name__ == "__main__":
    test_login_successful()
