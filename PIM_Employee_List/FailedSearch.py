import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from element import elem
from Data import addData

class TestEditEmployee(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Chrome(ChromeDriverManager().install())
        # variable data
        self.url = "https://opensource-demo.orangehrmlive.com"

    def tearDown(self):
        self.browser.quit()
       
    def test_search_employee(self):
        #step
        driver = self.browser
        driver.maximize_window()
        driver.get(self.url)  # link url
        time.sleep(3)
        name = driver.find_element(By.NAME, elem.username)
        name.send_keys("Admin")
        password = driver.find_element(By.NAME, elem.password)
        password.send_keys("admin123")
        time.sleep(1)
        driver.find_element(By.TAG_NAME, elem.btnLogin).click()
        time.sleep(3)
        driver.find_element(By.XPATH, elem.menuPIM).click()
        time.sleep(2)
        driver.find_element(By.XPATH, elem.nameEmployee).send_keys(addData.name_false)
        time.sleep(2)

        # Button Search
        driver.find_element(By.XPATH, elem.btnSearchk).click()
        time.sleep(5)


if __name__ == "__main__":
    unittest.main()