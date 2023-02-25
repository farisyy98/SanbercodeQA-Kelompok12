import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


# baseUrl
domain = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"

# TestLogin : test login
class TestLogin(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Chrome(ChromeDriverManager().install())

    # openBrowser - helper func to open browser
    def openBrowser(self) :
        driver = self.browser 
        driver.get(domain) 
        time.sleep(2)
        return driver

    def test_success_login(self):
        driver = self.openBrowser()

        # isi data login
        driver.find_element(By.XPATH, "//input[@placeholder='Username']").send_keys("rikan24x")
        time.sleep(1)
        driver.find_element(By.XPATH, "//input[@placeholder='Password']").send_keys("@Rika_n24x")
        time.sleep(1)
        driver.find_element(By.XPATH, "//button[@type='submit']").click()
        time.sleep(10)
    
if __name__ == "__main__": 
    unittest.main()