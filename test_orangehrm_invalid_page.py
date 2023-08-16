import pytest
from test_utilities.test_login_module_fail import Orangehrm  # Import the Orangehrm class

class TestInvalidText:

    @pytest.mark.parametrize("expected_text", ["Invalid credentials"])
    def test_tc_login_02(self, expected_text):
        """
        Test case to verify the error text for invalid credentials.
        """

        actual_text = Orangehrm().orangehrm_login()  # Call the orangehrm_login method to get the actual error text

        assert actual_text == expected_text, f"Expected text: {expected_text}, Actual text: {actual_text}"
