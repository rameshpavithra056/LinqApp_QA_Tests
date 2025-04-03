from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import unittest

class LinqAppTest(unittest.TestCase):
    
    def setUp(self):
        """Setup Chrome WebDriver"""
        self.driver = webdriver.Chrome()
        self.driver.get("https://staging-web.linqapp.com/welcome")
        self.driver.maximize_window()

    def test_phone_login_field(self):
        """Test if phone number input field is functional"""
        driver = self.driver
        phone_input = driver.find_element(By.XPATH, "//input[@type='tel']")
        phone_input.send_keys("1234567890")
        time.sleep(2)  # Just for visualization
        self.assertEqual(phone_input.get_attribute("value"), "1234567890")
    
    def test_social_login_buttons(self):
        """Test if social login buttons are present"""
        driver = self.driver
        buttons = ["Email", "Apple", "Google", "LinkedIn"]
        for btn in buttons:
            element = driver.find_element(By.XPATH, f"//button[contains(text(), '{btn}')]")
            self.assertTrue(element.is_displayed())
    
    def tearDown(self):
        """Close the browser"""
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
