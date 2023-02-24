import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


# baseUrl
domain = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"

# TestLogout : test logout
class TestLogout(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Chrome(ChromeDriverManager().install())
    
    # openBrowser - helper func to open browser
    def openBrowser(self) :
        driver = self.browser 
        driver.get(domain) 
        time.sleep(2)
        return driver

    def login_account(self, driver):
        # isi data login
        driver.find_element(By.XPATH, "//input[@placeholder='Username']").send_keys("Admin")
        time.sleep(1)
        driver.find_element(By.XPATH, "//input[@placeholder='Password']").send_keys("admin123")
        time.sleep(1)
        driver.find_element(By.XPATH, "//button[@type='submit']").click()
        time.sleep(1)

    # test_logout - logout case
    def test_logout(self):
        driver = self.openBrowser()

        # login 
        self.login_account(driver)

        # process logout
        driver.find_element(By.XPATH, "//p[@class='oxd-userdropdown-name']").click()
        time.sleep(1)

        menus = driver.find_elements(By.XPATH, "//ul[@class='oxd-dropdown-menu']")
        count = 0
        # iterates through available menus
        for menu in menus : 
            # logout is menus[3]
            if count == 3 :
                menu.click()
            count += 1
        time.sleep(1)

    def tearDown(self):
        self.browser.close()

if __name__ == "__main__":
    unittest.main()