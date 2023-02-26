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

        # Submit
        driver.find_element(By.XPATH, "//button[@type='submit']").click()
        time.sleep(1)
        
        # Auto Klik ke PIM
        driver.find_element(By.XPATH, "//span[text()='PIM']").click()
        time.sleep(1)

        # Auto Klik ke Add Employee
        driver.find_element(By.XPATH, "//li[@class='oxd-topbar-body-nav-tab']").click()
        time.sleep(1)

        # Auto Klik Last Name
        driver.find_element(By.XPATH, "//input[@placeholder='First Name']").send_keys("Nakai")
        time.sleep(1)
        driver.find_element(By.XPATH, "//input[@placeholder='Last Name']").send_keys("Rika")
        time.sleep(1)

        # Klik Create Login Details
        driver.find_element(By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[2]/div/label/span").click()
        time.sleep(1)

        # Isi Nama pada Login Details

        #Isi Username
        driver.find_element(By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[3]/div/div[1]/div/div[2]/input").click()
        time.sleep(1)
        driver.find_element(By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[3]/div/div[1]/div/div[2]/input").send_keys("rika_n24x")
        time.sleep(1)

        #Isi Password
        driver.find_element(By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[4]/div/div[1]/div/div[2]/input").click()
        time.sleep(1)
        driver.find_element(By.XPATH,"/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[4]/div/div[1]/div/div[2]/input").send_keys("@Rika_n24x")
        time.sleep(1)

        #Isi Confirm Password
        driver.find_element(By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[4]/div/div[2]/div/div[2]/input").click()
        time.sleep(1)
        driver.find_element(By.XPATH,"/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[4]/div/div[2]/div/div[2]/input").send_keys("@Rika_n24x")
        time.sleep(1)

        # Submit
        driver.find_element(By.XPATH, "//button[@type='submit']").click()
        time.sleep(10)

if __name__ == "__main__": 
    unittest.main()