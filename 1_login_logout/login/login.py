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
        driver.find_element(By.XPATH, "//input[@placeholder='Username']").send_keys("Admin")
        time.sleep(1)
        driver.find_element(By.XPATH, "//input[@placeholder='Password']").send_keys("admin123")
        time.sleep(1)
        driver.find_element(By.XPATH, "//button[@type='submit']").click()
        time.sleep(1)

        # validasi
        response_data = driver.find_element(By.XPATH,"//h6[@class='oxd-text oxd-text--h6 oxd-topbar-header-breadcrumb-module']").text
        self.assertIn('Dashboard', response_data)
        time.sleep(1)

    # test_failed_login - wrong password
    def test_failed_login(self):
        driver = self.openBrowser()

        # isi data login
        driver.find_element(By.XPATH, "//input[@placeholder='Username']").send_keys("Admin")
        time.sleep(1)
        driver.find_element(By.XPATH, "//input[@placeholder='Password']").send_keys("admin1234") # wrong password
        time.sleep(1)
        driver.find_element(By.XPATH, "//button[@type='submit']").click()
        time.sleep(1)

        # validasi
        response_data = driver.find_element(By.XPATH,"//p[@class='oxd-text oxd-text--p oxd-alert-content-text']").text
        self.assertIn('Invalid credentials', response_data)
        time.sleep(1)

    def tearDown(self):
        self.browser.close()

if __name__ == "__main__":
    unittest.main()